from django.urls import path


from . import views

app_name = 'feed'

urlpatterns = [
    path('',views.HomePage.as_view(), name='index'),
    path("<int:pk>",views.DetailPostView.as_view(),name='detail'),
    path("new/",views.CreateNewPost.as_view(), name='new_post'),
    path('<int:pk>/delete/', views.DeletePost.as_view(), name='delete' ),
    path('follow_post/', views.FollowingHomePage.as_view(), name='follow_post' ),
    path('my_post/', views.MyPostHomePage.as_view(), name='my_post' ),
]