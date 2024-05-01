from .barcode_handler import BarCodeHandler


def test_create_barcode():

    the_barcode = "987-654-321"

    barcode_handler = BarCodeHandler()

    result = barcode_handler.create_barcode(the_barcode)

    assert result == the_barcode
