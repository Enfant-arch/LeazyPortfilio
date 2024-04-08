from django.views import View
from django.http import HttpResponseNotFound, HttpResponse

from django.views.generic.base import TemplateView



class NotFoundView(View):
    def get(self, request):
        return HttpResponseNotFound(content="Can't find this page")
    


class FeedBackVeiw(View):
    def get(self, request):
        return HttpResponse(content="Good")