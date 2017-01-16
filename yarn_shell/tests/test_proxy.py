# -*- coding: utf-8 -*-

""" basic test cases """

import unittest


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

        proxy = YarnProxy('testrm', session=Session())
        info = proxy.cluster_info()
        self.assertEqual(info['foo'], 'bar')
