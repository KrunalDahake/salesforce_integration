from sales.models import User
from sales.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from .utils import login
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    
    
    
@action(methods=['post'], permission_classes=[AllowAny],detail=True)
def contact( request):
        sf = login()

        if request.method == 'POST':
            data = request.data.copy()
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                return_dict = serializer.validated_data
                query = sf.User.create({'first_name':'kunal','last_name':'dahake','mobile':89070065})
                return Response(query)
            else:
                return Response(serializer.errors)
        else:
            data = sf.query("Select Id,Name from Contact")
            result = UserSerializer(data['records'][0])
            return Response(result.data)    