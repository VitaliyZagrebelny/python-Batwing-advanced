"""002_create_books

Revision ID: bf1038bd7dff
Revises: 0df767757389
Create Date: 2022-07-27 16:38:54.197789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002_create_books'
down_revision = '001_create_authors'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "books",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("title", sa.String(255), nullable=False, unique=True))


def downgrade() -> None:
    op.drop_table('books')