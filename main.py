from rich.console import Console
from rich.table import Table

from core.banner import show_banner
from core.dashboard import show_dashboard
from core.loading import (
    startup_loading,
    task_loading
)
from core.storage import (
    create_investigation,
    save_investigation,
    load_investigation,
    list_investigations,
    add_note,
    add_evidence,
    add_timeline_event
)
from core.investigation_summary import (
    show_summary
)
from core.evidence_viewer import (
    view_evidence
)
from modules.breach_lookup import (
    breach_lookup,
    display_breach_results
)

from modules.username_intelligence import (
    username_intelligence,
    display_username_results
)

from modules.url_intelligence import (
    url_intelligence,
    display_url_results
)

from modules.hash_intelligence import (
    hash_intelligence,
    display_hash_results
)
from modules.email_reputation import (
    analyze_email_reputation,
    display_email_reputation
)
from core.timeline import (
    show_timeline
)
from modules.domain_intelligence import (
    domain_intelligence,
    display_domain_intelligence
)
from modules.geoip_lookup import (
    geoip_lookup,
    display_geoip_results
)
from modules.ioc_extractor import (
    extract_iocs,
    display_iocs
)
from core.report_generator import (
    generate_pdf_report
)
from core.utils import clear_screen

from modules.email_lookup import (
    email_lookup,
    display_email_results
)

from modules.header_analyzer import (
    analyze_headers,
    display_header_results
)

console = Console()


def show_main_menu():

    table = Table(
        title="MAILTRACE MAIN MENU",
        show_lines=True
    )

    table.add_column(
        "Option",
        style="bright_cyan"
    )

    table.add_column(
        "Action",
        style="bright_green"
    )

    table.add_row(
        "1",
        "New Investigation"
    )

    table.add_row(
        "2",
        "Load Investigation"
    )

    table.add_row(
        "3",
        "Exit"
    )

    console.print(table)


def show_investigation_menu():

    table = Table(
        title="INVESTIGATION MENU",
        show_lines=True
    )

    table.add_column(
        "Option",
        style="bright_cyan"
    )

    table.add_column(
        "Action",
        style="bright_green"
    )

    table.add_row(
        "1",
        "Email Intelligence"
    )

    table.add_row(
        "2",
        "Add Note"
    )

    table.add_row(
        "3",
        "View Notes"
    )

    table.add_row(
        "4",
        "View Evidence"
    )

    table.add_row(
        "5",
        "Save Investigation"
    )

    table.add_row(
        "6",
        "Generate PDF Report"
    )

    table.add_row(
        "7",
        "Close Investigation"
    )

    table.add_row(
        "8",
        "Header Analysis"
    )

    table.add_row(
        "9",
        "IOC Extraction"
    )
    table.add_row(
        "10",
        "Email Reputation"
    )
    table.add_row(
        "11",
        "Domain Intelligence"
    )
    table.add_row(
        "12",
        "GeoIP Intelligence"
    )
    table.add_row(
    "13",
    "Threat Intelligence"
    )

    table.add_row(
    "14",
    "Breach Intelligence"
    )

    table.add_row(
        "15",
        "Username Intelligence"
    )

    table.add_row(
        "16",
        "URL Intelligence"
    )

    table.add_row(
        "17",
        "Hash Intelligence"
    )
    table.add_row(
    "19",
    "Timeline"
    )
    table.add_row(
    "18",
    "Investigation Summary"
    )
    table.add_row(
    "20",
    "Change Status"
    )

    console.print(table)


