from django.http import JsonResponse
from .models import UploadedFile
import pandas as pd
from django.core.serializers.json import DjangoJSONEncoder
import json


def get_columns(request, file_id):
    file_obj = UploadedFile.objects.get(pk=file_id)
    df = pd.read_csv(file_obj.file.path)
    columns = df.columns.tolist()
    return JsonResponse({"columns": columns})

def get_data(request, file_id, x_column, y_column):
    file_obj = UploadedFile.objects.get(pk=file_id)
    df = pd.read_csv(file_obj.file.path)
    x_data = df[x_column].tolist()
    y_data = df[y_column].tolist()
    return JsonResponse({x_column: x_data, y_column: y_data})


def calculate(request, file_id, column, function_name):
    file_obj = UploadedFile.objects.get(pk=file_id)
    df = pd.read_csv(file_obj.file.path)
    
    if column not in df.columns:
        return JsonResponse({"error": "Invalid column name"})
    
    if function_name == "min":
        result = df[column].min()
    elif function_name == "max":
        result = df[column].max()
    elif function_name == "sum":
        result = df[column].sum()
    else:
        return JsonResponse({"error": "Invalid function name"})
    if isinstance(result, pd.Int64Dtype().type):
        result = int(result)
    return JsonResponse({"result": result})