from django.urls import path, include
from service import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    #path('', include('django.contrib.auth.urls'), ),
    path('register', views.RegisterForm.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('', views.PostsView.as_view(), name='index'),
    path('post/<int:pk>', views.DetailPostsView.as_view(), name='detail_post'),
    path('create_post', views.CreatePostsView.as_view(), name='create_post'),
    path('update_post/<int:pk>', views.UpdatePostsView.as_view(), name='update_post'),
    path('delete_post/<int:pk>', views.DeletePostsView.as_view(), name='delete_post'),
    path('about', views.about, name='about'),
    path('post/<int:pk>/add_comment', views.AddCommentView.as_view(), name='add_comment'),
    
]