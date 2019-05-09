from django.urls import path
from .import views

app_name = 'mango'

urlpatterns = [
    path('',views.MemberListview.as_view(), name='index'),
    path('add_Member', views.MemberCreateView.as_view(),name='add_Member'),
    path('<int:pk>/update', views.MemberUpdateView.as_view(),name ='update-member'),
    path('<int:pk>/Delete', views.MemberDeleteView.as_view(),name = 'Delete-member'),
]