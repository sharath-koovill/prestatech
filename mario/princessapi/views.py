from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import sqlalchemy, sqlalchemy.orm

from .shortestpath import process
from .serializers import path_serializer
from .models import Base, ShortestPathRequest
from mario import settings

engine = sqlalchemy.create_engine("sqlite:///" + str(settings.DATABASES['default']['NAME']))
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

def get_shortest_path(request):
    """
    This function returns the ERROR and PATHS based on the grid and grid size
    """
    grid = request.GET.get('grid', None)
    grid_size = request.GET.get('grid_size', None)
    
    results = None    
    try:
        grid = grid.split(",")                
        grid_size = int(grid_size)
        
        path_data = process(grid, grid_size)
        shortest_path = ShortestPathRequest(grid=str(grid), grid_size=grid_size, request_time=str(datetime.now()))
        session.add(shortest_path)
        session.commit()
        
        path_data_json = [{'error_flag': path_data[0], 'paths':path_data[1]}]        
        results = path_serializer(path_data_json, many=True).data
    except Exception as e:
        print(e)
        return JsonResponse({'error_flag': 'TRUE', 'paths':''}, status=400)
    return JsonResponse(results, safe=False)
