from basic import Basic
from token import Token
from exception import AuthenticationException


class AuthenticatorFactory(object):

    strategies = dict(
        basic=Basic(),
        token=Token()
    )

    @staticmethod
    def create(kind):
        kind = kind.lower()

        if kind not in AuthenticatorFactory.strategies:
            raise AuthenticationException(
                'Could not find a strategy for the given credentials'
            )

        return AuthenticatorFactory.strategies.get(kind)
