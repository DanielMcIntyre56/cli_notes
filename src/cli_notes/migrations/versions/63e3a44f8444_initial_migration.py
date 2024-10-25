"""
Initial migration

Revision ID: 63e3a44f8444
Revises: 
Create Date: 2024-12-08 21:13:51.808968

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# Revision identifiers, used by Alembic.
revision: str = '63e3a44f8444'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'noteslist',
        sa.Column('note_id', sa.SMALLINT(), autoincrement=True, nullable=False, primary_key=True),
        sa.Column('hash', sa.VARCHAR(length=64), nullable=False, unique=True),
        sa.Column('note', sa.TEXT(), nullable=False),
        sa.PrimaryKeyConstraint('note_id'),
    )


def downgrade() -> None:
    op.drop_table('noteslist')
