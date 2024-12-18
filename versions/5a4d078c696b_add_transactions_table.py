"""add transactions table

Revision ID: 5a4d078c696b
Revises: 387475aafab5
Create Date: 2024-11-22 00:32:38.654957

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "5a4d078c696b"
down_revision: Union[str, None] = "387475aafab5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "transactions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("bank_id", sa.Integer(), nullable=False),
        sa.Column(
            "type", sa.Enum("INCOME", "EXPENSE", name="transactiontype"), nullable=False
        ),
        sa.Column("amount", sa.Float(), nullable=False),
        sa.Column(
            "date", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("description", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["bank_id"],
            ["banks.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_transactions_id"), "transactions", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_transactions_id"), table_name="transactions")
    op.drop_table("transactions")
    # ### end Alembic commands ###
