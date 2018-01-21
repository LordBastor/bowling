from rest_framework import serializers

from .models import BowlingGame


class BowlingGameSerializer(serializers.ModelSerializer):
	class Meta:
		model = BowlingGame
		fields = (
			'id',
			'user',
			'rolls',
		)

