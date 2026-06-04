from rich.console import Console
from rich.panel import Panel

console = Console()


def detect_hash_type(hash_value):

    length = len(
        hash_value
    )

    if length == 32:
        return "MD5"

    elif length == 40:
        return "SHA1"

    elif length == 64:
        return "SHA256"

    return "Unknown"


def hash_intelligence(hash_value):

    return {

        "Type":
        "Hash Intelligence",

        "Hash":
        hash_value,

        "Length":
        len(hash_value),

        "Hash Type":
        detect_hash_type(
            hash_value
        )
    }


def display_hash_results(results):

    output = ""

    for key, value in results.items():

        output += (
            f"[cyan]{key}:[/cyan] "
            f"{value}\n"
        )

    console.print(
        Panel.fit(
            output,
            title="Hash Intelligence",
            border_style="bright_green"
        )
    )