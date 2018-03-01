input_file = open('a_example.in')
first_line = input_file.readline()

n_rows, n_columns, n_vehicles, n_rides, bonus, max_steps = tuple(map(int, first_line.split(' ')))

grid = []

for r in range(n_rows):
    grid.append(input_file.readline().rstrip())

for r in range(n_rides):
    current_step = 0
    begin = (grid[r][0], grid[r][1])
    end = (grid[r][2], grid[r][3])
    earliest_start = grid[r][4]
    latest_finish = grid[r][5]

    while current_step < max_steps:
        distance = travelDistance(begin, end)
        current_step += 1





# display output

print(grid)