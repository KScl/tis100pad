"""Solution scores

Revision ID: 22f65a18faec
Revises: 2b660667a788
Create Date: 2015-07-30 17:54:11.131441

"""

# revision identifiers, used by Alembic.
revision = '22f65a18faec'
down_revision = '2b660667a788'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

import re

solutionTable = sa.table("solution",
sa.Column("id",sa.Integer),
sa.Column("cycles",sa.Integer),
sa.Column("nodeCount",sa.Integer),
sa.Column("instructionCount",sa.Integer),
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

def instructionsCount(input):
 intstructions = 0
 lines = re.split("/\r\n|\r|\n/g",input)
 for line in lines:
  if(not (line.strip() == "" or line.strip()[:1] == "#")):
   intstructions+=1
 return intstructions

def nodeCount(input):
 return int(input.strip() != "")

def upgrade():
 conn = op.get_bind()
 op.add_column('solution',sa.Column("cycles",sa.Integer))
 op.add_column('solution',sa.Column("nodeCount",sa.Integer))
 op.add_column('solution',sa.Column("instructionCount",sa.Integer))
 res = conn.execute(solutionTable.select())
 print res
 for solution in res:
  instruction = 0
  nodes = 0
  nodes += nodeCount(solution.a0)
  instruction += instructionsCount(solution.a0)
  nodes += nodeCount(solution.a1)
  instruction += instructionsCount(solution.a1)
  nodes += nodeCount(solution.a2)
  instruction += instructionsCount(solution.a2)
  nodes += nodeCount(solution.a3)
  instruction += instructionsCount(solution.a3)
  nodes += nodeCount(solution.a4)
  instruction += instructionsCount(solution.a4)
  nodes += nodeCount(solution.a5)
  instruction += instructionsCount(solution.a5)
  nodes += nodeCount(solution.a6)
  instruction += instructionsCount(solution.a6)
  nodes += nodeCount(solution.a7)
  instruction += instructionsCount(solution.a7)
  nodes += nodeCount(solution.a8)
  instruction += instructionsCount(solution.a8)
  nodes += nodeCount(solution.a9)
  instruction += instructionsCount(solution.a9)
  nodes += nodeCount(solution.a10)
  instruction += instructionsCount(solution.a10)
  nodes += nodeCount(solution.a11)
  instruction += instructionsCount(solution.a11)

  conn.execute( solutionTable.update().where(solutionTable.c.id == solution.id).values(cycles = -1, nodeCount = nodes, instructionCount= instruction ))




def downgrade():
 op.drop_column('solution',"cycles")
 op.drop_column('solution',"nodeCount")
 op.drop_column('solution',"instructionCount")
