from authenticator import Authenticator
import base64


class Basic(Authenticator):

    def authenticate(self, credentials):
        try:
            username, pwd = base64.b64decode(credentials).split(':')
            print username, pwd
            # return User.query.find_by(username=username, password=pwd).one()
            return 2
        except:
            raise Exception('...')
