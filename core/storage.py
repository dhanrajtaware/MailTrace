import json
import os
from datetime import datetime


def create_investigation(name, target):

    return {
    "name": name,
    "target": target,
    "created": datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    ),
    "status": "ACTIVE",
    "notes": [],
    "evidence": [],
    "timeline": []
    }   


def save_investigation(investigation):

    os.makedirs(
        "investigations",
        exist_ok=True
    )

    filename = (
        f"investigations/"
        f"{investigation['name'].replace(' ', '_')}.json"
    )

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            investigation,
            file,
            indent=4,
            ensure_ascii=False
        )

    return filename


def load_investigation(name):

    filename = (
        f"investigations/"
        f"{name.replace(' ', '_')}.json"
    )

    if not os.path.exists(filename):
        return None

    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    if "status" not in data:
        data["status"] = "ACTIVE"

    if "timeline" not in data:
        data["timeline"] = []

    return data


def list_investigations():

    os.makedirs(
        "investigations",
        exist_ok=True
    )

    investigations = []

    for file in os.listdir(
        "investigations"
    ):

        if file.endswith(".json"):

            investigations.append(
                file.replace(
                    ".json",
                    ""
                )
            )

    return investigations


def add_note(
    investigation,
    note
):

    investigation[
        "notes"
    ].append(note)


def add_evidence(
    investigation,
    evidence
):

    if isinstance(
        evidence,
        dict
    ) and "Type" in evidence:

        investigation[
            "evidence"
        ].append(
            evidence
        )

    else:

        investigation[
            "evidence"
        ].append(
            {
                "Type": "Unknown",
                "Timestamp": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                "Data": evidence
            }
        )

def add_timeline_event(
    investigation,
    event
):

    if "timeline" not in investigation:

        investigation[
            "timeline"
        ] = []

    investigation[
        "timeline"
    ].append(
        {
            "time":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "event":
            event
        }
    )