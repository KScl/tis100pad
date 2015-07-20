from app.model.problem import Problem
from app import db

E = Problem.EXEC
S = Problem.STCK
ER = Problem.ERR


LEVELS = {
    '00150':   {"Nodes":[E, ER, E, E, E, ER, E, ER, E, ER, E, E],  "inOut" :"10011001", "name":'Self-test diagnostic'},
    '10981':   { "Nodes" : [E, E, E, ER, E, E, E, E, ER, E, E, E], "inOut" :'01000010', "name": 'Signal amplifier'},
    '20176':   { "Nodes" : [E, E, E, E, E, E, E, ER, E, E, E, E],  "inOut" :'01100110', "name": 'Differential converter'},
    '21340':   { "Nodes" : [E, E, E, E, E, ER, ER, ER, E, E, E, E],"inOut" : '10000111', "name": 'Signal comparator'},
    '22280':   { "Nodes" : [E, E, E, E, E, E, E, E, ER, E, E, E],  "inOut" : '01110010', "name": 'Signal multiplexer'},
    '30647':   { "Nodes" : [E, E, E, E, E, E, E, E, E, ER, E, E],  "inOut" : '01100010', "name": 'Sequence generator'},
    '31904':   { "Nodes" : [E, E, E, ER, E, E, E, E, E, E, E, E],  "inOut" : '01000110', "name": 'Sequence counter'},
    '32050':   { "Nodes" : [E, E, E, E, E, E, E, E, ER, E, E, E],  "inOut" : '01000010', "name": 'Signal edge detector'},
    '33762':   { "Nodes" : [E, E, E, E, E, E, E, E, ER, E, E, E],  "inOut" : '11110010', "name": 'Interrupt handler'},
    '40633':   { "Nodes" : [E, E, E, ER, E, E, E, E, E, E, E, E],  "inOut" : '01000010', "name": 'Signal pattern detector'},
    '41427':   { "Nodes" : [E, E, E, E, E, E, E, ER, E, E, E, E],  "inOut" : '01000110', "name": 'Sequence peak detector'},
    '42656':   { "Nodes" : [E, E, S, E, E, E, E, E, ER, S, E, E],  "inOut" : '01000010', "name": 'Sequence reverser'},
    '43786':   { "Nodes" : [E, E, E, E, S, E, E, S, ER, E, E, E],  "inOut" : '01100010', "name": 'Signal multiplier'},
    '50370':   { "Nodes" : [E, E, E, E, ER, E, E, E, E, E, E, E],  "inOut" : '00000010', "name": 'Image test pattern 1'},
    '51781':   { "Nodes" : [ER, E, E, E, E, E, E, E, E, E, E, E],  "inOut" : '00000010', "name": 'Image test pattern 2'},
    '52544':   { "Nodes" : [E, E, E, ER, E, E, E, E, E, E, E, E],  "inOut" : '01000010', "name": 'Exposure mask viewer'},
    '53897':   { "Nodes" : [E, E, E, E, E, E, E, E, ER, E, E, E],  "inOut" : '01000010', "name": 'Histogram viewer'},
    '60099':   { "Nodes" : [ER, E, E, S, E, E, E, E, E, E, E, S],  "inOut" : '01000110', "name": 'Signal window filter'},
    '61212':   { "Nodes" : [E, E, E, E, S, E, E, S, E, E, E, ER],  "inOut" : '01100110', "name": 'Signal divider'},
    '62711':   { "Nodes" : [E, S, E, ER, E, E, E, E, E, S, E, E],  "inOut" : '10100010', "name": 'Sequence indexer'},
    '63534':   { "Nodes" : [ER, E, S, E, E, E, E, E, E, S, E, E],  "inOut" : '01000010', "name": 'Sequence sorter'},
    '70601':   { "Nodes" : [E, E, E, E, E, E, E, E, E, E, E, E],   "inOut" : '01000010', "name": 'Stored image decoder'},
    'UNKNOWN': { "Nodes" : [E, E, E, ER, E, E, E, ER, ER, E, E, E],"inOut" :'00000000', "name": ''},
    'USEG0':   { "Nodes" : [E, E, E, E, E, E, E, E, E, E, E, E],   "inOut" : '00000000', "name": 'Simple sandbox'},
    'USEG1':   { "Nodes" : [E, E, S, E, E, E, E, E, E, S, E, E],   "inOut" : '00000000', "name": 'Stack memory sandbox'},
    'USEG2':   { "Nodes" : [E, E, E, E, E, E, E, E, E, E, E, E],   "inOut" : '00000000', "name": 'Image console sandbox'}
    }

for key in LEVELS:
 if Problem.query.filter_by(identifier = key ).count() == 0:
  problem = Problem(
    LEVELS[key]["Nodes"][0],
    LEVELS[key]["Nodes"][1],
    LEVELS[key]["Nodes"][2],
    LEVELS[key]["Nodes"][3],
    LEVELS[key]["Nodes"][4],
    LEVELS[key]["Nodes"][5],
    LEVELS[key]["Nodes"][6],
    LEVELS[key]["Nodes"][7],
    LEVELS[key]["Nodes"][8],
    LEVELS[key]["Nodes"][9],
    LEVELS[key]["Nodes"][10],
    LEVELS[key]["Nodes"][11],
    int(LEVELS[key]["inOut"][0]),
    int(LEVELS[key]["inOut"][1]),
    int(LEVELS[key]["inOut"][2]),
    int(LEVELS[key]["inOut"][3]),
    int(LEVELS[key]["inOut"][0]),
    int(LEVELS[key]["inOut"][1]),
    int(LEVELS[key]["inOut"][2]),
    int(LEVELS[key]["inOut"][3]),
    key,
    LEVELS[key]["name"])
  db.session.add(problem)
  db.session.commit()
