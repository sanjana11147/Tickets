from rest_framework import generics, permissions, renderers
from tickets.models import Ticket
from tickets.serializers import TicketSerializer, UserSerializer
from django.contrib.auth.models import User
from tickets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'users': reverse('user-list', request=request, format=format),
		'tickets': reverse('ticket-list', request=request, format=format)
})

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class index(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset = Ticket.objects.all()
	serializer_class = TicketSerializer
		
	def perform_create(self,serializer):
		serializer.save(owner=self.request.user)

class detail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
	queryset = Ticket.objects.all()
	serializer_class = TicketSerializer

