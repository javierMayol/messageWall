"""Comment route13

Revision ID: 68d358f955cd
Revises: 8fccc16ea32a
Create Date: 2020-02-11 04:47:55.558731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68d358f955cd'
down_revision = '8fccc16ea32a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('post_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comment', 'post', ['post_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_column('comment', 'post_id')
    # ### end Alembic commands ###
