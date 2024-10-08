import logging

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from account.role_decorator import role_required

logger = logging.getLogger(__name__)


class AdminInfoView(APIView):
    permission_classes = [IsAuthenticated]

    @role_required('admin')
    def get(self, request, info_id: int):
        logger.info(f"Get App Info: {info_id}")
        params = request.query_params.get('params', None)
        logger.info(f"Get params: {params}")
        return Response(
            {
                "data": "Admin info"
            },
            status=200
        )
