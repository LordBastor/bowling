from .serializers import BowlingGameSerializer
from .models import BowlingGame

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.http import Http404


class BowlingGameView(APIView):
	def post(self, request):
		"""
			Creates a new bowling game for the current user
			Does not require a score input but can accept full or partial
			score comma separated integer list
			
			Response code: 201
			
			Response body: BowlingGameSerializer
			---
			
			serializer: BowlingGameSerializer
		"""
		data = request.data
		user = request.user
		
		data['user'] = request.user.id
		
		serializer = BowlingGameSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(data=serializer.data, status=status.HTTP_201_CREATED)
		return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BowlingGameDetailView(APIView):
	def get_game(self, id):
		try:
			return BowlingGame.objects.get(pk=id)
		except BowlingGame.DoesNotExist:
			raise Http404()
	
	def get(self, request, id):
		"""
			Return a bowling game by its id
			
			Response code: 200
			
			Response body: BowlingGameSerializer
			---
			
			serializer: BowlingGameSerializer
		"""
		game		 = self.get_game(id)
		serializer	 = BowlingGameSerializer(game)
		
		return Response(data=serializer.data, status=status.HTTP_200_OK)
	
	def put(self, request, id):
		"""
			Updates a bowling game by its id
			can be passed `roll` parameter to add roll to game by id
			
			Response code: 200
			
			Response body: BowlingGameSerializer
			---
			
			serializer: BowlingGameSerializer
		"""
		game = self.get_game(id)
		roll = None
		data = request.data
		
		if 'roll' in data and data['roll']:
			roll = data.pop('roll')
		
		serializer = BowlingGameSerializer(game, data=data, partial=True)
		if serializer.is_valid():
			updated_game = serializer.save()
			
			if roll:
				game.rolls = game.rolls + '{},'.format(roll)
				game.save()
			return Response(data=serializer.data, status=status.HTTP_200_OK)
		return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BowlingGameListView(APIView):
	def get(self, request):
		"""
			Returns a list of paignated bowling games for the current user
		"""
