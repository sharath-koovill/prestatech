def find_shortest_path(s, e, grid):    
    queue = [(s, [])]
    visited = create_visit_grid(5)
    path_list = []
    
    while len(queue) > 0:
        node, path = queue.pop(0)
        path.append(node)
        visited[node[0]][node[1]] = True
        
        if node == e:
            path_list.append(path)

        adj_nodes = get_neighbors(node, grid)
        
        for item_node in adj_nodes:
            if not visited[item_node[0]][item_node[1]]:                
                queue.append((item_node, path[:]))

    return path_list

def find_position(symbol, grid):
    positions = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == symbol:
                positions.append((i,j))
    return positions

def create_visit_grid(n):
    visited = []
    visited_grid = []
    for i in range(n):
        visited.append(False)
    for i in range(n):
        visited_grid.append(visited[:])     
    return visited_grid

def get_neighbors1(node, grid):    
    rows = len(grid)
    cols = rows
    for i in range(max(0, node[0] - 1), min(rows, node[0] + 2)):
        for j in range(max(0, node[1] - 1), min(cols, node[1] + 2)):
            if (i, j) != node:
                print(node,i,j)
                yield (i, j)

def get_neighbors(node, grid):    
    rows = len(grid)
    cols = rows
    neighbors = []
    for i in range(max(0, node[0] - 1), min(rows, node[0] + 2)):
        for j in range(max(0, node[1] - 1), min(cols, node[1] + 2)):            
            if (i, j) != node and grid[i][j]!='x' and \
            ((i == node[0] and j in [node[1]-1, node[1]+1]) or (i in [node[0]-1, node[0]+1] and j == node[1])):
                neighbors.append((i, j))
    return neighbors

def get_direction(path):
    previous = path[0]
    direction = []
    for i in range(1, len(path)):
        current = path[i]
        if(current[0] == previous[0] and current[1] > previous[1]):
            direction.append("RIGHT")
        elif(current[0] == previous[0] and current[1] < previous[1]):
            direction.append("LEFT")
        elif(current[0] < previous[0] and current[1] == previous[1]):
            direction.append("UP")
        elif(current[0] > previous[0] and current[1] == previous[1]):
            direction.append("DOWN")
        previous = current
    return tuple(direction)

def validate_grid(grid, n):    
    if not len(grid) == n and not len(grid[0]) == n:
        return "TRUE"
    return "FALSE"

def process(grid, grid_size):    
    mario = "m"
    princess = "p"
    obstacle = "x"
    free_cell = "-"

    not_valid = validate_grid(grid, grid_size)
    if not_valid == "TRUE":
        return not_valid, []

    mario_position = find_position(mario, grid)
    princess_position = find_position(princess, grid)

    if len(mario_position) != 1 or len(princess_position) != 1:
        return "TRUE", []    
    paths = find_shortest_path(mario_position[0], princess_position[0], grid)    
    path_list = []
    for each_path in paths:
        path_list.append(get_direction(each_path))
    
    return "FALSE", path_list
