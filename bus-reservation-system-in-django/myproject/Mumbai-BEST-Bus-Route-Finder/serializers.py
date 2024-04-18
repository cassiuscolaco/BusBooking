from rest_framework import serializers
from .models import MumbaiRoute

class MumbaiRouteSerializer(serializers.ModelSerializer):
	class Meta:
		model=MumbaiRoute
		fields='__all__'