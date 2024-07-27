import re

def regex_search(pat, string, area='start'):
    assert area in {'start','end','all'}, "Area should be one of 'start', 'end', or 'all'."
    m = re.search(pat, string, re.MULTILINE)
    m = m.span()
    if area == 'start':
        return m[0]
    elif area == 'end':
        return m[1]
    elif area == 'all':
        return m