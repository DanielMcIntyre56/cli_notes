#!/usr/bin/env python3

import sys
import argparse

from datetime import datetime

from cli_notes import database as _db


def get_args():
    """
    Parse input arguments.
    """
    parser = argparse.ArgumentParser(description="Arguments for notes CLI tool.")
    action_group = parser.add_mutually_exclusive_group(required=True)
    action_group.add_argument("-a", "--add", dest="add", default="", help="Add a new note.")
    action_group.add_argument("-l", "--list", dest="list", action='store_true', help="List stored notes.")
    action_group.add_argument("-r", "--replace", dest="replace", default="", help="Replace an existing note.")
    action_group.add_argument("-d", "--delete", dest="delete", action='store_true', help="Delete a note.")
    action_group.add_argument("-c", "--clear", dest="clear", action='store_true', help="Clear all existing notes.")
    action_group.add_argument("-ap", "--append", dest="append", default="", help="Append to an existing note.")

    parser.add_argument("-id", "--note-id", dest="note_id", default=0, help="ID of the note.")
    parser.add_argument("-hash", "--show-hash", dest="show_hash", action='store_true', help="Show the note hashes.")

    (known, unknown) = parser.parse_known_args()
    return (known, unknown)


def fail(err: str, rc: int=1):
    """
    Print timestamped failure message
    with RC and exit program.
    """
    print(f"{datetime.now()} - Error: {err}. RC: {rc}.")
    sys.exit(rc)


def main():
    """
    Notes CLI script entry point.
    """
    MYSQL = _db.MySQL()

    known, unknown = get_args()

    if unknown:
        fail(f"unknown args {unknown}")
        return

    if known.list:
        MYSQL.list_notes(show_hash=known.show_hash)

    elif known.clear:
        MYSQL.clear_all_notes()

    elif known.delete:
        if not known.note_id:
            fail("-id is required to delete a note.")

        MYSQL.delete_note(known.note_id)

    elif known.add:
        MYSQL.add_note(known.add)

    elif known.replace:
        if not known.note_id:
            fail("-id is required to replace a note.")

        MYSQL.replace_note(known.note_id, known.replace)

    elif known.append:
        if not known.note_id:
            fail("-id is required to append to a note.")

        MYSQL.append_to_note(known.note_id, known.append)

    MYSQL.write_notes_to_txt()

if __name__ == "__main__":
    main()
