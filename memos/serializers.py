from rest_framework import serializers
from memos.models import Memo

class MemoSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only = True)
	title = serializers.CharField(required = True, max_length = 200)
	text = serializers.CharField(required = True)
	words = serializers.IntegerField()

	def create(self, validated_data):
		return Memo.objects.create(**validated_data)
