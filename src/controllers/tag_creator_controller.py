from typing import Dict
from src.drivers.barcode_handler import BarCodeHandler

class TagCreatorController:

    '''
        Responsabilidade para implementar as regras de negócios.
    '''

    def create(self, product_code: str) -> Dict:
        path_from_tag = self.__create_tag(product_code)
        the_response = self.__format_response(path_from_tag)
        return the_response

    ## Two initial underline represent that is a private method.
    def __create_tag(self, product_code: str) -> str:
        barcode_handler = BarCodeHandler()
        tag_path = barcode_handler.create_barcode(product_code)
        return tag_path


    def __format_response(self, tag_path: str) -> Dict:
        return {
            "data": {
                "type": "Tag image",
                "count": 1,
                "path": f'{tag_path}.png'
            }
        }
