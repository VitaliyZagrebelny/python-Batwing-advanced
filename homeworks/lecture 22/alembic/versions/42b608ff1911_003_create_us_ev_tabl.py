"""003_create_us_ev_tabl

Revision ID: 003_create_us_ev_tabl
Revises: 002_create_ev_tabl
Create Date: 2022-08-08 13:38:56.857290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '003_create_us_ev_tabl'
down_revision = '002_create_ev_tabl'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'user_event',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('user.id'), nullable=False),
        sa.Column('event_id', sa.Integer(), sa.ForeignKey('event.id'), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('user_event')