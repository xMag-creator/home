from .models import Device
from .serializers import DeviceSerializer
from rest_framework import generics


class DeviceListView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = DeviceSerializer
    lookup_field = 'username'

    def get_object(self):
        name = self.kwargs["name"]
        return generics.get_object_or_404(Device, name=name)
