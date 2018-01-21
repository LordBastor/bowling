from django.db import models
from django.conf import settings

from django.core.validators import validate_comma_separated_integer_list


class BaseModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	class Meta:
		abstract = True
		ordering = ['-updated_at']


class BowlingGame(BaseModel):
	user	 = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
	rolls	 = models.CharField(
		max_length=511,
		blank=True,
		null=True,
		validators=[validate_comma_separated_integer_list]
	)
