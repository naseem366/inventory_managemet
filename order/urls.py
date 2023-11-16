from django.urls import path
from order import views

urlpatterns = [
    path('order_list',views.order_list,name='order_list'),
    path('create_order/<int:id>', views.create_order,name='create_order'), 
    path('recived_order/<int:id>',views.RecivedOrder,name='recived_order'),
    path('cancel_order/<int:id>',views.CancelOrder,name='cancel_order'),
    path("sell_order/<int:id>",views.sell_order,name='sell_order'),

# Transaction Urls 
    path("trans_list",views.trans_list,name='trans_list'),
    path("create_trans/<int:id>",views.create_trans,name="create_trans"),
    path("ApprovedTrans/<int:id>",views.ApprovedTrans,name="ApprovedTrans"),
]