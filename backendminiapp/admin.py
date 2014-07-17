from django.contrib import admin
from backendminiapp.models import Legislator


class LegislatorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Legislator, LegislatorAdmin)