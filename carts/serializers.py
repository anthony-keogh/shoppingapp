from rest_framework import serializers
from snippets.forms import Snippet

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['cart']