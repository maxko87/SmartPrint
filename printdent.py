from __future__ import print_function
import traceback

def pprint(*args, **kwargs):
    tabs = max(len(traceback.format_stack())-2,0)
    result = "  " * tabs + args[0]
    args = list(args)
    args[0] = result
    args = tuple(args)
    return print(*args, **kwargs)
