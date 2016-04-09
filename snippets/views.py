from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
	"""
	List all snippets, or create a new snippet.
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update or delete a snippet instance.
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer


class UserList(generics.ListAPIView):
	"""
	List all users
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
	"""
	Retrieve a user instance
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer


