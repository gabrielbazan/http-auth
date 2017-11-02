from functools import wraps
from flask import Flask, request, jsonify
from authentication import AuthenticatorFactory, Token, AuthenticationException


app = Flask(__name__)


# This is an example, so we declare it here. You should store it elsewhere
user_id = None


@app.errorhandler(AuthenticationException)
def error(e):
    return jsonify(dict(message='Authentication failure', detail=str(e))), 401


def protected(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        header = request.headers.get('Authorization', '').split(' ')

        if len(header) != 2:
            raise AuthenticationException('Wrong credentials')

        method, value = header
        user = AuthenticatorFactory.create(method).authenticate(value)

        if not user:
            raise AuthenticationException('Wrong credentials')

        # Do something with the user
        global user_id
        user_id = user

        return f(*args, **kwargs)
    return decorated


@app.route('/secret', methods=['GET'])
@protected
def hello():
    return jsonify(dict(message='You are in!')), 200


@app.route('/tokens', methods=['POST'])
@protected
def authenticate():
    print user_id
    return jsonify(dict(token=Token.generate(user_id))), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
