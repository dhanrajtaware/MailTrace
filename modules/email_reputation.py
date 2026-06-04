from rich.console import Console
from rich.panel import Panel

console = Console()


FREE_PROVIDERS = [
    "gmail.com",
    "yahoo.com",
    "outlook.com",
    "hotmail.com",
    "live.com",
    "icloud.com",
    "proton.me",
    "protonmail.com"
]

DISPOSABLE_PROVIDERS = [
    "10minutemail.com",
    "mailinator.com",
    "guerrillamail.com",
    "temp-mail.org",
    "yopmail.com"
]


def get_email_category(domain):

    domain = domain.lower()

    if domain.endswith(".gov"):
        return "Government"

    elif domain.endswith(".edu"):
        return "Educational"

    elif domain.endswith(".mil"):
        return "Military"

    elif domain in FREE_PROVIDERS:
        return "Free Provider"

    else:
        return "Corporate"


def is_disposable(domain):

    return domain.lower() in DISPOSABLE_PROVIDERS


def calculate_reputation_score(
    category,
    disposable
):

    score = 100

    if disposable:
        score -= 70

    if category == "Free Provider":
        score -= 10

    if category == "Corporate":
        score += 0

    if category == "Government":
        score += 10

    if category == "Educational":
        score += 5

    if score > 100:
        score = 100

    if score < 0:
        score = 0

    return score


def get_risk_level(score):

    if score >= 80:
        return "Low"

    elif score >= 50:
        return "Medium"

    else:
        return "High"


def analyze_email_reputation(email):

    domain = email.split("@")[1]

    category = get_email_category(
        domain
    )

    disposable = is_disposable(
        domain
    )

    score = calculate_reputation_score(
        category,
        disposable
    )

    results = {

        "Type":
        "Email Reputation",

        "Email":
        email,

        "Domain":
        domain,

        "Category":
        category,

        "Disposable":
        disposable,

        "Reputation Score":
        score,

        "Risk Level":
        get_risk_level(score)
    }

    return results


def display_email_reputation(results):

    output = ""

    for key, value in results.items():

        output += (
            f"[cyan]{key}:[/cyan] "
            f"{value}\n"
        )

    console.print(
        Panel.fit(
            output,
            title="Email Reputation",
            border_style="bright_green"
        )
    )