import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

IP = "localhost"

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

CSRF_ENABLED = True

levels = {
    '00150': (0, 2, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0, '10011001', 'Self-test diagnostic'),
    '10981': (0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, '01000010', 'Signal amplifier'),
    '20176': (0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, '01100110', 'Differential converter'),
    '21340': (0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, '10000111', 'Signal comparator'),
    '22280': (0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, '01110010', 'Signal multiplexer'),
    '30647': (0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, '01100010', 'Sequence generator'),
    '31904': (0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, '01000110', 'Sequence counter'),
    '32050': (0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, '01000010', 'Signal edge detector'),
    '33762': (0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, '11110010', 'Interrupt handler'),
    '40633': (0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, '01000010', 'Signal pattern detector'),
    '41427': (0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, '01000110', 'Sequence peak detector'),
    '42656': (0, 0, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, '01000010', 'Sequence reverser'),
    '43786': (0, 0, 0, 0, 1, 0, 0, 1, 2, 0, 0, 0, '01100010', 'Signal multiplier'),
    '50370': (0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, '00000010', 'Image test pattern 1'),
    '51781': (2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '00000010', 'Image test pattern 2'),
    '52544': (0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, '01000010', 'Exposure mask viewer'),
    '53897': (0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, '01000010', 'Histogram viewer'),
    '60099': (2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, '01000110', 'Signal window filter'),
    '61212': (0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, '01100110', 'Signal divider'),
    '62711': (0, 1, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, '10100010', 'Sequence indexer'),
    '63534': (2, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, '01000010', 'Sequence sorter'),
    '70601': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '01000010', 'Stored image decoder'),
    'UNKNOWN': (0, 0, 0, 2, 0, 0, 0, 2, 2, 0, 0, 0, '',  ''),
    'USEG0': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', 'Simple sandbox'),
    'USEG1': (0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, '', 'Stack memory sandbox'),
    'USEG2': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', 'Image console sandbox')
}