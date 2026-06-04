from rich.console import Console
from rich.progress import (
    Progress,
    BarColumn,
    TextColumn,
    TimeElapsedColumn
)
import time

console = Console()


def startup_loading():

    modules = [

        "Email Intelligence Engine",
        "Header Analyzer",
        "IOC Extraction Engine",
        "Email Reputation Engine",
        "Domain Intelligence",
        "GeoIP Intelligence",
        "Threat Intelligence",
        "Investigation Core",
        "Reporting Engine"
    ]

    console.print()

    for module in modules:

        with console.status(
            f"[bold cyan]Loading {module}...",
            spinner="dots12"
        ):

            time.sleep(0.7)

        console.print(
            f"[green]✓[/green] {module}"
        )

    console.print()

    console.print(
        "[bold green]✓ ACCESS GRANTED[/bold green]"
    )

    time.sleep(1)

def task_loading(text):

    with console.status(
        f"[bold cyan]{text}",
        spinner="arc"
    ):

        time.sleep(1.5)