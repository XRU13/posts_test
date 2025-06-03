"""create posts table

Revision ID: d8be39e4230d
Revises: 
Create Date: 2025-06-03 11:18:26.591898

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'd8be39e4230d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('posts')
