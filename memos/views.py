from django.shortcuts import render
from .models import Memo
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json
from collections import Counter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from memos.serializers import MemoSerializer

def Index(request):
	memos = Memo.objects.all().order_by('words')
	return render(request, 'memos/base.html', {
		'notes': memos,
	})

@api_view(['GET', 'POST'])
def memos(request):
	if request.method == 'GET':
		memos = Memo.objects.all().order_by('words')
		serializer = MemoSerializer(memos, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		data['words'] = len(Counter(data['text'].lower().split()))
		serializer = MemoSerializer(data=data)
		serializer.create(data)
		memos = Memo.objects.all().order_by('words')
		res = MemoSerializer(memos, many=True)
		return Response(res.data)

@api_view(['POST'])
def memo_del(request):
	data = JSONParser().parse(request)
	try:
		memo = Memo.objects.get(pk = data['id'])
		memo.delete()
		memos = Memo.objects.all().order_by('words')
		serializer = MemoSerializer(memos, many=True)
		return Response(serializer.data)
	except Memo.DoesNotExist:
		return Response(status = 404)
