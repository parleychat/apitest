"""added login functionality to access api

Revision ID: 8369b3c92775
Revises: 3aa01ecc04c5
Create Date: 2019-06-28 17:48:42.263565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8369b3c92775'
down_revision = '3aa01ecc04c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('hash_password', sa.String(length=256), nullable=True),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('dev_id', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_dev_id'), 'users', ['dev_id'], unique=True)
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_index(op.f('ix_users_dev_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
