from django.shortcuts import render,get_object_or_404
from .models import Blog
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
	)


class PostListView(ListView):
	model=Blog 
	template_name='blog/index.html'  	#<app>/<model>_<viewtype>.html
	context_object_name="blog"
	ordering=['-date_posted']
	paginate_by=4


class UserView(ListView):
	model=Blog 
	template_name='blog/userpost.html'  	#<app>/<model>_<viewtype>.html
	context_object_name="blog"
	ordering=['-date_posted']
	paginate_by=4

	def get_queryset(self):
		user=get_object_or_404(User,username=self.kwargs.get('username'))
		return Blog.objects.filter(author=user).order_by("-date_posted")


class PostDetailView(DetailView):

	model=Blog
	
	

class PostCreateView(LoginRequiredMixin,CreateView):
	model=Blog
	fields=['title','content']
	
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model=Blog
	fields=['title','content']
	
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		blog=self.get_object()
		if self.request.user ==blog.author:
			return True
		return False

	
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):

	model=Blog
	success_url = '/'
	def test_func(self):
		blog=self.get_object()
		if self.request.user ==blog.author:
			return True
		return False

def about(request):
	return render(request,'blog/about.html')



