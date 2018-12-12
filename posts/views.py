from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy
from posts.models import Post, Comment
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from posts.forms import PostForm, CommentForm

from django.contrib.auth import get_user_model
User = get_user_model()


class PostList(ListView):
	model = Post
	# may add queryset 
	
class CreatePost(LoginRequiredMixin,CreateView):
	model = Post
	form_class = PostForm
# this bit of code gets the current user logged in and creating the post and sets it to post.author  
	def form_valid(self,form):
		self.object = form.save(commit=False)
		self.object.author = self.request.user # connect post to a user
		self.object.save()
		return super().form_valid(form) # super connects to class you inherit from so maybe generic.createview		

class DeletePost(LoginRequiredMixin,DeleteView):
	model = Post
	success_url = reverse_lazy('post_list')

	#def get_queryset(self):
	#	queryset = super().get_queryset()
	#	return queryset.filter(user_id=self.request.user_id)
		
class PostDetail(DetailView):
	model = Post
	
	# may add get_queryset
	
class PostUpdate(LoginRequiredMixin,UpdateView):
	model = Post
	form_class = PostForm
	template_name_suffix = '_update_form'
	
class UserPosts(ListView):
	
	model = Post
	template_name = 'posts/user_posts.html'
	
	def get_queryset(self):
		try:
			self.post_user = User.objects.prefetch_related("posts").get(
                username__iexact=self.kwargs.get("username")
            )	
		except User.DoesNotExist:
			raise Http404
		else:
			return self.post_user.posts.all()
			
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['post_user'] = self.post_user
		return context
		
		
class Search_Posts(PostList):
	paginate_by = 10
	template_name = 'posts/post_list.html'
	
	def get_queryset(self):
		result = super(Search_Posts,self).get_queryset()
		
		query = self.request.GET.get('q')
		
		results = Post.objects.filter(Q(title__icontains=query))
		
		return results



@login_required
def add_comment_to_post(request,pk):

	post = get_object_or_404(Post, pk=pk)
	
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post= post
			comment.author = request.user
			comment.save()
			return redirect('posts:post_detail', pk=post.pk)
	else:
		form = CommentForm()
	return render(request, 'posts/comment_form.html', {'form':form})
	
@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk # we are deleting this comment so need to grab the pk from the comment before deleting so we can use it in redirect
    comment.delete()
    return redirect('posts:post_detail', pk=post_pk)
	
		
			
	