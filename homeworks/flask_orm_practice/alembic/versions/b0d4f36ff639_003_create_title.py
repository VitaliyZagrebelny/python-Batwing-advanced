"""003_create_title

Revision ID: b0d4f36ff639
Revises: 002_create_books
Create Date: 2022-07-27 16:40:19.771801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '003_create_title'
down_revision = '002_create_books'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "author_title",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("author", sa.String, nullable=False),
        sa.Column("title", sa.String, nullable=False))


def downgrade() -> None:
    op.drop_table('author_title')