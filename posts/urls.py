from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns = [
	path('create/', views.CreatePost.as_view(), name='post_create'),
	path('<int:pk>/delete', views.DeletePost.as_view(), name='post_delete'),
	path('<int:pk>', views.PostDetail.as_view(), name='post_detail'),
	path('<int:pk>/edit', views.PostUpdate.as_view(), name='post_update'),
	path("by/<username>/",views.UserPosts.as_view(),name="for_user"), # all the posts listed by that user in listview class
	path('<int:pk>/comment/add', views.add_comment_to_post, name='add_comment'),
	path('results/', views.Search_Posts.as_view(), name="search_posts"),
	path('<int:pk>/comment/remove', views.comment_remove, name='remove_comment'),


	
]
