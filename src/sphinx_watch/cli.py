"""CLI entrypoint of sphinx-watch."""
import click
import sphinx

from . import __version__


@click.command()
def main():
    click.echo(f"sphinx-watch version is {__version__}")
    click.echo(f"Sphinx version is {sphinx.__display_version__}")
