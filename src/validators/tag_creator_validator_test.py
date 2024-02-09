from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .tag_creator_validator import tag_creator_validator



class MockRequest:
    def __init__(self, json) -> None:
        self.json = json

def test_tag_creator_validator():
    reqst = MockRequest(json = { "product_code": "12" })
    tag_creator_validator(reqst)


def test_tag_creator_validator_with_error():
    reqst = MockRequest(json = { "product_code": 12 })

    try:
        ## Case not throw the exception then the test failed. [next lines]
        tag_creator_validator(reqst)
        assert False
    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)
