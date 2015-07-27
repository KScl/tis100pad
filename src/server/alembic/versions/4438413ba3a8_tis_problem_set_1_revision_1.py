"""TIS problem set 1 revision 1

Revision ID: 4438413ba3a8
Revises: 47a716b5755e
Create Date: 2015-07-26 15:08:46.074536

"""

# revision identifiers, used by Alembic.
revision = '4438413ba3a8'
down_revision = '47a716b5755e'
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
 res = conn.execute(problemtable.select().where(problemtable.c.userId == -1))
 if len(res.fetchall()) == 0:
  op.bulk_insert(problemtable,[
{"userId":-1,'identifier':'00150',"a0" : 0, "a1":2, "a2" : 0, "a3":0, "a4":0, "a5" : 2, "a6" : 0, "a7" : 2, "a8":0, "a9":2, "a10":0, 'a11':0,"entry1":1,"entry2":0,"entry3":0,"entry4":1,"output1":1,"output2":0,"output3":0,"output4":1,"name":'Self-test diagnostic'},
{"userId":-1,'identifier':'10981',"a0" : 0, "a1":0, "a2" : 0, "a3":2, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":2, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":0,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Signal amplifier'},
{"userId":-1,'identifier':'20176',"a0" : 0, "a1":0, "a2" : 0, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 2, "a8":0, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":1,"entry4":0,"output1":0,"output2":1,"output3":1,"output4":0,"name":'Differential converter'},
{"userId":-1,'identifier':'21340',"a0" : 0, "a1":0, "a2" : 0, "a3":0, "a4":0, "a5" : 2, "a6" : 2, "a7" : 2, "a8":0, "a9":0, "a10":0, 'a11':0,"entry1":1,"entry2":0,"entry3":0,"entry4":0,"output1":0,"output2":1,"output3":1,"output4":1,"name":'Signal comparator'},
{"userId":-1,'identifier':'22280',"a0" : 0, "a1":0, "a2" : 0, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":2, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":1,"entry4":1,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Signal multiplexer'},
{"userId":-1,'identifier':'30647',"a0" : 0, "a1":0, "a2" : 0, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":2, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":1,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Sequence generator'},
{"userId":-1,'identifier':'31904',"a0" : 0, "a1":0, "a2" : 0, "a3":2, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":0,"entry4":0,"output1":0,"output2":1,"output3":1,"output4":0,"name":'Sequence counter'},
{"userId":-1,'identifier':'32050',"a0" : 0, "a1":0, "a2" : 0, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":2, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":0,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Signal edge detector'},
{"userId":-1,'identifier':'33762',"a0" : 0, "a1":0, "a2" : 0, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":2, "a9":0, "a10":0, 'a11':0,"entry1":1,"entry2":1,"entry3":1,"entry4":1,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Interrupt handler'},
{"userId":-1,'identifier':'40633',"a0" : 0, "a1":0, "a2" : 0, "a3":2, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":0,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Signal pattern detector'},
{"userId":-1,'identifier':'41427',"a0" : 0, "a1":0, "a2" : 0, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 2, "a8":0, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":0,"entry4":0,"output1":0,"output2":1,"output3":1,"output4":0,"name":'Sequence peak detector'},
{"userId":-1,'identifier':'42656',"a0" : 0, "a1":0, "a2" : 1, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":2, "a9":1, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":0,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Sequence reverser'},
{"userId":-1,'identifier':'43786',"a0" : 0, "a1":0, "a2" : 0, "a3":0, "a4":1, "a5" : 0, "a6" : 0, "a7" : 1, "a8":2, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":1,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Signal multiplier'},
{"userId":-1,'identifier':'50370',"a0" : 0, "a1":0, "a2" : 0, "a3":0, "a4":2, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":0,"entry3":0,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Image test pattern 1'},
{"userId":-1,'identifier':'51781',"a0" : 2, "a1":0, "a2" : 0, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":0,"entry3":0,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Image test pattern 2'},
{"userId":-1,'identifier':'52544',"a0" : 0, "a1":0, "a2" : 0, "a3":2, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":0,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Exposure mask viewer'},
{"userId":-1,'identifier':'53897',"a0" : 0, "a1":0, "a2" : 0, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":2, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":0,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Histogram viewer'},
{"userId":-1,'identifier':'60099',"a0" : 2, "a1":0, "a2" : 0, "a3":1, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":0, "a10":0, 'a11':1,"entry1":0,"entry2":1,"entry3":0,"entry4":0,"output1":0,"output2":1,"output3":1,"output4":0,"name":'Signal window filter'},
{"userId":-1,'identifier':'61212',"a0" : 0, "a1":0, "a2" : 0, "a3":0, "a4":1, "a5" : 0, "a6" : 0, "a7" : 1, "a8":0, "a9":0, "a10":0, 'a11':2,"entry1":0,"entry2":1,"entry3":1,"entry4":0,"output1":0,"output2":1,"output3":1,"output4":0,"name":'Signal divider'},
{"userId":-1,'identifier':'62711',"a0" : 0, "a1":1, "a2" : 0, "a3":2, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":1, "a10":0, 'a11':0,"entry1":1,"entry2":0,"entry3":1,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Sequence indexer'},
{"userId":-1,'identifier':'63534',"a0" : 2, "a1":0, "a2" : 1, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":1, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":0,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Sequence sorter'},
{"userId":-1,'identifier':'70601',"a0" : 0, "a1":0, "a2" : 0, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":1,"entry3":0,"entry4":0,"output1":0,"output2":0,"output3":1,"output4":0,"name":'Stored image decoder'},
{"userId":-1,'identifier':'UNKNOWN',"a0" : 0, "a1":0, "a2" : 0, "a3":2, "a4":0, "a5" : 0, "a6" : 0, "a7" : 2, "a8":2, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":0,"entry3":0,"entry4":0,"output1":0,"output2":0,"output3":0,"output4":0,"name":''},
{"userId":-1,'identifier':'USEG0',"a0" : 0, "a1":0, "a2" : 0, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":0,"entry3":0,"entry4":0,"output1":0,"output2":0,"output3":0,"output4":0,"name":'Simple sandbox'},
{"userId":-1,'identifier':'USEG1',"a0" : 0, "a1":0, "a2" : 1, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":1, "a10":0, 'a11':0,"entry1":0,"entry2":0,"entry3":0,"entry4":0,"output1":0,"output2":0,"output3":0,"output4":0,"name":'Stack memory sandbox'},
{"userId":-1,'identifier':'USEG2',"a0" : 0, "a1":0, "a2" : 0, "a3":0, "a4":0, "a5" : 0, "a6" : 0, "a7" : 0, "a8":0, "a9":0, "a10":0, 'a11':0,"entry1":0,"entry2":0,"entry3":0,"entry4":0,"output1":0,"output2":0,"output3":0,"output4":0,"name":'Image console sandbox'}])


def downgrade():
 print "skip"