from basic import Basic
from token import Token


class AuthenticatorFactory(object):

    strategies = dict(
        basic=Basic(),
        token=Token()
    )

    @staticmethod
    def create(kind):
        kind = kind.lower()

        if kind not in AuthenticatorFactory.strategies:
            raise NotImplementedError(
                'Could not find a strategy for the given credentials'
            )

        return AuthenticatorFactory.strategies.get(kind)
