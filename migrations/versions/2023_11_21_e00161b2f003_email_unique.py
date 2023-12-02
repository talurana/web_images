"""email unique

Revision ID: e00161b2f003
Revises: 54912fe9b6b4
Create Date: 2023-11-21 21:41:58.755755

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e00161b2f003'
down_revision: Union[str, None] = '54912fe9b6b4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_image_user_id', 'image', type_='foreignkey')
    op.drop_column('image', 'edited_by')
    op.create_unique_constraint(None, 'user', ['email'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.add_column('image', sa.Column('edited_by', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('fk_image_user_id', 'image', 'user', ['edited_by'], ['id'])
    # ### end Alembic commands ###
