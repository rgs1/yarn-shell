""" a simple proxy for YARN's REST API """

import requests


HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}


class YarnProxy(object):
    """ a simple proxy into YARN's world """

    def __init__(self, rm_endpoint, scheme='http', session=None):
        self.rm_endpoint = rm_endpoint
        self._scheme = scheme
        self._session = session if session else requests.Session()

    def _fetch(self, path):
        """ help to hitting endpoints """
        url = '{}://{}/ws/v1{}'.format(
            self._scheme,
            self.rm_endpoint,
            path)
        resp = self._session.get(url, headers=HEADERS)
        if resp.status_code != 200:
            return {}
        return resp.json()

    def cluster_info(self):
        """ get basic info about the backing YARN cluster """
        return self._fetch('/cluster/info').get('clusterInfo', {})

    def cluster_metrics(self):
        """ get metrics about the backing YARN cluster """
        return self._fetch('/cluster/metrics').get('clusterMetrics', {})
