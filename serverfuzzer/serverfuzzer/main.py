"""Perform an automated fuzzing campaign to find a defect in a JSON-processing server."""

import typer
from rich.console import Console

from serverfuzzer.server import process_json

# TODO: Add all of the required imports here

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a console for rich text output
console = Console()

# TODO: Add all of the required functions here


@cli.command()
def serverfuzzer(
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose output."
    ),
) -> None:
    """Conduct a fuzzing campaign to automatically find a JSON processing defect."""
    console.print(
        "\n:runner: Performing a fuzzing campaign on a server that processes JSON!"
    )
    console.print(
        f":question: Should the fuzzing campaign produce verbose output? {verbose}"
    )
    console.print()
    # TODO: Implement a function that meets all of the
    # requirements outlined in the README.md file
