from django.contrib import admin

from .models import WordCheck, ApiCallHist

admin.site.register(WordCheck)
admin.site.register(ApiCallHist)
