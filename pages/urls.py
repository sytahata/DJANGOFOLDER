#import paths to resolve web paths
from django.urls import path
from .views import homepageview,aboutpageview,detailview,createviewpost,updateviewpost,deleteviewpost

urlpatterns = [
    path("", homepageview.as_view(),name="home"),
    path("about/", aboutpageview.as_view(), name="about"),
    path("post/<int:pk>/",detailview.as_view(),name="post_details"),
    path("post/new/",createviewpost.as_view(),name="post_new"),
    path("post/<int:pk>/edit",updateviewpost.as_view(),name="post_edit"),
    path("post/<int:pk>/delete",deleteviewpost.as_view(),name="post_delete")
]