def investigation_loop(
    investigation
):

    while True:

        clear_screen()

        show_banner()

        show_dashboard(
            investigation
        )

        show_investigation_menu()

        choice = input(
            "\nMailTrace > "
        ).strip()

        if choice == "1":

            task_loading(
                "Running Email Intelligence..."
            )

            results = email_lookup(
                investigation[
                    "target"
                ]
            )

            if results:

                add_evidence(
                    investigation,
                    results
                )

                display_email_results(
                    results
                )
                add_timeline_event(
                    investigation,
                    "Email Intelligence Executed"
                )

            input(
                "\nPress Enter to continue..."
            )

        elif choice == "20":

            console.print(
                "\n1. ACTIVE"
            )

            console.print(
                "2. ON HOLD"
            )

            console.print(
                "3. CLOSED"
            )

            status = input(
                "\nChoice: "
            ).strip()

            mapping = {

                "1": "ACTIVE",
                "2": "ON HOLD",
                "3": "CLOSED"
            }

            investigation[
                "status"
            ] = mapping.get(
                status,
                "ACTIVE"
            )

            add_timeline_event(
                investigation,
                f"Case status changed to {investigation['status']}"
            )

            console.print(
                f"\n[green]Status Updated:[/green] {investigation['status']}"
            )

            input(
                "\nPress Enter to continue..."
            )

        elif choice == "2":

            note = input(
                "\nEnter Note: "
            )

            add_note(
                investigation,
                note
            )

            console.print(
                "\n[green]Note Added[/green]"
            )

            input(
                "\nPress Enter to continue..."
            )

        elif choice == "3":

            console.print(
                "\n[bright_cyan]Notes[/bright_cyan]\n"
            )

            if not investigation["notes"]:

                console.print(
                    "[yellow]No notes found[/yellow]"
                )

            else:

                for index, note in enumerate(
                    investigation["notes"],
                    start=1
                ):

                    console.print(
                        f"{index}. {note}"
                    )

            input(
                "\nPress Enter to continue..."
            )

        elif choice == "4":

            view_evidence(
                investigation
            )

            input(
                "\nPress Enter to continue..."
            )

        elif choice == "18":

            show_summary(
                investigation
            )

            input(
                "\nPress Enter to continue..."
            )

        elif choice == "19":

            show_timeline(
                investigation
            )

            input(
                "\nPress Enter to continue..."
            )

        elif choice == "5":

            task_loading(
                "Saving Investigation..."
            )

            filename = save_investigation(
                investigation
            )

            console.print(
                f"\n[green]Saved:[/green] "
                f"{filename}"
            )

            input(
                "\nPress Enter to continue..."
            )

        elif choice == "6":

            task_loading(
                "Generating Report..."
            )

            filename = generate_pdf_report(
                investigation
            )

            console.print(
                f"\n[green]Report Generated:[/green] "
                f"{filename}"
            )

            input(
                "\nPress Enter to continue..."
            )

        elif choice == "7":

            break

        elif choice == "8":

            console.print(
                "\nPaste Email Headers"
            )

            console.print(
                "Press Enter twice when finished\n"
            )

            lines = []

            while True:

                line = input()

                if line == "":
                    break

                lines.append(
                    line
                )

            headers = "\n".join(
                lines
            )

            task_loading(
                "Analyzing Headers..."
            )

            results = analyze_headers(
                headers
            )

            add_evidence(
                investigation,
                results
            )

            display_header_results(
                results
            )
            add_timeline_event(
                investigation,
                "Header Analysis Executed"
            )

            input(
                "\nPress Enter to continue..."
            )

        elif choice == "9":

            console.print(
                "\nPaste Text For IOC Extraction"
            )

            console.print(
                "Press Enter twice when finished\n"
            )

            lines = []

            while True:

                line = input()

                if line == "":
                    break

                lines.append(
                    line
                )

            text = "\n".join(
                lines
            )

            task_loading(
                "Extracting IOCs..."
            )

            results = extract_iocs(
                text
            )

            add_evidence(
                investigation,
                {
                    "Type": "IOC Extraction",
                    "Data": results
                }
            )

            display_iocs(
                results
            )
            add_timeline_event(
                investigation,
                "IOC Extraction Executed"
            )
            input(
                "\nPress Enter to continue..."
            )

        elif choice == "10":

            task_loading(
                "Analyzing Reputation..."
            )

            results = analyze_email_reputation(
                investigation[
                    "target"
                ]
            )

            add_evidence(
                investigation,
                {
                    "Type":
                    "Email Reputation",
                    "Data":
                    results
                }
            )

            display_email_reputation(
                results
            )
            add_timeline_event(
                investigation,
                "Email Reputation Executed"
            )
            input(
                "\nPress Enter to continue..."
            )

        elif choice == "11":

            domain = (
                investigation[
                    "target"
                ].split("@")[1]
            )

            task_loading(
                "Analyzing Domain..."
            )

            results = (
                domain_intelligence(
                    domain
                )
            )

            add_evidence(
                investigation,
                {
                    "Type":
                    "Domain Intelligence",

                    "Data":
                    results
                }
            )

            display_domain_intelligence(
                results
            )
            add_timeline_event(
                investigation,
                "Domain Intelligence Executed"
            )
            input(
                "\nPress Enter to continue..."
            )

        elif choice == "12":

            ip = input(
                "\nTarget IP: "
            ).strip()

            task_loading(
                "Running GeoIP Intelligence..."
            )

            results = geoip_lookup(
                ip
            )

            add_evidence(
                investigation,
                {
                    "Type":
                    "GeoIP Intelligence",

                    "Data":
                    results
                }
            )

            display_geoip_results(
                results
            )
            add_timeline_event(
                investigation,
                "GeoIP Intelligence Executed"
            )
            input(
                "\nPress Enter to continue..."
            )

        elif choice == "14":

            email = input(
                "\nTarget Email: "
            ).strip()

            task_loading(
                "Checking Breaches..."
            )

            results = breach_lookup(
                email
            )

            add_evidence(
                investigation,
                {
                    "Type":
                    "Breach Intelligence",

                    "Data":
                    results
                }
            )

            display_breach_results(
                results
            )

            add_timeline_event(
                investigation,
                "Breach Intelligence Executed"
            )

            input(
                "\nPress Enter to continue..."
            )

        elif choice == "15":

            username = input(
                "\nTarget Username: "
            ).strip()

            task_loading(
                "Running Username Intelligence..."
            )

            results = username_intelligence(
                username
            )

            add_evidence(
                investigation,
                {
                    "Type":
                    "Username Intelligence",

                    "Data":
                    results
                }
            )

            display_username_results(
                results
            )
            add_timeline_event(
                investigation,
                "Username Intelligence Executed"
            )
            input(
                "\nPress Enter to continue..."
            )

        elif choice == "16":

            url = input(
                "\nTarget URL: "
            ).strip()

            task_loading(
                "Running URL Intelligence..."
            )

            results = url_intelligence(
                url
            )

            add_evidence(
                investigation,
                {
                    "Type":
                    "URL Intelligence",

                    "Data":
                    results
                }
            )

            display_url_results(
                results
            )
            add_timeline_event(
                investigation,
                "URL Intelligence Executed"
            )

            input(
                "\nPress Enter to continue..."
            )

        elif choice == "17":

            hash_value = input(
                "\nTarget Hash: "
            ).strip()

            task_loading(
                "Running Hash Intelligence..."
            )

            results = hash_intelligence(
                hash_value
            )

            add_evidence(
                investigation,
                {
                    "Type":
                    "Hash Intelligence",

                    "Data":
                    results
                }
            )

            display_hash_results(
                results
            )

            add_timeline_event(
                investigation,
                "URL Intelligence Executed"
            )

            input(
                "\nPress Enter to continue..."
            )

        else:

            console.print(
                "\n[red]Invalid Option[/red]"
            )

            input(
                "\nPress Enter to continue..."
            )


