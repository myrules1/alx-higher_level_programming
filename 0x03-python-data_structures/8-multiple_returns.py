#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0,None)
    else:
        ln = len(sentence)
        fchar = sentence[0]
    return (ln,fchar)
