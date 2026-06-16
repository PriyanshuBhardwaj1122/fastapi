"""add last few col to posts

Revision ID: cf1ce8e7fb9a
Revises: 35c9d3ef7896
Create Date: 2026-06-15 17:29:03.864623

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cf1ce8e7fb9a'
down_revision: Union[str, Sequence[str], None] = '35c9d3ef7896'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('published',sa.Boolean(),nullable=False,server_default='True'),)
    op.add_column('posts',sa.Column(
        'created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')
    ))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','pubished')
    op.drop_column('posts','created_at')
    pass
