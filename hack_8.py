"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    ls = []
    
    if len(result) % 2 == 0:
        for u, p in enumerate(result):
            ls.append(str(u+1))
    else:
        for i, p in enumerate(result):
            ls.append(str(p) + "-" + str(i+1))
    
    return ls[::-1]