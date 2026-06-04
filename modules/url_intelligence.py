from urllib.parse import (
    urlparse,
    parse_qs
)

from rich.console import Console
from rich.panel import Panel

console = Console()


SUSPICIOUS_KEYWORDS = [
    "login",
    "verify",
    "update",
    "banking",
    "secure",
    "account"
]


def url_intelligence(url):

    parsed = urlparse(
        url
    )

    risk = 0

    found_keywords = []

    for keyword in SUSPICIOUS_KEYWORDS:

        if keyword in url.lower():

            risk += 10

            found_keywords.append(
                keyword
            )

    return {

        "Type":
        "URL Intelligence",

        "URL":
        url,

        "Domain":
        parsed.netloc,

        "Path":
        parsed.path,

        "Parameters":
        str(
            parse_qs(
                parsed.query
            )
        ),

        "Suspicious Keywords":
        found_keywords,

        "Risk Score":
        risk
    }


def display_url_results(results):

    output = ""

    for key, value in results.items():

        output += (
            f"[cyan]{key}:[/cyan] "
            f"{value}\n"
        )

    console.print(
        Panel.fit(
            output,
            title="URL Intelligence",
            border_style="yellow"
        )
    )