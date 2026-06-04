from rich.console import Console
from rich.panel import Panel

console = Console()


def show_dashboard(
    investigation
):

    evidence_count = len(
        investigation["evidence"]
    )

    note_count = len(
        investigation["notes"]
    )

    dashboard = f"""

[bright_cyan]CASE[/bright_cyan]
{investigation['name']}

[green]TARGET[/green]
{investigation['target']}

[yellow]NOTES[/yellow]
{note_count}

[magenta]EVIDENCE[/magenta]
{evidence_count}

[red]STATUS[/red]
ACTIVE

"""

    console.print(
        Panel(
            dashboard,
            title="[bold bright_magenta]MAILTRACE CONTROL CENTER[/bold bright_magenta]",
            border_style="bright_cyan"
        )
    )