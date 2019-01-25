from django.urls import path
from ad.views import AdListView, AdDetailView


urlpatterns = [
    path('', AdListView.as_view(), name='list'),
    path('detail/<pk>/', AdDetailView.as_view(), name='detail'),
]
