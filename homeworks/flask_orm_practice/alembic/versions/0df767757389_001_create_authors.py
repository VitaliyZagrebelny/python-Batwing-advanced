"""001_create_authors

Revision ID: 0df767757389
Revises: 
Create Date: 2022-07-27 16:37:55.264482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001_create_authors'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "authors",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name_lastname", sa.String(255), nullable=False, unique=True))


def downgrade() -> None:
    op.drop_table('authors')