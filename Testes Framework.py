from operator import itemgetter

input_file = open('b_should_be_easy.in')
first_line = input_file.readline()

n_rows, n_columns, n_vehicles, n_rides, bonus, max_steps = tuple(map(int, first_line.split(' ')))


def greatest_distance():
    return n_columns * n_rows


def travel_distance(start, finish):
    return abs(start[0] - finish[0]) + abs(start[1] - finish[1])


def make_trip_list():
    trips = list()

    for i in range(n_rides):
        trips.append([i] + input_file.readline().rstrip().split())
        # trips.append(str(i) + ' ' + input_file.readline().rstrip())
        # trip_list.append(''.join(str(x) for x in input_file.readline().rstrip()))

    for i in range(n_rides):
        # trips[i] = [int(x) for x in trips[i] if x.isnumber()]
        trips[i][1:7] = map(int, trips[i][1:7])
    return trips


# print(make_trip_list())
trip_list = make_trip_list()
print(trip_list)
# for r in range(n_rows):
#     trip_list.append(input_file.readline().rstrip())
#
# print(input_file.readline())

# n_cars = 0
fleet = []
cars_list = []

for car in range(n_vehicles):  # Inicializa a array de carros, todos na posicao (0,0) com valor false
    cars_list.append([car, (0, 0), False])

# sorted(trip_list, key=itemgetter(1))
trip_list.sort(key=itemgetter(5))

for r in range(n_rides):
    current_step = 0
    # trip_id, begin_row, begin_col, end_row, end_col, earliest_start, latest_finish = tuple(map(int, trip_list[r].split(' ')))

    trip_id = trip_list[r][0]
    begin_row = trip_list[r][1]
    begin_col = trip_list[r][2]
    end_row = trip_list[r][3]
    end_col = trip_list[r][4]
    earliest_start = trip_list[r][5]
    latest_finish = trip_list[r][6]

    begin = (int(begin_row), int(begin_col))
    end = (int(end_row), int(end_col))

    print(begin, end)

    # while current_step < max_steps:
    #     distance = travel_distance(begin, end)
    #
    #     if begin[0] != end[0]:
    #         begin[0] += 1
    #     else:
    #         begin[1] += 1

    # if travel_distance(begin, end) == greatest_distance():

    # current_step += 1

print(trip_list)
