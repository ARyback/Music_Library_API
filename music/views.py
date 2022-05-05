from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MusicSerializer
from .models import Music

@api_view(['GET', 'POST'])
def music_list(request):
    if request.method == 'GET':
        music = Music.objects.all()
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MusicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






# from django.shortcuts import get_object_or_404
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import CarSerializer
# from .models import Car

# @api_view(['GET', 'POST'])
# def music_list(request):
#     if request.method == 'GET':
#         dealership_name = request.query__params.get('dealership')
#         #print(dealership_name)
#         queryset = Car.objects.all()
#         if dealership_name:
#             queryset = queryset.filter(dealership__name=dealership_name)
#         serializer = CarSerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CarSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET', 'PUT', 'DELETE'])
# def car_detail(request, pk):
#     car = get_object_or_404(Car, pk=pk)
#     if request.method == 'GET':
#         serializer = CarSerializer(car)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = CarSerializer(car , data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         car.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)