# -*- coding: utf-8 -*-

""" basic test cases """

import unittest

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

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
        class Session(object):
            """ mock requests Session """
            def get(self, *args, **kwargs):
                class Response(object):
                    @property
                    def status_code(self):
                        return 200

                    def json(self):
                        return {
                            'clusterInfo': {
                                'foo': 'bar'
                            }
                        }

                return Response()

        output = StringIO()
        proxy = YarnProxy('testrm', session=Session())
        shell = Shell(proxy, output=output, setup_readline=False)
        shell.onecmd('info')

        self.assertEqual(output.getvalue(), 'foo = bar\n')
