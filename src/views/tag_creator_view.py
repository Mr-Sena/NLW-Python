from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controller import TagCreatorController

class TagCreatorView:
    '''
        Responsiidade para interagir com HTTP.
    '''

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body["product_code"]

        # Business rule
        print('Processo em view.')
        tag_creator_controller = TagCreatorController()
        tag_data = tag_creator_controller.create(product_code)

        # HTTP Response.
        return HttpResponse(200, tag_data)
