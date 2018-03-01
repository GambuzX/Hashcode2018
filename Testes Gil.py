n_vehicles = 12
car_list = [[0, (1,1), False] , [1, (0,0), False]]
output_file = []

for car in range(n_vehicles): #Inicializa o output file
    output_file.append([car])

def availableCar():
    for car in car_list:
        if (car[2] == False):
            return car[0]
    return False

def AssignNextTrip(carNumber, tripNumber):
    for car in car_list:
        if(car[0] == carNumber):
            car[2] = True;
            for line in output_file: #escrever no ficheiro de output o tripNumber
                if (line[0] == carNumber):
                    line.append(tripNumber)
                    return
            return

tripNumber = 0
while(availableCar()): #Verifies there is a car available
    car = availableCar()
    AssignNextTrip(car, tripNumber) #adicionar viagem, alterar valores dentro do carro
    tripNumber += 1


print(output_file)
print(car_list)
