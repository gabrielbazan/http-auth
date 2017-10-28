from authentication import AuthenticatorFactory, Token


def validate(authorization):
    method, value = authorization.split(' ')
    return AuthenticatorFactory.create(method).authenticate(value)


token = 'Token {}'.format(Token().generate(1))
basic = 'Basic dXNlcjpwYXNz'  # user: user, password: pass


user1 = validate(token)
user2 = validate(basic)

print user1, user2
