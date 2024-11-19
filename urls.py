from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', main),
    path('index', index, name="index"),
    path('get-main', index, name="get-main"),
    path('magazine',magazine,name='magazine'),
    path('find_category/<int:id>/',find_category,name = "find_category"),
    path('search', search, name="search"),
    path('open_ad/<int:id>/', open_ad, name="open_ad"),
    path('add_ad/', add_ad, name="add_ad"),
    path('edit_ad/<int:id>/', edit_ad, name="edit_ad"),
    path('auth/', auth, name="auth"),
    path('reguser', reguser, name="reguser"),
    path('logout_view', logout_view, name="logout_view"),
    path('personal_cabinet', personal_cabinet, name="personal_cabinet"),
    path('fast_payment/', fast_payment, name="fast_payment"),
    path('delete_image/<int:id_card>/<int:id_picture>', delete_image, name="delete_image"),
    path('make_image_main/<int:id_card>/<int:id_picture>', make_image_main, name="make_image_main"),
    path('publish_ad/<int:id_card>/', publish_ad, name="publish_ad"),
    path('unpublish_ad/<int:id_card>/', unpublish_ad, name="unpublish_ad"),
    path('delete_card/<int:id_card>/', delete_card, name="delete_card"),

]