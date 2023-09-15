from rest_framework.views import APIView, status, Response
from .models import Album
from .serializers import AlbumSerializer
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView


class AlbumView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def get_queryset(self):
        router_parameter = self.request.query_params.get("pk")

        if router_parameter:
            queryset = Album.objects.filter(album_id=router_parameter)
            return queryset

        return super().get_queryset()

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)
