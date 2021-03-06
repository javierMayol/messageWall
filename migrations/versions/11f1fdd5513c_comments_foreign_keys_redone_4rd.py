"""Comments foreign keys, redone 4rd

Revision ID: 11f1fdd5513c
Revises: 21082fc3bf2b
Create Date: 2020-02-10 20:00:59.302194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11f1fdd5513c'
down_revision = '21082fc3bf2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comment', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_column('comment', 'user_id')
    # ### end Alembic commands ###
