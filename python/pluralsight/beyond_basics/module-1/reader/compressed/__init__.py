# from module import *
# The __all__ attribute should be a list of strings containing
# names available in the module

from reader.compressed.bzipped import opener as bz2_opener
from reader.compressed.gzipped import opener as gzip_opener

__all__ = ['bz2_opener', 'gzip_opener']