"""002_create_ev_talb

Revision ID: 002_create_ev_talb
Revises: 001_create_user_table
Create Date: 2022-08-08 13:35:59.782430

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy.orm import load_only

revision = '002_create_ev_tabl'
down_revision = '001_create_user_table'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'event',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=300), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('starts_at', sa.DateTime(), nullable=False),
        sa.Column('ends_at', sa.DateTime(), nullable=False),
        sa.Column('creator_id', sa.Integer(), nullable=False),
    )



def downgrade() -> None:
    op.drop_table('event')