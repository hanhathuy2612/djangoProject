import logging

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

logger = logging.getLogger(__name__)


class InfoView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, info_id: int):
        logger.info(f"Get App Info: {info_id}")
        params = request.query_params.get('params', None)
        logger.info(f"Get params: {params}")
        return Response(
            {
                "data": "info"
            },
            status=200
        )
