import whois
import dns.resolver

from datetime import datetime
from rich.console import Console
from rich.panel import Panel

console = Console()


def get_domain_age(
    creation_date
):

    try:

        if isinstance(
            creation_date,
            list
        ):
            creation_date = creation_date[0]

        age = (
            datetime.now() -
            creation_date.replace(
                tzinfo=None
            )
        ).days

        return age

    except:

        return "Unknown"


def get_dnssec_status(
    domain
):

    try:

        dns.resolver.resolve(
            domain,
            "DNSKEY"
        )

        return "Enabled"

    except:

        return "Disabled"


def domain_intelligence(
    domain
):

    results = {}

    try:

        w = whois.whois(
            domain
        )

        results["Type"] = (
            "Domain Intelligence"
        )

        results["Domain"] = (
            domain
        )

        results["Registrar"] = str(
            w.registrar
        )

        results["Creation Date"] = str(
            w.creation_date
        )

        results["Expiration Date"] = str(
            w.expiration_date
        )

        results["Domain Age"] = (
            get_domain_age(
                w.creation_date
            )
        )

        results["Organization"] = str(
            getattr(
                w,
                "org",
                "Unknown"
            )
        )

        results["Country"] = str(
            getattr(
                w,
                "country",
                "Unknown"
            )
        )

        results["Nameservers"] = str(
            w.name_servers
        )

        results["DNSSEC"] = (
            get_dnssec_status(
                domain
            )
        )

        return results

    except Exception as e:

        return {
            "Type":
            "Domain Intelligence",

            "Domain":
            domain,

            "Error":
            str(e)
        }


def display_domain_intelligence(
    results
):

    output = ""

    for key, value in results.items():

        output += (
            f"[cyan]{key}:[/cyan] "
            f"{value}\n"
        )

    console.print(
        Panel.fit(
            output,
            title="Domain Intelligence",
            border_style="bright_blue"
        )
    )