"""added TIS-NET tables

Revision ID: 7e404593db7
Revises: 23857e9882c
Create Date: 2016-01-17 08:49:33.408432

"""

# revision identifiers, used by Alembic.
revision = '7e404593db7'
down_revision = '23857e9882c'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

problemtable = sa.table("problem",
sa.Column("id",sa.Integer),
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


def upgrade():
 conn = op.get_bind()
 res = conn.execute(problemtable.select().where(problemtable.c.identifier == 'NEXUS 00.526.6'))
 if len(res.fetchall()) == 0:
  op.bulk_insert(problemtable,[
{"userId":-1,'identifier':'NEXUS.00.526.6',"a0" : 0, "a1":0, "a2" : 2, "a3":0, "a4":1, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":0, "a10":0, 'a11':1,"entry1":0,"entry2":1,"entry3":0,"entry4":1,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Sequence merger'},
{"userId":-1,'identifier':'NEXUS.01.874.8',"a0" : 0, "a1":0, "a2" : 0, "a3":2, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":0, "a10":0, 'a11':2,"entry1":0,"entry2":1,"entry3":0,"entry4":0,"output1":0,"output2":1,"output3":0,"output4":0,"name":'Integer series calculator'},
{"userId":-1,'identifier':'NEXUS.02.981.2',"a0" : 0, "a1":0, "a2" : 0, "a3":2, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":0, "a10":0, 'a11':0,"entry1":1,"entry2":1,"entry3":1,"entry4":0,"output1":0,"output2":1,"output3":0,"output4":0,"name":'Sequence range limiter'},
{"userId":-1,'identifier':'NEXUS.03.176.9',"a0" : 2, "a1":0, "a2" : 0, "a3":2, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":1,"entry4":0,"output1":0,"output2":1,"output3":1,"output4":1,"name":'Signal error corrector'},
{"userId":-1,'identifier':'NEXUS.04.340.5',"a0" : 0, "a1":0, "a2" : 0, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":2, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":1,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Subsequence extractor'},
{"userId":-1,'identifier':'NEXUS.05.647.1',"a0" : 0, "a1":2, "a2" : 2, "a3":2, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":0, "a10":0, 'a11':0,"entry1":1,"entry2":0,"entry3":0,"entry4":0,"output1":0,"output2":1,"output3":1,"output4":1,"name":'Signal prescaler'},
{"userId":-1,'identifier':'NEXUS.06.786.0',"a0" : 0, "a1":0, "a2" : 0, "a3":0, "a4":2, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":1,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Signal averager'},
{"userId":-1,'identifier':'NEXUS.07.050.0',"a0" : 0, "a1":0, "a2" : 0, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":2, "a9":0, "a10":0, 'a11':0,"entry1":1,"entry2":1,"entry3":1,"entry4":1,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Submaximum selector'},
{"userId":-1,'identifier':'NEXUS.08.633.9',"a0" : 0, "a1":0, "a2" : 0, "a3":2, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":0,"entry4":0,"output1":1,"output2":1,"output3":1,"output4":0,"name":'Decimal decomposer'},
{"userId":-1,'identifier':'NEXUS.09.904.9',"a0" : 1, "a1":0, "a2" : 1, "a3":2, "a4":0, "a5" : 0, "a6" : 0, "a7" : 2, "a8":0, "a9":0, "a10":0, 'a11':2,"entry1":0,"entry2":1,"entry3":0,"entry4":0,"output1":0,"output2":1,"output3":0,"output4":0,"name":'Sequence mode calculator'},
{"userId":-1,'identifier':'NEXUS.10.656.5',"a0" : 0, "a1":0, "a2" : 1, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 1, "a8":0, "a9":2, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":0,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Sequence normalizer'},
{"userId":-1,'identifier':'NEXUS.11.711.2',"a0" : 2, "a1":0, "a2" : 0, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":0,"entry3":0,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Image test pattern 3'},
{"userId":-1,'identifier':'NEXUS.12.534.4',"a0" : 2, "a1":0, "a2" : 0, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":0,"entry3":0,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Image test pattern 4'},
{"userId":-1,'identifier':'NEXUS.13.370.9',"a0" : 2, "a1":0, "a2" : 0, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":0,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Spatial path viewer'},
{"userId":-1,'identifier':'NEXUS.14.781.3',"a0" : 1, "a1":0, "a2" : 0, "a3":2, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":1, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":0,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Character terminal'},
{"userId":-1,'identifier':'NEXUS.15.897.9',"a0" : 0, "a1":0, "a2" : 0, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":2, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":1,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Back-reference reifier'},
{"userId":-1,'identifier':'NEXUS.16.212.8',"a0" : 0, "a1":0, "a2" : 0, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":0, "a10":0, 'a11':2,"entry1":1,"entry2":0,"entry3":1,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Dynamic pattern detector'},
{"userId":-1,'identifier':'NEXUS.17.135.0',"a0" : 2, "a1":0, "a2" : 0, "a3":0, "a4":2, "a5" : 1, "a6" : 0, "a7" : 1, "a8":2, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":0,"entry3":1,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Sequence gap interpolator'},
{"userId":-1,'identifier':'NEXUS.18.427.7',"a0" : 0, "a1":0, "a2" : 0, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":2, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":0,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Decimal to octal converter'},
{"userId":-1,'identifier':'NEXUS.19.762.9',"a0" : 2, "a1":1, "a2" : 0, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":1, "a10":0, 'a11':0,"entry1":0,"entry2":0,"entry3":1,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Prolonged sequence sorter'},
{"userId":-1,'identifier':'NEXUS.20.433.1',"a0" : 0, "a1":0, "a2" : 0, "a3":0, "a4":2, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":0,"entry4":0,"output1":0,"output2":1,"output3":0,"output4":0,"name":'Prime factor calculator'},
{"userId":-1,'identifier':'NEXUS.21.601.6',"a0" : 0, "a1":0, "a2" : 0, "a3":0, "a4":1, "a5" : 0, "a6" : 0, "a7" : 1, "a8":2, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":1,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Sigmal exponentiator'},
{"userId":-1,'identifier':'NEXUS.22.280.8',"a0" : 0, "a1":0, "a2" : 0, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":0, "a10":0, 'a11':2,"entry1":0,"entry2":1,"entry3":1,"entry4":0,"output1":0,"output2":1,"output3":0,"output4":0,"name":'T20 node emulator'},
{"userId":-1,'identifier':'NEXUS.23.727.9',"a0" : 2, "a1":1, "a2" : 0, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":1, "a10":0, 'a11':0,"entry1":0,"entry2":0,"entry3":1,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'T31 node emulator'},
{"userId":-1,'identifier':'NEXUS.24.511.7',"a0" : 0, "a1":0, "a2" : 0, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":0, "a10":0, 'a11':0,"entry1":1,"entry2":1,"entry3":1,"entry4":1,"output1":0,"output2":1,"output3":0,"output4":0,"name":'Wave collapse supervisor'}])



def downgrade():
	print "this process is not reversible"
