input_file = open('b_should_be_easy.in')
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


# print(make_trip_list())
trip_list = make_trip_list()
print(trip_list)
# for r in range(n_rows):
#     trip_list.append(input_file.readline().rstrip())
#
# print(input_file.readline())

n_cars = 0
fleet = []

for r in range(n_rides):
    current_step = 0
    trip_id, begin_row, begin_col, end_row, end_col, earliest_start, latest_finish = tuple(map(int, trip_list[r].split(' ')))

    begin = (begin_row, begin_col)
    end = (end_row, end_col)
    
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