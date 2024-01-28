import csv
from django.shortcuts import render
from rest_framework.decorators import api_view,parser_classes
from rest_framework.parsers import FileUploadParser
from .serializers import FileSerializer
from rest_framework.response import Response
# Create your views here.
@api_view(['POST'])
@parser_classes([FileUploadParser])
def upload_file(request):
    fileSerializer = FileSerializer(data=request.data)
    if fileSerializer.is_valid():
        fileSerializer.save()
        csv_file = request.FILES.get("csv_file")
        file_path = r"C:\Users\AVISHEK\Downloads\{}".format(csv_file.name)
        with open(file_path, 'wb') as destination:
            for chunk in csv_file.chunks():
                destination.write(chunk)
        with open(file_path,"r") as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                print(row)
        return Response(fileSerializer.data)
    else:
        return Response(fileSerializer.errors)
