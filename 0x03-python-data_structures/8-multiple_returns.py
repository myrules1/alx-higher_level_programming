#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return "",None
    else:
        ln = len(sentence)
        fchar = sentence[0]
    return ln,fchar
