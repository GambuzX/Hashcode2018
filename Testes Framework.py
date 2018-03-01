input_file = open('a_example.in')
first_line = input_file.readline()

n_rows, n_columns, n_vehicles, n_rides, bonus, max_steps = tuple(map(int, first_line.split(' ')))


def greatest_distance():
    return n_columns * n_rows


def travel_distance(start, finish):
    return abs(start[0] - finish[0]) + abs(start[1] - finish[1])


def make_trip_list():
    trip_list = list()

    for i in range(n_rides):
        trip_list.append(str(i) + ' ' + input_file.readline().rstrip())
        # trip_list.append(''.join(str(x) for x in input_file.readline().rstrip()))
    return trip_list


print(make_trip_list())

grid = []

for r in range(n_rows):
    grid.append(input_file.readline().rstrip())

print(grid)

n_cars = 0
fleet = []

for r in range(n_rides):
    current_step = 0
    begin = (grid[r][0], grid[r][1])
    end = (grid[r][2], grid[r][3])
    earliest_start = grid[r][4]
    latest_finish = grid[r][5]

    while current_step < max_steps:
        distance = travel_distance(begin, end)

        if begin[0] != end[0]:
            begin[0] += 1
        else:
            begin[1] += 1

        # if travel_distance(begin, end) == greatest_distance():


        current_step += 1



print(grid)