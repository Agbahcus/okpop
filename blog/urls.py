from django.urls import path
from.import views
from.views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserView


urlpatterns = [
   path('',PostListView.as_view(),name='Home'),
   path('user/<str:username>',UserView.as_view(),name='user-post'),
   path('<int:pk>/',PostDetailView.as_view(),name='blog-detail'),
   path('blog/new/',PostCreateView.as_view(),name='blog-create'),
   path('<int:pk>/update/',PostUpdateView.as_view(),name='blog-update'),
    path('<int:pk>/delete/',PostDeleteView.as_view(),name='blog-delete'),
   path('about/',views.about,name='About'),


]