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
sa.Column("Cycles",sa.Text),
sa.Column("NodeCount",sa.Integer),
sa.Column("InstructionCount",sa.Text),
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

def lines(input):
 intstructions = 0
 lines = re.split("/\r\n|\r|\n/g",input)
 for line in lines:
  if(not (line.trim() == "" or line.trim().substring(0,1) == "#")):
   intstructions+=1
 return intstructions

def upgrade():
 op.add_column('solution',sa.Column("cycles",sa.Text))
 op.add_column('solution',sa.Column("nodeCount",sa.Text))
 op.add_column('solution',sa.Column("instructionCount",sa.Text))
 conn = op.get_bind();
 res = conn.execute(solutionTable.select())
 print res
 for solution in res:
  instruction = 0
  instruction += lines(solution.a0)
  instruction += lines(solution.a1)
  instruction += lines(solution.a2)
  instruction += lines(solution.a3)
  instruction += lines(solution.a4)
  instruction += lines(solution.a5)
  instruction += lines(solution.a6)
  instruction += lines(solution.a7)
  instruction += lines(solution.a8)
  instruction += lines(solution.a9)
  instruction += lines(solution.a10)
  instruction += lines(solution.a11)
  print instruction




def downgrade():
 op.drop_column('solution',"cycles")
 op.drop_column('solution',"nodeCount")
 op.drop_column('solution',"instructionCount")
