from rich.console import Console
from rich.panel import Panel

console = Console()

KNOWN_BREACHES = {
    "test@gmail.com": [
        "LinkedIn 2012",
        "Adobe 2013"
    ],
    "admin@yahoo.com": [
        "Dropbox 2012"
    ]
}


def breach_lookup(email):

    breaches = KNOWN_BREACHES.get(
        email.lower(),
        []
    )

    return {
        "Type": "Breach Intelligence",
        "Email": email,
        "Breaches Found": len(breaches),
        "Breaches": breaches
    }


def display_breach_results(results):

    output = ""

    for key, value in results.items():

        output += (
            f"[cyan]{key}:[/cyan] "
            f"{value}\n"
        )

    console.print(
        Panel.fit(
            output,
            title="Breach Intelligence",
            border_style="red"
        )
    )