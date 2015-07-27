"""create problem table

Revision ID: 47a716b5755e
Revises: c24235851ad
Create Date: 2015-07-26 14:31:46.108364

"""

# revision identifiers, used by Alembic.
revision = '47a716b5755e'
down_revision = 'c24235851ad'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
 op.create_table('problem',
sa.Column("id",sa.Integer, primary_key=True),
sa.Column("identifier",sa.Text),
sa.Column("userId",sa.Integer),
sa.Column("name",sa.Text),
sa.Column("script",sa.Text),
sa.Column("entry1",sa.Text),
sa.Column("entry2",sa.Text),
sa.Column("entry3",sa.Text),
sa.Column("entry4",sa.Text),
sa.Column("output1",sa.Text),
sa.Column("output2",sa.Text),
sa.Column("output3",sa.Text),
sa.Column("output4",sa.Text),
sa.Column("a0",sa.Integer),
sa.Column("a1",sa.Integer),
sa.Column("a2",sa.Integer),
sa.Column("a3",sa.Integer),
sa.Column("a4",sa.Integer),
sa.Column("a5",sa.Integer),
sa.Column("a6",sa.Integer),
sa.Column("a7",sa.Integer),
sa.Column("a8",sa.Integer),
sa.Column("a9",sa.Integer),
sa.Column("a10",sa.Integer),
sa.Column("a11",sa.Integer))


def downgrade():
 op.drop_table('problem')
