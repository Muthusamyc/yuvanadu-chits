from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('productandservice',views.productandservice,name='product and service'),
    path('contact',views.contact,name='contact'),
    path('payment',views.payment,name='payment'),
    path('securitiesacceptable',views.securitiesacceptable,name='securitiesacceptable'),
    ]
   