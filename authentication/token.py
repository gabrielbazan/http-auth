from authenticator import Authenticator
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired


class Token(Authenticator):

    secret_key = 'secret'
    expiration = 600

    def authenticate(self, token):
        s = Serializer(self.secret_key)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token

        # return User.query.get(data['id'])
        return data['id']

    def generate(self, user_id):
        s = Serializer(self.secret_key, expires_in=self.expiration)
        return s.dumps({'id': user_id})
