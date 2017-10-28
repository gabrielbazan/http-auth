# HTTP Authentication

This brief development shows how you could implement multiple
strategies for HTTP authentication in a Python application.

It is applicable to any HTTP interface implemented in Python,
and includes an implementation for Basic and Token auth.

For example, this is how you could use it from Flask:

```
from functools import wraps
from flask import request, Response
from authentication import AuthenticatorFactory


def validate(authorization):
    method, value = authorization.split(' ')
    return AuthenticatorFactory.create(method).authenticate(value)

def authenticate():
    return Response('Authentication failure', 401)

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization')
        if not auth or not validate(auth):
            return authenticate()
        return f(*args, **kwargs)
    return decorated
    
@app.route('/secret-page')
@requires_auth
def secret_page():
    return render_template('secret_page.html')
```


## Installation

```
git clone https://github.com/gabrielbazan/http-auth.git

cd http-auth/

virtualenv venv

./venv/bin/pip install -r requirements.txt
```
