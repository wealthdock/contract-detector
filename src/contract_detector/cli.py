"""Command-line interface for contract_detector."""

import typer

from contract_detector import __version__

app = typer.Typer(help="Detects recurring contracts and subscriptions.")


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(__version__)
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        False,
        "--version",
        callback=_version_callback,
        is_eager=True,
        help="Show the version and exit.",
    ),
) -> None:
    """contract-detector CLI."""


if __name__ == "__main__":
    app()
