import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from cli_notes import config as _config
from cli_notes import models as _models
from cli_notes import utils as _utils


sql_engine = create_engine(f"mysql+pymysql://{_config.MYSQL_USER}@{_config.MYSQL_HOST}/{_config.NOTES_DB_NAME}")


class MySQL:
    """
    A database management class used for
    interacting with the noteslist MySQL table.
    """
    def __init__(self) -> None:
        self.mysql_session = sessionmaker(sql_engine)


    def add_note(self, note: str) -> None:
        """
        Add a note string to the DB.
        """
        note_hash = _utils.hash_string(note)

        new_note = _models.NotesList(
            hash=note_hash,
            note=note,
        )

        with self.mysql_session() as session, session.begin():
            session.add(new_note)
            session.commit()

        print(f"Successfully added note.")


    def list_notes(self, show_hash=False) -> None:
        """
        List all current notes.
        """
        with self.mysql_session() as session, session.begin():
            query = sa.select(_models.NotesList)

        notes = session.execute(query).scalars()

        if show_hash:
            print(f"Note ID{_config.SMALL_SPACE} Hash {_config.HASH_SPACE}  Note")
            print(_config.DIVIDER)
        else:
            print(f"Note ID {_config.SMALL_SPACE} Note")
            print(_config.DIVIDER)

        for note in notes:
            note_dict = note.asdict()
            if show_hash:
                print(f"{_config.SMALL_SPACE}{note_dict['note_id']}{_config.LARGE_SPACE}{note_dict['hash']}{_config.LARGE_SPACE}{note_dict['note']}")
            else:
                print(f"{_config.SMALL_SPACE}{note_dict['note_id']}{_config.LARGE_SPACE} {note_dict['note']}")


    def replace_note(self, note_id: int, new_note: str):
        """
        Replace a note string for a note identified by its note_id.
        """
        with self.mysql_session() as session, session.begin():
            if not self._note_exists(note_id, session):
                print(f"Note with ID '{note_id}' not found.")
                return

            query = sa.update(_models.NotesList).where(_models.NotesList.note_id == note_id).values(note=new_note)
            session.execute(query)
            session.commit()


    def delete_note(self, note_id: int) -> None:
        """
        Delete a note by its note_id.
        """
        with self.mysql_session() as session, session.begin():
            if not self._note_exists(note_id, session):
                print(f"Note with ID '{note_id}' not found.")
                return

            query = sa.delete(_models.NotesList).where(_models.NotesList.note_id == note_id)
            session.execute(query)
            session.commit()


    def clear_all_notes(self) -> None:
        """
        Clear all existing notes and reset the note_id count.
        """
        with self.mysql_session() as session, session.begin():
            query = sa.delete(_models.NotesList)
            session.execute(query)
            session.execute(sa.text(f"ALTER TABLE {_models.NotesList.__tablename__} AUTO_INCREMENT = 1"))
            session.commit()


    def append_to_note(self, note_id: int, str_to_append: str) -> None:
        """
        Append a new string to the end of an existing note.
        """
        with self.mysql_session() as session, session.begin():
            if not self._note_exists(note_id, session):
                print(f"Note with ID '{note_id}' not found.")
                return

            query = sa.select(_models.NotesList).where(_models.NotesList.note_id == note_id)
            note_result = session.execute(query).scalars()
            note_str = note_result.first().asdict()['note']

            new_note = note_str + str_to_append
            query = sa.update(_models.NotesList).where(_models.NotesList.note_id == note_id).values(note=new_note)
            session.execute(query)
            session.commit()


    def _note_exists(self, note_id: int, session) -> bool:
        """
        Returns True if a note with a given note_id exists, False otherwise.
        """
        query = sa.select(_models.NotesList).where(_models.NotesList.note_id == note_id)
        note = session.execute(query).scalars()

        if note.first():
            return True

        return False


    def write_notes_to_txt(self) -> None:
        """
        Write notes to a .txt file.
        """
        with self.mysql_session() as session, session.begin():
            query = sa.select(_models.NotesList)

        notes = session.execute(query).scalars()

        with open(_config.NOTES_TXT_FILE, 'w+') as f:
            f.truncate(0)
            f.write("\n")

            for note in notes:
                note_dict = note.asdict()

                f.write(f"{note_dict['note_id']} {note_dict['note']}\n")
