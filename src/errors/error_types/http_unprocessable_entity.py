class HttpUnprocessableEntityError(Exception): ## This class has an inheritance from the Expt class.

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "UnprocessableEntity"
        self.status_code = 422
