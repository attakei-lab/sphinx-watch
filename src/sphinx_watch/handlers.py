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
    """Management params passing to Sphinx CMD."""

    source_dir: Path
    build_dir: Path
    builder_name: str

    @property
    def argv(self) -> List[str]:
        """Return arguments style."""
        return ["-b", self.builder_name, str(self.source_dir), str(self.build_dir)]


class SphinxSourceEventHandler(RegexMatchingEventHandler):
    """Includes build trigger for Sphinx."""

    def __init__(
        self,
        source_dir: Path,
        build_dir: Path,
        builder_name: str,
        extensions=["rst"],
        case_sensitive: bool = False,
    ):  # noqa: D107
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
        self._can_loop = False
        self._thread = threading.Thread(target=self.watch_build)

    def watch_build(self):
        """Core loop to watch build flag.

        This method is called as thread target.
        """
        while self._can_loop:
            time.sleep(1)
            if not self._can_build:
                continue
            sphinx_build(self.build_context.argv)
            # NOTE: Set value not with reason.
            self._can_build = False

    def start_watch(self):
        """Start loop of ``watch_build`` from outside."""
        self._can_loop = True
        self._thread.start()

    def stop_watch(self):
        """Stop loop of ``watch_build``.

        This method is called by main loop (obeserver works).
        """
        self._can_loop = False
        # NOTE: Set value not with reason. (same to watch_build)
        time.sleep(1)
        self._thread.join()

    def on_any_event(self, event):
        """Set flag only (main build works at ``watch_build``)."""
        self._can_build = True
