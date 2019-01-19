import sys

def is_py3():
    return sys.version_info[0] == 3
def is_py2():
    return sys.version_info[0] == 2

if is_py3():
    import urllib.request as urllib
else:
    import urllib


