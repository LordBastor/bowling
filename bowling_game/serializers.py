from rest_framework import serializers

from .models import BowlingGame

from bowling_main.score_helper import calculate_score


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
		if obj.rolls:
			roll_list = [int(r) for r in obj.rolls.rstrip(',').split(',')]
			return calculate_score(roll_list)
		return 0
