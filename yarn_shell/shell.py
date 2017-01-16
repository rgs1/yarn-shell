""" a shell to interact with a YARN cluster """

from functools import wraps

import os
import sys

from xcmd import (
    conf,
    xcmd
)


def connected(func):
    """ ensure there's a YARN proxy """
    @wraps(func)
    def wrapper(*args, **kwargs):
        self = args[0]
        if not self._proxy:
            self.show_output('Not connected to a YARN cluster.')
        else:
            return func(*args, **kwargs)

    return wrapper


# pylint: disable=R0904
class Shell(xcmd.XCmd):
    CONF_PATH = os.path.join(os.environ['HOME'], '.yarn_shell')
    DEFAULT_CONF = conf.Conf(
        conf.ConfVar(
            'default_resource_manager',
            'The default Resource Manager',
            ''
        )
    )

    def __init__(self, proxy, output=sys.stdout, setup_readline=True):
        xcmd.XCmd.__init__(self, None, setup_readline, output)
        self._proxy = proxy
        prompt = '(%s) ' % proxy.rm_endpoint if proxy else 'disconnected'
        self.update_curdir(prompt)

    def do_exit(self, *args):
        self._exit(False)

    def do_quit(self, *args):
        """
\x1b[1mNAME\x1b[0m
        quit - alias for exit
        """
        self._exit(False)

    def do_EOF(self, *args):
        """
\x1b[1mNAME\x1b[0m
        <ctrl-d> - Exits via Ctrl-D
        """
        self._exit(True)

    @connected
    def do_info(self, params):
        """
\x1b[1mNAME\x1b[0m
        info - Get info about the connected YARN cluster

\x1b[1mSYNOPSIS\x1b[0m
        info

\x1b[1mEXAMPLES\x1b[0m
        > info
       id = 1324053971963
       startedOn = 1324053971963
       state = STARTED
       ...

        """
        info = self._proxy.cluster_info()
        keys = sorted(info.keys())
        for key in keys:
            self.show_output("%s = %s", key, info[key])
