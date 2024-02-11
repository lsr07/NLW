from cerberus import Validator

body = {
    "data": {
        "elemento1": 123.25,
        "elemento2": "ÉS DIABO",
        "elemento3": "123"
    }
}

body_validator = Validator({
    "data": {
        "type": "dict",
        "schema": {
            "elemento1": { "type": "float", "requerid": True, "empty": False },
            "elemento2": { "type": "string", "requerid": True, "empty": True },
            "elemento3": { "type": "string", "requerid": False, "empty": False },
        }
    }
})

response = body_validator.validate(body)

if response is False:
    print(body_validator.errors)
else:    
    print('Body OK')
