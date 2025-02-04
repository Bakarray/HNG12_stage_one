from django.urls import path
from .views import NumberClassificationView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('classify-number/', NumberClassificationView.as_view(), name='classify-number'),
]

urlpatterns = format_suffix_patterns(urlpatterns)