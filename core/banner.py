from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from pyfiglet import Figlet

console = Console()


def show_banner():

    figlet = Figlet(
        font="slant"
    )

    banner = figlet.renderText(
        "MailTrace"
    )

    panel_content = (
        f"[bright_magenta]{banner}[/bright_magenta]\n"
        "[bold bright_cyan]EMAIL INTELLIGENCE & INVESTIGATION PLATFORM[/bold bright_cyan]\n\n"
        "[green]OSINT[/green] • "
        "[yellow]DFIR[/yellow] • "
        "[red]THREAT INTELLIGENCE[/red] • "
        "[cyan]INVESTIGATIONS[/cyan]\n\n"
        "[dim]Developed by Dhanraj Taware[/dim]"
    )

    console.print(
        Panel(
            Align.center(
                panel_content
            ),
            border_style="bright_magenta",
            title="[bold cyan]MAILTRACE[/bold cyan]",
            subtitle="[green]ACTIVE[/green]"
        )
    )