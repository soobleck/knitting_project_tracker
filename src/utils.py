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

def get_decimals_from_string(string):
    num_i = ''
    point = True
    lst = []
    for c in string:
        if c.isnumeric():
            num_i += c
        elif c == '.':
            if point:
                num_i += c
            point = not point
        else:
            if len(num_i) > 0:
                lst.append(float(num_i))
                num_i = ''
    return lst