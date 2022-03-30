"""add last_anomaly_timestamp in alert table

Revision ID: 0747323f8f25
Revises: 4c40273b1dea
Create Date: 2022-03-22 17:11:33.011210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0747323f8f25'
down_revision = '4c40273b1dea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('alert', sa.Column('last_anomaly_timestamp', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('alert', 'last_anomaly_timestamp')
    # ### end Alembic commands ###