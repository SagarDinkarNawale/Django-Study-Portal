from django.urls import path,include
from . import views

urlpatterns = [
     
    path('',views.viewbookbcs,name='viewbookbcs'),
    # path('viewbookbcs/', job.views.viewbookbcs,name='viewbookbcs'),  

    path('<int:book_id>/',views.getbook,name='getbook'),
    
    
]
