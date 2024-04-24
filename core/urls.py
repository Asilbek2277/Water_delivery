from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path, include
from waterApp.views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('buyurtmalar', BuyurtmaModelViewSet)
router.register('admin', AdmintmaModelViewSet)
router.register('haydovchilar', HaydovchiModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('suvlar/', SuvlarAPIView.as_view()),
    path('suv/<int:pk>/', WaterAPI.as_view()),
    path('mijozlar/', MijozlarAPIView.as_view()),
    path('mijoz/<int:pk>/', ClientAPI.as_view()),
]
