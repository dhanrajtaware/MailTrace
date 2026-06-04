import re

from rich.console import Console
from rich.panel import Panel

console = Console()


def extract_emails(text):

    return list(
        set(
            re.findall(
                r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
                text
            )
        )
    )


def extract_domains(text):

    return list(
        set(
            re.findall(
                r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b",
                text
            )
        )
    )


def extract_urls(text):

    return list(
        set(
            re.findall(
                r"https?://[^\s]+",
                text
            )
        )
    )


def extract_ips(text):

    return list(
        set(
            re.findall(
                r"(?:\d{1,3}\.){3}\d{1,3}",
                text
            )
        )
    )


def extract_md5(text):

    return list(
        set(
            re.findall(
                r"\b[a-fA-F0-9]{32}\b",
                text
            )
        )
    )


def extract_sha1(text):

    return list(
        set(
            re.findall(
                r"\b[a-fA-F0-9]{40}\b",
                text
            )
        )
    )


def extract_sha256(text):

    return list(
        set(
            re.findall(
                r"\b[a-fA-F0-9]{64}\b",
                text
            )
        )
    )


def extract_iocs(text):

    results = {

        "Type":
        "IOC Extraction",

        "Emails":
        extract_emails(text),

        "Domains":
        extract_domains(text),

        "URLs":
        extract_urls(text),

        "IPs":
        extract_ips(text),

        "MD5":
        extract_md5(text),

        "SHA1":
        extract_sha1(text),

        "SHA256":
        extract_sha256(text)
    }

    return results


def display_iocs(results):

    output = ""

    for key, value in results.items():

        output += (
            f"[cyan]{key}:[/cyan] "
            f"{value}\n\n"
        )

    console.print(
        Panel(
            output,
            title="IOC Extraction",
            border_style="bright_red"
        )
    )