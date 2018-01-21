from django.conf.urls import url
from .views import \
	BowlingGameView, \
	BowlingGameDetailView,\
	BowlingGameListView


urlpatterns = [
	url(r'^bowling$', BowlingGameView.as_view()),
	url(r'^bowling/list$', BowlingGameListView.as_view()),
	url(r'^bowling/(?P<id>[0-9]+)$', BowlingGameDetailView.as_view()),
]
