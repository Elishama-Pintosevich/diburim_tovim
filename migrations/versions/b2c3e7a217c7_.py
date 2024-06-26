"""empty message

Revision ID: b2c3e7a217c7
Revises: f78974e91b7e
Create Date: 2024-06-04 21:17:11.584003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2c3e7a217c7'
down_revision = 'f78974e91b7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('actions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('parameters', sa.String(length=500), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('actions', schema=None) as batch_op:
        batch_op.drop_column('parameters')

    # ### end Alembic commands ###
