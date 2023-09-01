from django.urls import path, include
from rest_framework import routers
from app.views import ReceiptCodeViewSet, TextAPIView, Upload

router = routers.DefaultRouter()
router.register('ReceiptCodes', ReceiptCodeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('Text/', TextAPIView.as_view()),
    path('upload/', Upload.as_view()),
]