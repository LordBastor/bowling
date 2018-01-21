from django.conf.urls import url
from .views import AliveView

urlpatterns = [
	url(r'^alive$', AliveView.as_view()),
]
