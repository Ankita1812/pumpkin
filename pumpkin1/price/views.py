from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from price.serializers import PumpkinSerializer
from django.contrib.auth.models import User
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PumpkinSerializer
from .models import Pumpkin, mydb
from rest_framework.renderers import TemplateHTMLRenderer
import datetime

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="anki",
  passwd=""
)
mycursor = mydb.cursor()
class CreateView(generics.ListAPIView):
	queryset = Pumpkin.objects.all()
	serializer_class = PumpkinSerializer

	def perform_create(self, serializer):
		serializer.save()

def get_max(request):
	a=Pumpkin.objects.all()
	return a.max.highp
def get_min(request):
	a=Pumpkin.objects.all()
	return a.min.lowp

# ViewSets define the view behavior.
class getPrice(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'static/read.html'

	def get_Price_Bydate(self,request):
		'''mycursor = mydb.cursor()
		mycursor.execute("SELECT * FROM atlanta1")
		mycursor.execute("SELECT * FROM atlanta1 WHERE date =10/15/2016")
		myresult = mycursor.fetchall()
		'''
		renderer_classes = [TemplateHTMLRenderer]
		template_name = 'static/read.html'

		city = self.request.query_params.get('city', None)
		date = self.request.query_params.get('date', None)

		if city is not None and date is not None:
			data = Pumpkin.objects.filter(city=city, date=date)
			serializer = PumpkinSerializer(data, many=True)
			serializer.save()
			mycursor.execute("SELECT * FROM abc/ WHERE city=city AND date=date")
			myresult = mycursor.fetchall()
			return Response({"Pumpkins": serializer.myresult})

	def max_price(self, request):
		renderer_classes = [TemplateHTMLRenderer]
		template_name = 'static/max.html'

		city = self.request.query_params.get('city', None)
		date = self.request.query_params.get('date', None)

		if city is not None and date is not None:
			max = Pumpkin.objects.filter(city=city, date=date)
			get_max(max)
			serializer = PumpkinSerializer(max)
			serializer.save()
			return Response({"PumpkinsMax": serializer.max})

	def min_price(self, request):
		renderer_classes = [TemplateHTMLRenderer]
		template_name = 'static/min.html'

		city = self.request.query_params.get('city', None)
		date = self.request.query_params.get('date', None)

		if city is not None and date is not None:
			min = Pumpkin.objects.filter(city=city, date=date)
			get_min(min)
			serializer = PumpkinSerializer(min)
			serializer.save()
			return Response({"PumpkinsMin": serializer.min})



