import requests

from rich.console import Console
from rich.panel import Panel

console = Console()


def username_intelligence(username):

    platforms = {

        "GitHub":
        f"https://github.com/{username}",

        "Reddit":
        f"https://www.reddit.com/user/{username}",

        "Pinterest":
        f"https://www.pinterest.com/{username}",

        "TikTok":
        f"https://www.tiktok.com/@{username}"
    }

    results = {
        "Type": "Username Intelligence",
        "Username": username,
        "Profiles": []
    }

    for platform, url in platforms.items():

        try:

            response = requests.get(
                url,
                timeout=5
            )

            if response.status_code == 200:

                results[
                    "Profiles"
                ].append(
                    f"{platform}: {url}"
                )

        except:

            pass

    return results


def display_username_results(results):

    output = ""

    for key, value in results.items():

        output += (
            f"[cyan]{key}:[/cyan] "
            f"{value}\n"
        )

    console.print(
        Panel.fit(
            output,
            title="Username Intelligence",
            border_style="bright_magenta"
        )
    )