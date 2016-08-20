"""Chapter11f

Revision ID: 0ab9c335e1d0
Revises: 11bf5be60325
Create Date: 2016-08-19 16:19:19.587670

"""

# revision identifiers, used by Alembic.
revision = '0ab9c335e1d0'
down_revision = '11bf5be60325'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    ### end Alembic commands ###