
from django.urls import path 
from myapp.views import hello_world, my_hotel_menu

# it maps addresses with their corresponding functions

urlpatterns = [
    # whenever someone is trying to access this address
    # return them the response generated by the 'hello_world' function
    path('hello/', hello_world),
    path('mymenu/', my_hotel_menu)
]