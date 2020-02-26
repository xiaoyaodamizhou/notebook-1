"""add language

Revision ID: 4c894ead3fec
Revises: c47b6dbd5e2e
Create Date: 2018-12-28 15:27:17.722053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c894ead3fec'
down_revision = 'c47b6dbd5e2e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'language')
    # ### end Alembic commands ###
