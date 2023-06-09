from .models import Car, NewUser
from .serializers import CarSerializer, UserRegisterSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .permissions import IsOwerOrReadOnlyAuthenticated, IsAdminOrOwerOrReadOnlyAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .resources import CarResources
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# class CarViewSet(viewsets.ModelViewSet):
#     # queryset = Car.objects.all()
#     serializer_class = CarSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         if not pk:
#             return Car.objects.all()
#
#         return Car.objects.filter(pk=pk)
#
#     @action(methods=["get"], detail=False)
#     def users(self, request):
#         userrr = NewUser.objects.all()
#         return Response({'users': [user.username for user in userrr]})
class CarApiView(APIView):

    @method_decorator(cache_page(60 * 15))
    def get(self, request):
        model = Car.objects.all()

        return Response({'car': CarSerializer(model, many=True).data})



class CarAPIList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (JWTAuthentication,)


class CarAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsOwerOrReadOnlyAuthenticated,)
    # authentication_classes = (TokenAuthentication,)


class CarAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsOwerOrReadOnlyAuthenticated,)


class CarAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAdminOrOwerOrReadOnlyAuthenticated,)


class RegisterUserView(generics.CreateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response
        else:
            data = serializer.errors
            return Response(data)


class DownloadDataBase(APIView):
    def get(self, request):
        car_resource = CarResources()
        dataset = car_resource.export()
        response = HttpResponse(dataset.xls)
        response['Content-Disposition'] = 'attachment; filename="cars.xls"'
        return response
