from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('login/home/', views.apiOverview, name="api-overview"),
    path('login/', views.UserLogin.as_view(), name="login"),
    path('logout/', views.logoutView, name="logout"),
    path('powtoon/', views.OwnedViewSet.as_view(), name="list-powtoons"),
    path('powtoon/<int:pk>', views.PowtoonDetailViewSet.as_view(), name="get-powtoon"),
    path('powtoon/shared/', views.SharedViewSet.as_view(), name="shared-with-me"),
    path('powtoon/shared/<int:pk>', views.SharedRetrieveViewSet.as_view(), name="shared-with-me"),
]