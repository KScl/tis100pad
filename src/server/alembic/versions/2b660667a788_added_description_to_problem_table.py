"""added description to problem table

Revision ID: 2b660667a788
Revises: 4438413ba3a8
Create Date: 2015-07-30 17:14:10.246096

"""

# revision identifiers, used by Alembic.
revision = '2b660667a788'
down_revision = '4438413ba3a8'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
 op.add_column('problem',sa.Column("description",sa.Text))


def downgrade():
 op.drop_column('problem',"description")

