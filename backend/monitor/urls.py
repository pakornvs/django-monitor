from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import RoomViewSet, VideoViewSet, home

router = DefaultRouter()
router.register("rooms", RoomViewSet, basename="room")
router.register("videos", VideoViewSet, basename="video")

urlpatterns = [
    path("", home, name="home"),
    #path("video_feeds/<int:video_id>/", VideoFeedView.as_view(), name="video-feed"),
    #path("upload/", UploadVideoView.as_view(), name="video-upload"),
] + router.urls
