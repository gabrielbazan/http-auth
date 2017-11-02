from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from authenticator import Authenticator


class Token(Authenticator):

    secret_key = 'secret'
    expiration = 600

    def authenticate(self, token):
        s = Serializer(Token.secret_key)

        try:
            data = s.loads(token)
        except (SignatureExpired, BadSignature):
            return None

        # Return the user's identifier
        return data['id']

    @staticmethod
    def generate(user_id):
        s = Serializer(Token.secret_key, expires_in=Token.expiration)
        return s.dumps({'id': user_id})
