from utils import *
from pattern import Pattern

class Scarf(Pattern):
    def __init__(self, fpath):
        super().__init__(fpath)
        lines = ('\n').join(self._pattern_rows)
        i,j = regex_search('[0-9]+(\.[0-9]+)?\s?(\”|\"|IN|CM)', lines, 'all')
        self._length_units = get_decimals_from_string(lines[i:j])[0] # assume the unit used in gauge is the same unit here