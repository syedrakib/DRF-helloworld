from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from rest_framework import renderers
from rest_framework.response import Response


class SnippetHighlight(generics.GenericAPIView):
	queryset = Snippet.objects.all()
	renderer_classes = (
		renderers.StaticHTMLRenderer,
	)

	def get(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)


class SnippetList(generics.ListCreateAPIView):
	"""
	List all snippets, or create a new snippet.
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = (
		permissions.IsAuthenticatedOrReadOnly,
	)
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update or delete a snippet instance.
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = (
		permissions.IsAuthenticatedOrReadOnly,
		IsOwnerOrReadOnly,
	)


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


