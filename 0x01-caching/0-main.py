#!/usr/bin/python3
"""
Test
"""
import sys

try:
    BasicCache = __import__('0-basic_cache').BasicCache

    my_cache = BasicCache()
    my_cache.print_cache()
    my_cache.put("test1", "myValue")
    my_cache.print_cache()
    my_cache.put(None, "myValue")
    my_cache.print_cache()
except:
    print(sys.exc_info()[1])
