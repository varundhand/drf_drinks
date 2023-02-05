from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def drink_list(request, format= None):
  if request.method == 'GET':
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks,many=True) # many serilizes all of data because we have a list(drinks)
    # return JsonResponse({"drinks":serializer.data}, safe=False) # returing json
    return Response(serializer.data)
 
  if request.method == 'POST': # taking the data we get, deSerialize it and create an object out of it 
    serializer =  DrinkSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED) # returing a response object with a status value

@api_view(['GET','PUT','DELETE'])
def drink_detail(request, id,format=None):
  try:
    drink = Drink.objects.get(pk=id)
  except Drink.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = DrinkSerializer(drink)  
    return Response(serializer.data)
  elif request.method == 'PUT': # elif is used so that only one of the them is used 
    serializer = DrinkSerializer(drink, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    drink.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)

  return 
  