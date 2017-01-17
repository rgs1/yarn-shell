""" helpers for tests """


def session(pdict):
    """ a session object that returns pdict on resp.json() """

    class Session(object):
        """ mock requests Session """
        def get(self, *args, **kwargs):
            class Response(object):
                @property
                def status_code(self):
                    return 200

                def json(self):
                    return pdict

            return Response()

    return Session()
