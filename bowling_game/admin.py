from django.contrib import admin

from .models import BowlingGame


class BowlingGameAdmin(admin.ModelAdmin):
	list_display = (
		'user',
		'rolls',
		'created_at',
		'updated_at',
	)
admin.site.register(BowlingGame, BowlingGameAdmin)