def main():

    clear_screen()

    startup_loading()

    while True:

        clear_screen()

        show_banner()

        show_main_menu()

        choice = input(
            "\nMailTrace > "
        ).strip()

        if choice == "1":

            name = input(
                "\nInvestigation Name: "
            )

            target = input(
                "Target Email: "
            )

            investigation = (
                create_investigation(
                    name,
                    target
                )
            )

            investigation_loop(
                investigation
            )

        elif choice == "2":

            investigations = (
                list_investigations()
            )

            if not investigations:

                console.print(
                    "\n[red]No investigations found[/red]"
                )

                input(
                    "\nPress Enter to continue..."
                )

                continue

            console.print(
                "\n[bright_cyan]Available Investigations[/bright_cyan]\n"
            )

            for item in investigations:

                console.print(
                    f"- {item}"
                )

            name = input(
                "\nInvestigation Name: "
            )

            task_loading(
                "Loading Investigation..."
            )

            investigation = (
                load_investigation(
                    name
                )
            )

            if investigation:

                investigation_loop(
                    investigation
                )

            else:

                console.print(
                    "\n[red]Investigation Not Found[/red]"
                )

                input(
                    "\nPress Enter to continue..."
                )

        elif choice == "3":

            console.print(
                "\n[green]Thank you for using MailTrace.[/green]"
            )

            break

        else:

            console.print(
                "\n[red]Invalid Option[/red]"
            )

            input(
                "\nPress Enter to continue..."
            )


if __name__ == "__main__":
    main()