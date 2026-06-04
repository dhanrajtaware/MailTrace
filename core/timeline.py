from rich.console import Console
from rich.panel import Panel

console = Console()


def show_timeline(
    investigation
):

    timeline = investigation.get(
        "timeline",
        []
    )

    if not timeline:

        console.print(
            Panel(
                "No activity recorded yet.",
                title="Timeline",
                border_style="yellow"
            )
        )

        return

    output = ""

    for item in timeline:

        output += (
            f"[cyan]{item['time']}[/cyan]\n"
            f"{item['event']}\n\n"
        )

    console.print(
        Panel(
            output,
            title="Investigation Timeline",
            border_style="bright_magenta"
        )
    )