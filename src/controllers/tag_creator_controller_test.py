from unittest.mock import patch
from src.drivers.barcode_handler import BarCodeHandler
from .tag_creator_controller import TagCreatorController

### Mock the create_barcode method, from the BarCodeHandler class.
@patch.object(BarCodeHandler, 'create_barcode')
def test_create(mock_create_barcode):

    mock_value = "image_path"

    ## When the funcion has called, then return the mock value.
    mock_create_barcode.return_value = mock_value
    tag_creator_controller = TagCreatorController()

    result = tag_creator_controller.create(mock_value)

    print(result)

    assert isinstance(result, dict)
    assert "data" in result
    assert "type" in result["data"]
    assert "count" in result["data"]
    assert "path" in result["data"]

    assert result["data"]["type"] == "Tag image"
    assert result["data"]["count"] == 1
    assert result["data"]["path"] == f'{mock_value}.png'
    