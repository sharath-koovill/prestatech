from django.shortcuts import render
from django.http import HttpResponse
from princessapi.shortestpath import process


def index(request):
    if request.method == 'GET':
        grid = request.GET.get('grid', None)
        grid_size = request.GET.get('grid_size', None)
        args = {}    
        if grid is not None and grid_size is not None:
            grid = grid.split(",")                
            grid_size = int(grid_size)            
            path_data = process(grid, grid_size)
            args['error_flag'] = path_data[0]
            args['paths'] = path_data[1]            
    return render(request, "home.html", args)
