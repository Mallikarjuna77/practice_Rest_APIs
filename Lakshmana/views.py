from rest_framework import status
from rest_framework.decorators import api_view
from .models import Admin
from .serializers import AdminSerializer, DeptSerializer
from rest_framework.response import Response

@api_view(['GET'])
def details(request):
    action=Admin.objects.all()
    serializer=AdminSerializer(action, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    home=AdminSerializer(data=request.data)
    if home.is_valid():
        Admin=home.save()
    request.data['Branch']=Admin.id
    A=DeptSerializer(data=request.data)
    if A.is_valid():
        A.save()
        return Response({'Status':'Success', 'data':'serializer.data'}, status=status.HTTP_200_OK)
    else:
        return Response({'Status':'Error', 'data':'serializer.errors'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update(request, id):
    apidetails=Admin.objects.get(id=id)
    serializer=AdminSerializer(instance=apidetails, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'Status': 'Success'}, status=status.HTTP_200_OK)
    else:
        return Response({'Status': 'Error'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def pupdate(request, id):
    detailsup=Admin.objects.get(id=id)
    serializer=AdminSerializer(instance=detailsup, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status':'Success'}, status=status.HTTP_200_OK)
    else:
        return Response({'Status':'Error'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete(request, id):
    details=Admin.objects.get(id=id)
    details.delete()
    return Response({'status':'Item deleted'})









