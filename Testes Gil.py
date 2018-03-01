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

def availableCar():
    for car in cars_list:
        if (car[2] == False):
            return car[0]
    return "false"

def AssignNextTrip(carNumber, tripNumber, start, finish):
    for car in cars_list:
        if(car[0] == carNumber):

            car[2] = True;
            car[1] = travel_distance(start, finish)
            car[3] = finish

            for line in output_file: #escrever no ficheiro de output o tripNumber
                if (line[0] == carNumber):
                    line.append(tripNumber)
                    return
            return

def NextTrip(trips):
    if (len(trips) != 0):
        nextTrip = trips[0]
        del trips[0]
        return nextTrip
    else:
        return False


def UpdateSteps():
    for car in cars_list:
        if(car[2] == True): #se a andar diminui steps
            car[1] -= 1
        if(car[1] <= 0): #se steps a 0 coloca a falso
            car[2] = False

# print(make_trip_list())
trip_list = make_trip_list()
# for r in range(n_rows):
#     trip_list.append(input_file.readline().rstrip())
#
# print(input_file.readline())

# n_cars = 0
fleet = []
cars_list = []
output_file = []

for car in range(n_vehicles):  # Inicializa a array de carros, todos na posicao (0,0) com valor false
    cars_list.append([car, 0, False, (0,0)]) #numero carro, steps until available, disponibilidade

for car in range(n_vehicles):  # Inicializa o output file
    output_file.append([car])

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

    #print(begin, end)

    # while current_step < max_steps:
    #     distance = travel_distance(begin, end)
    #
    #     if begin[0] != end[0]:
    #         begin[0] += 1
    #     else:
    #         begin[1] += 1

    # if travel_distance(begin, end) == greatest_distance():

    # current_step += 1

# while(availableCar() != "false"): #Verifies there is a car available
#     car = availableCar()
#     tripNumber = NextTripNumber(trip_list)
#     AssignNextTrip(car, tripNumber) #adicionar viagem, alterar valores dentro do carro
#     tripNumber += 1


for i in range(0, max_steps):
    while (availableCar() != "false" and NextTrip(trip_list) != False):  # Verifies there is a car available
        car = availableCar()
        nextTrip = NextTrip(trip_list)

        tripNumber = nextTrip[0]
        start = (nextTrip[1],nextTrip[2])
        finish = (nextTrip[3],nextTrip[4])

        AssignNextTrip(car, tripNumber, start, finish)  # adicionar viagem, alterar valores dentro do carro
    UpdateSteps()