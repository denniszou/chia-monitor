"""Add pool_state_events table

Revision ID: 7d540ed3aa62
Revises: 30957ecc3bb4
Create Date: 2021-07-11 19:07:10.596477

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '7d540ed3aa62'
down_revision = '30957ecc3bb4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pool_state_events',
    sa.Column('ts', sa.DateTime(), nullable=False),
    sa.Column('current_points', sa.Integer(), nullable=True),
    sa.Column('current_difficulty', sa.Integer(), nullable=True),
    sa.Column('points_found_since_start', sa.Integer(), nullable=True),
    sa.Column('points_acknowledged_since_start', sa.Integer(), nullable=True),
    sa.Column('num_pool_errors_24h', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('ts')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pool_state_events')
    # ### end Alembic commands ###