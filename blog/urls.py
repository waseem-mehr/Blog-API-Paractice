
from django.urls import path
from .views import HomePage,PostDetail,PostList
app_name="first app"

urlpatterns = [
    path('',HomePage.as_view(),name="home"),
    path('all-posts/',PostList.as_view(),name="post_list"),
    path('post/<int:pk>/',PostDetail.as_view(),name="post_detail"),

]
