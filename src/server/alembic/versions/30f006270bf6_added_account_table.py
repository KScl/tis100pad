"""added account table

Revision ID: 30f006270bf6
Revises: 22f65a18faec
Create Date: 2015-08-01 13:24:41.402614

"""

# revision identifiers, used by Alembic.
revision = '30f006270bf6'
down_revision = '22f65a18faec'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
 op.create_table('account',
  sa.Column("id",sa.Integer, primary_key=True),
  sa.Column("name",sa.String(80)),
  sa.Column("password",sa.String(120)))


def downgrade():
 op.drop_table('account')
