# HTTP Authentication

This brief development shows how you could implement multiple
strategies for HTTP authentication in a Python application.

It is applicable to any HTTP interface implemented in Python,
and includes an implementation for Basic and Token auth. You 
can add new authentication methods by writing new strategies 
and adding them to the _AuthenticatorFactory_ class.


## An Example

The _app.py_ script defines a very simple Flask application 
with HTTP authentication. You simply use the _@protected_ 
decorator to protect all the routes you want, as you can see 
in the _/secret_ route. 

The _/tokens_ only implements the 
_HTTP POST_ method in order to provide an endpoint that 
allows the user to create tokens. This is specially useful
for browser clients: When the user enters his credentials, 
you simply use _Basic_ auth to obtain the token, which you 
can store in order to reuse it each time you use the API. As 
you know, storing the user credentials is a big security 
risk.


## Installation

```
git clone https://github.com/gabrielbazan/http_auth.git

cd http_auth/

virtualenv venv

./venv/bin/pip install -r requirements.txt
```


## Run

```
./venv/bin/python app.py
```
