# -*- coding: utf-8 -*-
import sys


if sys.version_info >= (3,):
    from urllib.parse import urlparse, urljoin
    from queue import Queue
    import queue
    from urllib.robotparser import RobotFileParser
    from urllib.error import URLError
else:
    from urlparse import urlparse, urljoin


    from Queue import Queue
    import Queue as queue


    from robotparser import RobotFileParser


    from urllib2 import URLError


if sys.version_info >= (3,):
    from atexit import unregister
else:
    import atexit
    def unregister(func, *targs, **kargs):

        """unregister a function previously registered with atexit.
           use exactly the same aguments used for before register.
        """
        for i in range(0,len(atexit._exithandlers)):
            if (func, targs, kargs) == atexit._exithandlers[i] :
                del atexit._exithandlers[i]
                return True
        return False
