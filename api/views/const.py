from rest_framework.response import Response
from rest_framework import status

RESPONSE_FORBIDDEN = Response(
    data={
        'msg': 'Fobidden',
        'status': 403
    }, status=status.HTTP_403_FORBIDDEN
)

RESPONSE_NOT_FOUND = Response (
    data={
        'msg': 'Not Found',
        'status': 404
    }, status=status.HTTP_404_NOT_FOUND
)

RESPONSE_NOT_ACCEPTABLE = Response(
    data={
        'msg': 'Not Acceptable',
        'status': 406
    }, status=status.HTTP_406_NOT_ACCEPTABLE
)

def get_bad_request(msg) -> Response:
    return Response(
        {
            'msg': msg,
            'status': 400
        }, status=status.HTTP_400_BAD_REQUEST
    )