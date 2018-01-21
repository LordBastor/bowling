from rest_framework import serializers

from .models import BowlingGame

class BowlingGameSerializer(serializers.ModelSerializer):
	score = serializers.SerializerMethodField()
	
	class Meta:
		model = BowlingGame
		fields = (
			'id',
			'user',
			'rolls',
			'score',
		)
	
	def get_score(self, obj):
		# how to do score
		return 0
