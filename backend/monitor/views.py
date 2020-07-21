from django.shortcuts import redirect, render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .models import Room, Video
from .serializers import RoomSerializer, VideoSerializer


def home(request):
    video1 = Video.objects.get(id=1)
    video2 = Video.objects.get(id=2)
    context = {
        "video1": video1,
        "video2": video2,
    }
    return render(request, "index.html", context)


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return redirect("room-list")


class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return redirect("video-list")


# class VideoFeedView(View):
#     def get(self, request, video_id):
#         self.video = Video.objects.get(id=video_id)
#         # import json

#         # with open("/altotech/media/result.json") as json_file:
#         #     data = json.load(json_file)
#         # Video.objects.filter(id=1).update(metadata=data)

#         return StreamingHttpResponse(
#             self._process_frame(),
#             content_type="multipart/x-mixed-replace; boundary=frame",
#         )

#     def _process_frame(self):
#         boxes = self.video.metadata["boxes"]
#         for idx, frame in enumerate(self._frame_from_video()):
#             idx = str(idx)
#             if idx in boxes:
#                 for box in boxes[idx]:
#                     left, top, width, height = box
#                     frame = cv2.rectangle(
#                         frame,
#                         (left, top),
#                         (left + width, top + height),
#                         (0, 255, 0),
#                         2,
#                     )

#             _, jpeg = cv2.imencode(".jpeg", frame)
#             yield (
#                 b"--frame\r\n"
#                 b"Content-Type: image/jpeg\r\n\r\n" + jpeg.tobytes() + b"\r\n"
#             )
#             time.sleep(self.fps / 1000)

#     def _frame_from_video(self):
#         video = cv2.VideoCapture(self.video.content.path)
#         self.fps = video.get(cv2.CAP_PROP_FPS)
#         while video.isOpened():
#             success, frame = video.read()
#             if not success:
#                 break
#             yield frame
