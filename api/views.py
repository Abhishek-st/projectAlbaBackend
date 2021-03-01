from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db import transaction

from .models import *
from .myserializers import *
from django.db.models import Q
# Create your views here.


class PostMarks(APIView):
    def get(self, request):
        try:
            data = Marks.objects.all().order_by('percent')
            ser = MarkSerializer(data, many=True)
            return Response(ser.data)
        except Exception as e:
            return Response({'msg': str(e) })
    def post(self,request):

        if request.data['physics'] <=100 and request.data['chemistry'] <=100 and request.data['maths'] <=100 and request.data['physics'] >=0 and request.data['chemistry'] >=0 and request.data['maths'] >=0:
            request.data['total'] = request.data['physics'] + request.data['chemistry'] + request.data['maths']
            request.data['percent'] = round(request.data['total'] / 3, 2)
            serializer = MarkSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"msg : marks should be in between 0-100 inclusive"})

class LeaderBoard(APIView):
    def get(self, request):
        try:
            data = Marks.objects.all().order_by('-percent')
            ser = MarkSerializer(data, many=True)
            return Response(ser.data)
        except Exception as e:
            return Response({'msg': str(e) })

    def post(self, request):
        order = request.data['order']
        try:
            data = Marks.objects.all().order_by(order)
            ser = MarkSerializer(data, many=True)
            return Response(ser.data)
        except Exception as e:
            return Response({'msg': str(e) })

class leaderBoardSearch(APIView):
    def post(self, request):
        try:
            data = Marks.objects.filter(Q(name__icontains=request.data['name']) | Q(roll__contains=request.data['name']))
            ser = MarkSerializer(data, many=True)
            return Response(ser.data)
        except Exception as e:
            return Response({'msg': str(e) })
       
