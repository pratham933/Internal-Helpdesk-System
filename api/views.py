from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def health_check(request):
    return Response(
        {
            'success': True,
            'message': 'Helpdesk API is running',
            'data': {
                'service': 'Internal Helpdesk System',
                'version': '1.0'
            }
        },
        status=status.HTTP_200_OK
    )