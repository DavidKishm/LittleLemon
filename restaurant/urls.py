from django.urls import path
from .views import MenuItemsView, SingleMenuItemView

urlpatterns = [
    path('', MenuItemsView.as_view()),
    path('<int:pk>', SingleMenuItemView.as_view()),
]