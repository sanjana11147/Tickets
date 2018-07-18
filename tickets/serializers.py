from rest_framework import serializers
from tickets.models import Ticket
from django.contrib.auth.models import User



class TicketSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Ticket
		fields = ('url', 'id', 'title', 'description', 'pub_date', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
	tickets = serializers.HyperlinkedRelatedField(many=True, view_name='ticket-detail', read_only=True)

	class Meta:
		model = User
		fields = ('url', 'id', 'username', 'tickets')
