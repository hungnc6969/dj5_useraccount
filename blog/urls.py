from django.urls import path
from .views import BlogListView # lay tu file views.py, 
                                #phai ktra xem da update file nay chua

urlpatterns = [
    path('', BlogListView.as_view(), name = 'home'),
]