from django.views import View
from django.http import HttpResponse


class MainPageView(View):
    def get(self, requests):
        return HttpResponse(content="good")