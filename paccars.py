from pyvin import VIN
import csv
import os
import requests


def veh_info(_vin):
    vehicle = VIN(_vin)
    make = vehicle.Make
    model = vehicle.Model
    year = vehicle.ModelYear
    return make, model, year


req = 'https://www.skyonics.net/api/proxy/APIDeviceCommands/CommandDevice?APIKey=563o77hmgg6e7fszb2hzooh7qy&serialNumber=87B010620129&mode=0'
# filename = open('vehicles.csv', 'rw')
# file = csv.DictReader(filename)
#
# truck_list = list(file)

# for record in truck_list:
#     # truck.append(record['vin'])
#     # print(record['vin'])
#     # print(veh_info(record['vin']), record['serialNum'])
#     record['make'], record['model'], record['year'] = veh_info(record['vin'])
tmpFile = 'tmp.csv'
with open('vehicles.csv', 'r') as inputFile, open(tmpFile, 'w') as outFile:
    read_file = csv.reader(inputFile, delimiter=',')
    write_file = csv.writer(outFile, delimiter=',')
    header = next(read_file)
    write_file.writerow(header)

    for row in read_file:
        # print(veh_info(row[3]), row[5])
        # print(row)
        row[1], row[2], row[4] = veh_info(row[3])
        # for col in row:
        #     write_file.writerow(veh_info(row[3]))
        write_file.writerow(row)
        print(row)
os.rename(tmpFile, 'vehicles.csv')
