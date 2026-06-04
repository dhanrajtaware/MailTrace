import requests

from rich.console import Console
from rich.panel import Panel

console = Console()


def geoip_lookup(ip):

    try:

        response = requests.get(
            f"http://ip-api.com/json/{ip}"
        ).json()

        return {

            "Type":
            "GeoIP Intelligence",

            "IP":
            ip,

            "Country":
            response.get(
                "country",
                "Unknown"
            ),

            "Region":
            response.get(
                "regionName",
                "Unknown"
            ),

            "City":
            response.get(
                "city",
                "Unknown"
            ),

            "ISP":
            response.get(
                "isp",
                "Unknown"
            ),

            "Organization":
            response.get(
                "org",
                "Unknown"
            ),

            "ASN":
            response.get(
                "as",
                "Unknown"
            ),

            "Timezone":
            response.get(
                "timezone",
                "Unknown"
            )
        }

    except Exception as e:

        return {

            "Type":
            "GeoIP Intelligence",

            "Error":
            str(e)
        }


def display_geoip_results(results):

    output = ""

    for key, value in results.items():

        output += (
            f"[cyan]{key}:[/cyan] "
            f"{value}\n"
        )

    console.print(
        Panel.fit(
            output,
            title="GeoIP Intelligence",
            border_style="bright_yellow"
        )
    )