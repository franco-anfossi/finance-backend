"""Add foreign key to banks

Revision ID: 387475aafab5
Revises: b4349d81faf6
Create Date: 2024-11-21 18:18:21.070838

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "387475aafab5"
down_revision: Union[str, None] = "b4349d81faf6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(
        None, "banks", "users", ["user_id"], ["id"], ondelete="CASCADE"
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "banks", type_="foreignkey")
    # ### end Alembic commands ###