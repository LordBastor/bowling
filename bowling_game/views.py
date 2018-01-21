from .serializers import BowlingGameSerializer

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


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
		
		serializer = BowlingGameSerializer(data)
		if serializer.is_valid():
			serializer.save()
			return Response(data=serializer.data, status=status.HTTP_201_CREATED)
		return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BowlingGameDetailView(APIView):
	def get(self, request, id):
		"""
			Return a bowling game by its id
		"""
	def put(self, request, id):
		"""
			Updates a bowling game by its id
			can be passed `roll` parameter to add roll to game by id
		"""


class BowlingGameListView(APIView):
	def get(self, request):
		"""
			Returns a list of paignated bowling games for the current user
		"""
