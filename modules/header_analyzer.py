import re

from rich.console import Console
from rich.panel import Panel

console = Console()


def extract_ips(headers):

    return list(
        set(
            re.findall(
                r"(?:\d{1,3}\.){3}\d{1,3}",
                headers
            )
        )
    )


def extract_message_id(headers):

    match = re.search(
        r"Message-ID:\s*(.+)",
        headers,
        re.IGNORECASE
    )

    if match:
        return match.group(1).strip()

    return "Not Found"


def extract_spf(headers):

    if "spf=pass" in headers.lower():
        return "PASS"

    elif "spf=fail" in headers.lower():
        return "FAIL"

    return "UNKNOWN"


def extract_dkim(headers):

    if "dkim=pass" in headers.lower():
        return "PASS"

    elif "dkim=fail" in headers.lower():
        return "FAIL"

    return "UNKNOWN"


def extract_dmarc(headers):

    if "dmarc=pass" in headers.lower():
        return "PASS"

    elif "dmarc=fail" in headers.lower():
        return "FAIL"

    return "UNKNOWN"


def count_received_hops(headers):

    return len(
        re.findall(
            r"^Received:",
            headers,
            re.MULTILINE
        )
    )


def analyze_headers(headers):

    results = {}

    results["Type"] = (
        "Header Analysis"
    )

    results["Message ID"] = (
        extract_message_id(
            headers
        )
    )

    results["SPF"] = (
        extract_spf(
            headers
        )
    )

    results["DKIM"] = (
        extract_dkim(
            headers
        )
    )

    results["DMARC"] = (
        extract_dmarc(
            headers
        )
    )

    results["Received Hops"] = (
        count_received_hops(
            headers
        )
    )

    results["IPs Found"] = (
        extract_ips(
            headers
        )
    )

    return results


def display_header_results(results):

    output = ""

    for key, value in results.items():

        output += (
            f"[cyan]{key}:[/cyan] "
            f"{value}\n"
        )

    console.print(
        Panel(
            output,
            title="Header Analysis",
            border_style="bright_magenta"
        )
    )