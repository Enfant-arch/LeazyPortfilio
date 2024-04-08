from django.urls import path
from feedback.views import NotFoundView, FeedBackVeiw


urlpatterns = [
    path('', FeedBackVeiw.as_view(), name="not-fonund-view"),

]
