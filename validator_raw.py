from cerberus import Validator

body = {
    "data": {
        "number": 123,
        "alpha": "Hey there!",
        "alphanumber": "123"
    }
}


body_valid = Validator( {
    "data": {
        "type": "dict",
        "schema": {
            "number": { "type": "float", "required": True, "empty": False},
            "alpha": { "type": "string", "required": True, "empty": True},
            "alphanumber": { "type": "string", "required": False, "empty": True}
        }
    }
})


response = body_valid.validate(body)


if response is False:
    print(body_valid.errors)
else:
    print('Body OK.')
