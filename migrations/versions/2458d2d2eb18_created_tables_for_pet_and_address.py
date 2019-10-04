"""created tables for pet and address

Revision ID: 2458d2d2eb18
Revises: 3bea12a6af07
Create Date: 2019-10-04 00:31:37.343566

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2458d2d2eb18'
down_revision = '3bea12a6af07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('addr_1', sa.String(length=64), nullable=True),
    sa.Column('addr_2', sa.String(length=64), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('state', sa.String(length=64), nullable=True),
    sa.Column('zip_code', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pet',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('pet_type', sa.String(length=64), nullable=True),
    sa.Column('breed', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=64), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pet')
    op.drop_table('address')
    # ### end Alembic commands ###