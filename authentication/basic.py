import base64
import hashlib
from authenticator import Authenticator


class Basic(Authenticator):

    def authenticate(self, credentials):
        user = None

        try:
            username, password = base64.b64decode(credentials).split(':')
            md5 = hashlib.md5(password).hexdigest()
            # user = User.query.find_by(username=username, password=md5).one().id
            user = 1
        except:
            pass

        return user
