from .views import UploadFormView, UploadDetailView
from django.urls import path

urlpatterns = [
    path('<slug:slug>/', UploadDetailView.as_view(), name="upload"),
    path('', UploadFormView.as_view(), name="home"),
]

