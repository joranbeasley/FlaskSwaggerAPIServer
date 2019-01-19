from contextlib import contextmanager
from serve_swagger.py23compat_local import urllib

@contextmanager
def urllib_urlopen(url):
    fh = urllib.urlopen(url)
    yield fh
    fh.close()

def file_or_url_opener(url_or_file):
    if url_or_file.startswith("http"):
        return urllib_urlopen(url_or_file)
    return open(url_or_file)