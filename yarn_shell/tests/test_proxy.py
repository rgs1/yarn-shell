# -*- coding: utf-8 -*-

""" basic test cases """

import unittest

from .util import session

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

        proxy = YarnProxy('testrm', session=session(resp))
        info = proxy.cluster_info()
        self.assertEqual(info['foo'], 'bar')

    def test_metrics(self):
        resp = {
            'clusterMetrics': {
                'containersAllocated': 20
            }
        }

        proxy = YarnProxy('testrm', session=session(resp))
        metrics = proxy.cluster_metrics()
        self.assertEqual(metrics['containersAllocated'], 20)
