from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from .views import UploadImages,DisplayImages,EditView,DeleteView,ReplyView,MyPageView
urlpatterns=[
path("upload/",UploadImages.as_view(),name="upload"),
path("display",DisplayImages.as_view(),name="display"),
path("<int:pk>/edit/",EditView.as_view(),name="edit"),
path("<int:pk>/delete/",DeleteView.as_view(),name="delete"),
path("<int:pk>/reply/",ReplyView.as_view(),name="reply"),
path("mypage",MyPageView.as_view(),name="mypage")
]
