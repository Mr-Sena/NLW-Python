from unittest.mock import patch
from .tag_creator_view import TagCreatorController
from .tag_creator_view import TagCreatorView
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

@patch.object(TagCreatorController, 'create')
def test_create(mock_create_controller):

    http_data = {
        "data": {
            "type": "Tag image",
            "count": 1,
            "path": f'{1012}.png'
        }
    }
    mock_create_controller.return_value = http_data

    client_request = HttpRequest(body = {"product_code": http_data["data"]["path"]})

    tag_creator_view = TagCreatorView()
    result = tag_creator_view.validate_and_create(client_request)


    assert isinstance(result, HttpResponse)
    assert result.status_code == 200
    assert result.body == http_data
