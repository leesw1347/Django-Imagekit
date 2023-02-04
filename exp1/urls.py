from django.urls import path

from exp1 import views

urlpatterns = [
    path('exp1Sync/' , views.sync_view , name='exp1_sync') ,
    path('exp1Async/' , views.async_view , name='exp1_async') ,
    path('exp1AsyncAction/' , views.async_view_actions , name='exp1_async_action') ,
]
