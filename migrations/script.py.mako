"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision: str = ${repr(up_revision)}
down_revision: Union[str, None] = ${repr(down_revision)}
branch_labels: Union[str, Sequence[str], None] = ${repr(branch_labels)}
depends_on: Union[str, Sequence[str], None] = ${repr(depends_on)}


def upgrade() -> None:
    op.execute("create schema if not exist chat")
    op.execute("create schema if not exist user")
    op.execute("create schema if not exist team")
    op.execute("create schema if not exist settings")
    op.execute("create schema if not exist response")
    op.execute("create schema if not exist skill")
    op.execute("create schema if not exist subscription")

    ${upgrades if upgrades else "pass"}


def downgrade() -> None:

    ${downgrades if downgrades else "pass"}

    op.execute("drop schema if exist chat cascade")
    op.execute("drop schema if exist user cascade")
    op.execute("drop schema if exist team cascade")
    op.execute("drop schema if exist settings cascade")
    op.execute("drop schema if exist response cascade")
    op.execute("drop schema if exist skill cascade")
    op.execute("drop schema if exist subscription cascade")
