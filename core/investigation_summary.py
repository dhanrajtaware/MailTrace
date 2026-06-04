from rich.console import Console
from rich.panel import Panel

console = Console()


def show_summary(
    investigation
):

    modules = set()

    for evidence in investigation.get(
        "evidence",
        []
    ):

        modules.add(
            evidence.get(
                "Type",
                "Unknown"
            )
        )

    summary = f"""

[bright_cyan]Case Name[/bright_cyan]
{investigation['name']}

[green]Target[/green]
{investigation['target']}

[yellow]Created[/yellow]
{investigation['created']}

[magenta]Status[/magenta]
{investigation.get('status', 'ACTIVE')}

[cyan]Notes[/cyan]
{len(investigation['notes'])}

[red]Evidence[/red]
{len(investigation['evidence'])}

[bright_green]Modules Used[/bright_green]
{", ".join(sorted(modules)) if modules else "None"}
"""

    console.print(
        Panel(
            summary,
            title="Investigation Summary",
            border_style="bright_green"
        )
    )