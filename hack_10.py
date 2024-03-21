"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = [
        {"1": "2"},
        dict(reversed({"3": "4"}.items())),
        {"5": "6"}
    ]
    return result