"""004_add_inv_st

Revision ID: 004_add_inv_st
Revises: 003_create_us_ev_tabl
Create Date: 2022-08-08 13:43:20.118515

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '004_add_inv_st'
down_revision = '003_create_us_ev_tabl'
branch_labels = None
depends_on = None


def upgrade() -> None:
    inv_status = postgresql.ENUM('accepted', 'declined', 'pending', name='inv_status')
    inv_status.create(op.get_bind())

    op.add_column('user_event', sa.Column('invitation_status', sa.Enum('accepted',
                                                                       'declined',
                                                                       'pending',
                                                                       name='inv_status'),
                                                                       nullable=True))


def downgrade() -> None:
    op.drop_column('user_event', 'invitation_status')
