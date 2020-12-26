"""empty message

Revision ID: 7306e9d31301
Revises: a25157cdebae
Create Date: 2020-12-26 16:41:27.172239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7306e9d31301'
down_revision = 'a25157cdebae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('website_link', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'website_link')
    # ### end Alembic commands ###