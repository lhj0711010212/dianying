"""empty message

Revision ID: 435543b0e1df
Revises: None
Create Date: 2013-12-10 00:46:03.204270

"""

# revision identifiers, used by Alembic.
revision = '435543b0e1df'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('greetings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('src_user_id', sa.Integer(), nullable=True),
    sa.Column('dst_user_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['dst_user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['src_user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('greetings')
    ### end Alembic commands ###
