from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),
    # to make routing dynamic based of pk in db
    path('item/<int:pk>/', views.MenuItemDetail.as_view(), name="menu_item"),
]
