from pypdf import PdfReader
from .utils import *

class Pattern:
    def __init__(self, fpath):
        reader = PdfReader(fpath)
        lines = ''
        for page in reader.pages:
            lines += "\n" + page.extract_text()
        lines = lines.upper()
        self._unit = 'in'
        self._gauge = ((8.5,14),(4,4)) # TODO: change this so we parse it from PDF. Wasn't in scarf PDF.

        pattern_rows = lines[regex_search('(CO|CAST ON)\s+[0-9]+\s+ST(ITCHE)?S', lines):]
        pattern_rows = pattern_rows[:regex_search('BO|BIND OFF', pattern_rows, 'end')]
        i,j = regex_search('[0-9]+', pattern_rows, 'all')
        self._co_st = int(pattern_rows[i:j])
        pattern_rows = filter(lambda x: len(x) > 0, [s.strip() for s in pattern_rows.split('\n')[1:-1]])
        self._pattern_rows = list(pattern_rows)

    def __repr__(self) -> str:
        dct = vars(self)
        return '\n'.join("%s: %s" % item for item in dct.items())

    @property
    def unit(self):
        return self._unit
    
    @unit.setter
    def unit(self, change_unit=False):
        assert type(change_unit) == bool, "Change unit should be either be True (change units) or False (keep units)."
        if change_unit:
            self._unit = 'in' if self._unit == 'cm' else 'cm'
            conv_factor = 2.54
            if self._unit == 'in':
                self._gauge = (self._gauge[0], (self._gauge[1][0]/conv_factor, self._gauge[1][1]/conv_factor))
            else:
                self._gauge = (self._gauge[0], (self._gauge[1][0]*conv_factor, self._gauge[1][1]*conv_factor))
        return self._unit

    @property
    def gauge(self):
        return self._gauge
    
    @property
    def pattern_rows(self):
        return self._pattern_rows
    
    @property
    def co_st(self):
        return self._co_st