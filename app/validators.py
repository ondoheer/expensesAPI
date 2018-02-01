from cerberus import Validator

def validate_email(email):

    v = Validator()
    schema = {'email': {'type': 'string',
                        'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'}}
    document = {'email': email}

    return v.validate(document, schema), v.errors

def validate_password(password):

    v = Validator()
    schema = {'password': {'type': 'string',
                        'minlength': 8}}
    document = {'password': password}

    return v.validate(document, schema), v.errors

def validate_fullname(fullname):

    v = Validator()
    schema = {'fullname': {'type': 'string',
                'empty': False}}

    document = {'fullname': fullname}

    return v.validate(document, schema), v.errors


