"""create solution table

Revision ID: c24235851ad
Revises: 
Create Date: 2015-07-26 13:03:33.279222

"""

# revision identifiers, used by Alembic.
revision = 'c24235851ad'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
 op.create_table('solution',
  sa.Column("id",sa.Integer, primary_key=True),
  sa.Column("problemId",sa.Text),
  sa.Column("userId",sa.Integer),
  sa.Column("date",sa.Date),
  sa.Column("a0",sa.Text),
  sa.Column("a1",sa.Text),
  sa.Column("a2",sa.Text),
  sa.Column("a3",sa.Text),
  sa.Column("a4",sa.Text),
  sa.Column("a5",sa.Text),
  sa.Column("a6",sa.Text),
  sa.Column("a7",sa.Text),
  sa.Column("a8",sa.Text),
  sa.Column("a9",sa.Text),
  sa.Column("a10",sa.Text),
  sa.Column("a11",sa.Text))


def downgrade():
 op.drop_table('solution')
