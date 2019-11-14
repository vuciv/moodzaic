from community.models import Community
from community.serializers import CommunitySerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

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
