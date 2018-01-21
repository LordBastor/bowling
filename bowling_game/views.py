from django.shortcuts import render

from .serializers import BowlingGameSerializer

from rest_framework.views import APIView


class BowlingGameView(APIView):
	def post(self, request):
		"""
			Creates a new bowling game for the current user
			Does not require a score input but can accept full or partial
			score comma separated integer list
		"""
		pass


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
