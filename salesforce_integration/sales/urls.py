from django.db import router
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('',views.UserViewSet,basename='user')

# This is api url 
urlpatterns=[
    path('',include(router.urls))
    
]