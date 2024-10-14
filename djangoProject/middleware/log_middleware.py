import logging

from django.http import HttpResponse

logger = logging.getLogger()


class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Initialization code here (if needed).

    def __call__(self, request):
        # Code executed for each request before the view is called.

        # Example: logging the request path and method
        logger.debug(f"Request Path: {request.path}")
        logger.info(f"Request Method: {request.method}")

        response = self.get_response(request)

        # Code executed for each request after the view is called.

        return response

    def process_exception(self, request, exception):
        logger.error(f"Exception caught: {str(exception)}")
        return HttpResponse("An error occurred. Please try again later.")
