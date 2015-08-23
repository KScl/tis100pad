"""added descriptor to problem

Revision ID: 23857e9882c
Revises: 30f006270bf6
Create Date: 2015-08-16 15:21:19.940927

"""

# revision identifiers, used by Alembic.
revision = '23857e9882c'
down_revision = '30f006270bf6'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
 op.add_column('problem', sa.Column('descriptor', sa.Text))


def downgrade():
 op.drop_column('problem', 'descriptor')
