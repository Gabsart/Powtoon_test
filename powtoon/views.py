from urllib.request import Request
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Case, When, Value, BooleanField

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from .models import Powtoon, User
from .serializers import PowtoonSerializer, PowtoonBasicSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Login': '/login/',
        'Logout': '/logout/',
        'List Owned Powtoon':'/powtoon/',
        'Create Powtoon':'/powtoon/ -> POST',
        'Get a Powtoon': '/powtoon/id',
        'Edit Powtoon':'/powtoon/id -> PUT',
        'Share Powtoon with other users':'/powtoon/id -> PATCH/',
        'Delete Powtoon':'/powtoon/id -> DELETE',
        'List Powtoons shared with me':'/powtoon/shared/',
        'Get shared Powtoon': '/powtoon/shared/id'
    }
    return Response(api_urls)


class UserLogin(LoginView):
    template_name = 'login.html'


def logoutView(request):
    logout(request)
    return HttpResponse('<h1>Logout succesful</h1>')


#List and POST of owned powtoons
class PowtoonViewSet(generics.ListCreateAPIView):
    queryset = Powtoon.objects.all()
    serializer_class = PowtoonSerializer
    

#GET, PUT(edit), PATCH(add to shared users) of owned powtoons
class PowtoonDetailViewSet(LoginRequiredMixin, UserPassesTestMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Powtoon.objects.all()
    serializer_class = PowtoonSerializer

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


#GET of a shared powtoon
class SharedRetrieveViewSet(LoginRequiredMixin, UserPassesTestMixin, generics.RetrieveAPIView):
    queryset = Powtoon.objects.all()
    serializer_class = PowtoonSerializer

    def test_func(self):
        obj = self.get_object()
        sharedPowtoon=Case(
                        When(
                            sharedWith=self.request.user,
                            then=Value(True)
                        ),
                        default=Value(False),
                        output_field=BooleanField()
                    )
        return sharedPowtoon


#List of shared powtoons
class SharedViewSet(LoginRequiredMixin, generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = PowtoonBasicSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Powtoon.objects.filter(sharedWith=user.id)


#List and POST of owned powtoons
class OwnedViewSet(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Powtoon.objects.all()
    serializer_class = PowtoonBasicSerializer

    # Defaults owner to request user
    def perform_create(self, serializer_class):
        serializer_class.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Powtoon.objects.filter(owner=user.id)
