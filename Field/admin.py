# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Field,Review
from .forms import AddForm

# Register your models here.

class PitchModelAdmin(admin.ModelAdmin):
    form = AddForm
    class Meta:
        model = Field



admin.site.register(Field,PitchModelAdmin)
admin.site.register(Review)




