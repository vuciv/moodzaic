from users.models import User
from users.serializers import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from rest_framework import generics

@api_view(['GET', 'POST'])
def user_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        print(serializer)
        # if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # serializer_class = UserSerializer(data=request.data)
        # if serializer_class.is_valid():
        #     serializer_class.save()
        #     return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        # return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.get_queryset()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)