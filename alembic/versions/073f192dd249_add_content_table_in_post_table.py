"""add content table in post table

Revision ID: 073f192dd249
Revises: 8a4536fe599c
Create Date: 2026-06-15 17:10:16.484470

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '073f192dd249'
down_revision: Union[str, Sequence[str], None] = '8a4536fe599c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('content',sa.String,nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','content')
    pass
