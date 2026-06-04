import dns.resolver
import whois
import socket
import hashlib
import requests

from ipwhois import IPWhois
from rich.console import Console
from rich.panel import Panel
from datetime import datetime

console = Console()


def detect_provider(mx_records):

    mx_text = " ".join(mx_records).lower()

    if "google" in mx_text:
        return "Google Workspace"

    elif "outlook" in mx_text:
        return "Microsoft 365"

    elif "zoho" in mx_text:
        return "Zoho Mail"

    elif "proton" in mx_text:
        return "ProtonMail"

    elif "yandex" in mx_text:
        return "Yandex Mail"

    else:
        return "Unknown"


def calculate_risk_score(results):

    score = 50

    if results["SPF"]:
        score += 15

    if results["DMARC"]:
        score += 15

    if len(results["MX Records"]) > 0:
        score += 10

    if score > 100:
        score = 100

    return score


def gravatar_lookup(email):

    try:

        email_hash = hashlib.md5(
            email.lower().encode()
        ).hexdigest()

        url = (
            f"https://www.gravatar.com/avatar/"
            f"{email_hash}?d=404"
        )

        response = requests.get(url)

        if response.status_code == 200:

            return {
                "Gravatar Found": True,
                "Avatar URL": url
            }

        return {
            "Gravatar Found": False
        }

    except:

        return {
            "Gravatar Found": False
        }

def username_correlation(username):

    return {

        "GitHub":
        f"https://github.com/{username}",

        "Reddit":
        f"https://reddit.com/u/{username}",

        "Pinterest":
        f"https://pinterest.com/{username}",

        "Medium":
        f"https://medium.com/@{username}"
    }

def get_mx_infrastructure(mx_records):

    infrastructure = []

    for mx in mx_records:

        try:

            ip = socket.gethostbyname(
                str(mx).rstrip(".")
            )

            obj = IPWhois(ip)

            result = obj.lookup_rdap()

            infrastructure.append({
                "Host": str(mx),
                "IP": ip,
                "ASN": result.get(
                    "asn",
                    "Unknown"
                ),
                "Organization": result.get(
                    "network",
                    {}
                ).get(
                    "name",
                    "Unknown"
                )
            })

        except:

            pass

    return infrastructure

def email_lookup(email):

    results = {}

    try:

        username = email.split("@")[0]
        domain = email.split("@")[1]

        results["Email"] = email
        results["Username"] = username
        results["Domain"] = domain

        results["Domain Type"] = (
            classify_domain(domain)
        )

        results["Email Category"] = (
            get_email_category(domain)
        )

        results["Disposable"] = (
            is_disposable(domain)
        )

        domain_data = (
            get_domain_intelligence(domain)
        )

        results.update(domain_data)

        # MX RECORDS

        try:

            mx_records = dns.resolver.resolve(
                domain,
                "MX"
            )

            results["MX Records"] = [
                str(record.exchange)
                for record in mx_records
            ]

        except:

            results["MX Records"] = []

        # SPF

        results["SPF"] = False

        try:

            txt_records = dns.resolver.resolve(
                domain,
                "TXT"
            )

            for record in txt_records:

                text = str(record)

                if "v=spf1" in text.lower():

                    results["SPF"] = True
                    results["SPF Record"] = text

                    break

        except:

            pass

        # DMARC

        results["DMARC"] = False

        try:

            dmarc_domain = (
                f"_dmarc.{domain}"
            )

            dmarc_records = dns.resolver.resolve(
                dmarc_domain,
                "TXT"
            )

            for record in dmarc_records:

                text = str(record)

                if "v=dmarc1" in text.lower():

                    results["DMARC"] = True
                    results["DMARC Record"] = text

                    break

        except:

            pass

        # PROVIDER

        results["Provider"] = (
            detect_provider(
                results["MX Records"]
            )
        )

        results["Profiles"] = (
            username_correlation(
                username
            )
        )

        results["MX Infrastructure"] = (
            get_mx_infrastructure(
                results["MX Records"]
            )
        )

        # RISK SCORE

        results["Risk Score"] = (
            calculate_risk_score(
                results
            )
        )

        if results["Risk Score"] >= 80:

            results["Risk Level"] = "Low"

        elif results["Risk Score"] >= 50:

            results["Risk Level"] = "Medium"

        else:

            results["Risk Level"] = "High"

        results.update(
            gravatar_lookup(email)
        )

        return results

    except Exception as e:

        console.print(
            f"[red]{e}[/red]"
        )

        return None


def get_domain_intelligence(domain):

    data = {}

    try:

        w = whois.whois(domain)

        data["Registrar"] = str(
            w.registrar
        )

        data["Creation Date"] = str(
            w.creation_date
        )

        data["Expiration Date"] = str(
            w.expiration_date
        )

        data["Nameservers"] = str(
            w.name_servers
        )

        try:

            created = w.creation_date

            if isinstance(created, list):
                created = created[0]

            age = (
                datetime.now() -
                created.replace(
                    tzinfo=None
                )
            ).days

            data["Domain Age"] = (
                f"{age} Days"
            )

        except:

            data["Domain Age"] = (
                "Unknown"
            )

        return data

    except:

        return {
            "Registrar": "Unknown",
            "Creation Date": "Unknown",
            "Expiration Date": "Unknown",
            "Nameservers": "Unknown",
            "Domain Age": "Unknown"
        }
    
def classify_domain(domain):

    domain = domain.lower()

    if domain.endswith(".gov"):
        return "Government"

    elif domain.endswith(".edu"):
        return "Educational"

    elif domain.endswith(".mil"):
        return "Military"

    elif domain.endswith(".org"):
        return "Organization"

    else:
        return "Commercial"
    
def is_disposable(domain):

    disposable_domains = [
        "10minutemail.com",
        "guerrillamail.com",
        "temp-mail.org",
        "mailinator.com",
        "yopmail.com"
    ]

    return domain.lower() in disposable_domains


def get_email_category(domain):

    domain = domain.lower()

    if ".gov" in domain:
        return "Government"

    elif ".edu" in domain:
        return "Educational"

    elif ".mil" in domain:
        return "Military"

    elif is_disposable(domain):
        return "Disposable"

    else:
        return "Corporate / Personal"


def display_email_results(results):

    output = ""

    for key, value in results.items():

        output += (
            f"[cyan]{key}:[/cyan] "
            f"{value}\n"
        )

    console.print(
        Panel(
            output,
            title="Email Intelligence",
            border_style="bright_cyan"
        )
    )