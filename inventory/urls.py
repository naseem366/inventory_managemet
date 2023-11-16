from django.urls import path
from inventory import views

urlpatterns = [
    path('home',views.index,name='home'),
    path('show',views.show,name='show'),
    path('edit/<int:id>', views.edit,name='edit'),  
    path('update/<int:id>', views.update,name='update'),  
    path('delete/<int:id>', views.destroy,name='delete'), 
    path('management',views.management,name='management')
    
]