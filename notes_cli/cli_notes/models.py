#!/usr/bin/env python3
import sqlalchemy

from abc import abstractmethod
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """
    This is the base class which keeps track of all
    tables and metadata relating to the database.
    """
    @abstractmethod
    def asdict(self) -> dict:
        """
        Return the table attributes as a dict.
        """
        pass


# ORM (object relational mapping) classes
# which represent database tables
class NotesList(Base):
    __tablename__ = "noteslist"
    note_id: Mapped[int] = mapped_column(sqlalchemy.SMALLINT(), autoincrement=True, nullable=False, primary_key=True)  # SMALLINTs are -32,768 to 32,767
    hash: Mapped[str] = mapped_column(sqlalchemy.VARCHAR(64), nullable=False)
    note: Mapped[str] = mapped_column(sqlalchemy.TEXT, nullable=False)  # TEXT is 65,535 characters (64KB)


    def asdict(self) -> dict:
        return {
            "hash": self.hash,
            "note_id": self.note_id,
            "note": self.note,
        }
