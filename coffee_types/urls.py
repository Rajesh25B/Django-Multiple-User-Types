from django.urls import path
from coffee_types.views import create_views, detail_views

urlpatterns = [
    path('manage/', create_views.ManageListingView.as_view()),
    path('detail/', detail_views.CoffeeDetailView.as_view()),
    path('coffee-list/', detail_views.CoffeeListView.as_view()),
]
