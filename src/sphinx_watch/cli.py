"""CLI entrypoint of sphinx-watch."""
from pathlib import Path

import click
import sphinx

from . import __version__


@click.command()
@click.argument(
    "source_dir",
    type=click.Path(
        exists=True, file_okay=False, dir_okay=True, path_type=Path, resolve_path=True
    ),
)
@click.argument(
    "build_dir",
    type=click.Path(
        exists=True, file_okay=False, dir_okay=True, path_type=Path, resolve_path=True
    ),
)
@click.argument("builder", type=click.STRING)
def main(source_dir: Path, build_dir: Path, builder: str):
    click.echo(f"sphinx-watch version is {__version__}")
    click.echo(f"Sphinx version is {sphinx.__display_version__}")
    click.echo(f"Env is:\n\t{source_dir=}\n\t{build_dir=}\n\t{builder=}\n")
