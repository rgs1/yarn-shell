# -*- coding: utf-8 -*-

""" basic test cases """

import unittest

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from .util import session

from yarn_shell.shell import Shell
from yarn_shell.yarn_proxy import YarnProxy


class ProxyTestCase(unittest.TestCase):
    """ proxy cases """

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def test_info(self):
        resp = {
            'clusterInfo': {
                'foo': 'bar'
            }
        }

        output = StringIO()
        proxy = YarnProxy('testrm', session=session(resp))
        shell = Shell(proxy, output=output, setup_readline=False)
        shell.onecmd('info')

        self.assertEqual(output.getvalue(), 'foo = bar\n')

    def test_metrics(self):
        resp = {
            'clusterMetrics': {
                'containersAllocated': 20
            }
        }

        output = StringIO()
        proxy = YarnProxy('testrm', session=session(resp))
        shell = Shell(proxy, output=output, setup_readline=False)
        shell.onecmd('metrics')

        self.assertEqual(output.getvalue(), 'containersAllocated = 20\n')
