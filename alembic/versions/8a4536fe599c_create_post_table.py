"""create post table

Revision ID: 8a4536fe599c
Revises: 
Create Date: 2026-06-15 17:01:00.277223

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8a4536fe599c'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True)
                    ,sa.Column('title',sa.String(),nullable=False))
    
    


def downgrade() -> None:
    op.drop_table('posts')
    pass
