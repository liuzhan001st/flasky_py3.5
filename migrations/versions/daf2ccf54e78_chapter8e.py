"""Chapter8e

Revision ID: daf2ccf54e78
Revises: 5efd8f906a05
Create Date: 2016-08-04 20:46:42.454402

"""

# revision identifiers, used by Alembic.
revision = 'daf2ccf54e78'
down_revision = '5efd8f906a05'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    ### end Alembic commands ###
