"""For watchdog handlers."""
import threading
import time
from dataclasses import dataclass
from pathlib import Path
from typing import List

from sphinx.cmd.build import main as sphinx_build
from watchdog.events import RegexMatchingEventHandler


@dataclass
class SphinxBuildContext:
    source_dir: Path
    build_dir: Path
    builder_name: str

    @property
    def argv(self) -> List[str]:
        return ["-b", self.builder_name, str(self.source_dir), str(self.build_dir)]


class SphinxSourceEventHandler(RegexMatchingEventHandler):
    def __init__(
        self,
        source_dir: Path,
        build_dir: Path,
        builder_name: str,
        extensions=["rst"],
        case_sensitive: bool = False,
    ):
        super_args = {
            "case_sensitive": case_sensitive,
            "ignore_directories": [str(build_dir)],
        }
        super_args["regexes"] = rf"{source_dir}/*.*\.{'|'.join(extensions)}$"
        super().__init__(**super_args)
        self.build_context = SphinxBuildContext(
            source_dir=source_dir, build_dir=build_dir, builder_name=builder_name
        )
        self._can_build = False
        self._can_loop = True
        self.worker = threading.Thread(target=self.watch_build)
        self.worker.start()

    def watch_build(self):
        while self._can_loop:
            if not self._can_build:
                continue
            sphinx_build(self.build_context.argv)
            time.sleep(1)
            self._can_build = False

    def stop_watch(self):
        self._can_loop = False
        time.sleep(1)
        self.worker.join()

    def on_any_event(self, event):
        self._can_build = True
