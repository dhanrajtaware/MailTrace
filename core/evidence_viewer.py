import json

from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax

console = Console()


def view_evidence(
    investigation
):

    evidence_list = investigation.get(
        "evidence",
        []
    )

    if not evidence_list:

        console.print(
            "\n[yellow]No Evidence Found[/yellow]"
        )

        return

    console.print(
        "\n[bold bright_cyan]Evidence List[/bold bright_cyan]\n"
    )

    for index, evidence in enumerate(
        evidence_list,
        start=1
    ):

        console.print(
            f"[cyan]{index}[/cyan] "
            f"- "
            f"{evidence.get('Type', 'Unknown')}"
        )

    choice = input(
        "\nEvidence ID: "
    ).strip()

    try:

        evidence = evidence_list[
            int(choice) - 1
        ]

        evidence_json = json.dumps(
            evidence,
            indent=4,
            ensure_ascii=False
        )

        syntax = Syntax(
            evidence_json,
            "json",
            theme="monokai",
            line_numbers=False
        )

        console.print(
            Panel(
                syntax,
                title=f"Evidence #{choice}",
                border_style="bright_magenta"
            )
        )

    except Exception:

        console.print(
            "\n[red]Invalid Evidence ID[/red]"
        )