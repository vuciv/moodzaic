from community.models import Community
from users.models import User
from community.serializers import CommunitySerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
import logging

logger = logging.getLogger(__name__)


# class CommunityListCreate(generics.ListCreateAPIView):
#     queryset = Community.objects.all()
#     serializer_class = CommunitySerializer


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@ensure_csrf_cookie
def comDet(request):
    if request.method == 'PUT':
        return Response(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'POST', 'DELETE'])
@ensure_csrf_cookie

@api_view(['POST'])
def makeCommunity(request):
    if request.method == 'POST':
        serializer = CommunitySerializer(data=request.data)
        # logger.error(serializer.is_valid())
        # logger.error(serializer.data)
        # logger.error(serializer.errors)
        if serializer.is_valid():
            logger.error("is valid")
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)

class CommunityListCreate(generics.ListCreateAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

@api_view(['GET', 'POST', 'DELETE'])
def communityDetails(request, name):
    """
    Retrieve, update or get a community by name.
    """
    try:
        community = Community.objects.get(name=name)
        serializer = CommunitySerializer(community,context={'request': request})
        return Response(serializer.data)
    except Community.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = CommunitySerializer(community,context={'request': request})
            return Response(serializer.data)

        elif request.method == 'POST':
        #    serializer = CommunitySerializer(community, data=request.data,context={'request': request})
        #    if serializer.is_valid():
                #console.log('here')
                #serializer.save()
            #    return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            community.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # elif request.method == 'POST':
        #         serializer = CustomerSerializer(customer, data=request.data,context={'request': request})
        #         if serializer.is_valid():
        #             serializer.save()
        #             return Response(serializer.data)
        #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #
        # elif request.method == 'DELETE':
        #     community.delete()
        #     return Response(status=status.HTTP_204_NO_CONTENT)