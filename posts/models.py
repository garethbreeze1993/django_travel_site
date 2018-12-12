from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
	author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
	title = models.CharField(max_length = 255)
	image = models.ImageField(blank=True, upload_to = 'images/')
	body = models.TextField()
	like = models.PositiveIntegerField(blank=True, null=True) # decided not to implement like button
	created_date = models.DateTimeField(auto_now = True)
	
	def __str__(self):
		return self.title
		
	def get_absolute_url(self):
		return reverse('posts:post_detail', kwargs = {'pk':self.pk}) # after create post redirect me to the post  have craeted using post_detail/pk
		
	def snippet(self):
		return self.body[:140]
	
	class Meta:
		ordering = ['-created_date']
		#unique_together = ['user','body']
	
	
class Comment(models.Model):
	post = models.ForeignKey('posts.Post',related_name='comments',on_delete=models.CASCADE)
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	body = models.TextField()
	like = models.PositiveIntegerField(blank=True, null= True) # decided not to implement like button
	created_date = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.body
		
	def get_absolute_url(self):
		return reverse('post_list')
		
	class Meta:
		ordering = ['-created_date']	

	

