from pyvin import VIN
import csv
import os
import requests
import time


headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
data = "'DIAG ELD'"
tokens = []
elds = []


def veh_info(_vin):
    vehicle = VIN(_vin)
    make = vehicle.Make
    model = vehicle.Model
    year = vehicle.ModelYear
    return make, model, year


def list_csv():
    with open('vehicles.csv', 'r') as file:
        c_list = []
        reader = csv.reader(file)
        firstline = True
        for row in reader:
            c_list.append(row)
            if firstline:
                firstline = False
                continue
            elds.append(row[5])
    return c_list


csv_list = list_csv()

def p_req():
    for item in csv_list[1:]:
        if item[5][0:2] == '4C':
            print("Pacific device")
            item.append('/')
            tokens.append(None)
            continue
        else:
            purl = f'https://www.skyonics.net/api/skyonics/devicecommand?APIKey=563o77hmgg6e7fszb2hzooh7qy&serialNumber={item[5]}&mode=0'
            req = requests.post(purl, headers=headers, data=data)
            if req.status_code == 200:
                print(f"Request sent for {item[5]}. Received token: {req.text}")
                tokens.append(req.text.strip('"'))
            elif req.status_code == 401:
                print(f"{item[5]} is not on L8 skyonics")
                tokens.append(None)
                item.append("Not on L8 skyonics")
            else:
                print(f"Oops something went wrong with {item[5]}. Error {req.status_code}")
                tokens.append(None)
                item.append("Error getting data")


p_req()
print("wait 150 seconds")
time.sleep(150)


def g_req():
    c = 1
    for tok in tokens:
        if tok is None:
            c += 1
            continue
        else:
            gurl = f'https://www.skyonics.net/api/skyonics/devicecommand?APIKey=563o77hmgg6e7fszb2hzooh7qy&token={tok}'
            req = requests.get(gurl, headers=headers, data=data)
            if req.status_code == 200:
                if 'O' in req.text.replace(',', ' ').replace(',', ' ').split():
                    print(f"{elds[c-1]} has OBD odometer")
                    csv_list[c].append("YES")
                else:
                    print(f"{elds[c - 1]} OBD odometer missing")
                    csv_list[c].append("NO")
            else:
                print(f"Oops something went wrong. Error {req.status_code}")
                csv_list[c].append("Error getting data")
        c += 1


g_req()
tmp = "tmp.csv"


def decode_vin():
    for i in csv_list[1:]:
        i[1], i[2], i[4] = veh_info(i[3])


decode_vin()


def write_csv():
    with open(tmp, 'w') as file:
        csv_list[0].append("OBD odometer")
        wfile = csv.writer(file, delimiter=',')
        for row in csv_list:
            wfile.writerow(row)
            print(row)
    os.rename(tmp, "vehicles.csv")


write_csv()
