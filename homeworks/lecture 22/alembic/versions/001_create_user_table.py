"""001_cre1. add field creator_id to event table
2. add invitation_status to user_event table. Invitation Status: Enum(accepted, declined, pending)
3. create API for accepting or declining invitations
4. add rule that invitations could be sent only by creator
5. Add edit&delete API for events. Endpoints could be triggered only by creator
ate_user_table

Revision ID: 001_create_user_table
Revises: 
Create Date: 2022-07-15 19:24:17.794464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001_create_user_table'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("email", sa.String(350), unique=True, nullable=False),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("password", sa.String, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("user")
