from django.contrib import admin

# Register your models here.
from influencer.models import Influencer


class InfluencerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country')


admin.site.register(Influencer, InfluencerAdmin)
