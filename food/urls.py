from django.urls import path, include
from food import views

app_name = 'food'

urlpatterns = [
    # funtion based index view
#--------------------------------------
    # path('home/', views.index, name='index'),
    # class based index view
#-----------------------------------------------------------
    path('home/', views.IndexClassView.as_view(), name='index'),
    # funtion based detail view
#------------------------------------------------------------------
    # path('detail/<int:item_id>/', views.detail, name = 'detail'),
    # class based detail view
#------------------------------------------------------------------
    path('detail/<int:pk>/', views.FoodDetail.as_view(), name= 'detail'),

    #funtion based create view
#-----------------------------------------------------------
    path('add/', views.create_item, name='create_item'),
    #funtion based update item view
#----------------------------------------------------------
    path('update/<int:id>/', views.update_item, name='update_item'),
    #funtion based delete item view
#-----------------------------------------------------------------------   
    path('delete/<int:id>/', views.delete_item, name='delete_item'),

]