from time import sleep
from urllib import request
import json
from datetime import date, timedelta

today = date.today()
num = 30

def findV():
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=453&date="

    days = today

    for _ in range(0, num):
        day = days.strftime("%d-%m-%Y")
        print("------------" + day + "---------------")

        respone = request.Request(url+day)
        respone.add_header("User-Agent", "")
        respone.add_header("accept", "application/json")
        respones = request.urlopen(respone)

        if str(respones.status) == "200":
            data = json.loads(respones.read())

            data = data['centers']
            
            for center in data:
                # print(center)
                sessions = center['sessions']

                for session in sessions:
                    if session['min_age_limit'] == 18 and session['available_capacity_dose2'] > 0:
                        print("Ayush Ayush \n----------------------")
                        print("CENTER AVALIABLE IS " + center['name'])
                        print("Address = " + center['address'] +", " + str(center['pincode']))
                        print("Vaccine is " + session['vaccine'])
                        print("CHECK FOR MORE DETAILS \n")

                    elif session['available_capacity_dose2'] > 0 and session['vaccine'] == "COVISHIELD":
                        print("MAMMA AND DADDY!! \n----------------------")
                        print("CENTER AVALIABLE IS " + center['name'])
                        print("Address = " + center['address'] +", " + str(center['pincode']))
                        print("CHECK FOR MORE DETAILS \n")

        else:
            print("\n-----------------------------------------------\n FAILED, CHECK URL\n ---------------------------------------------\n")
            exit()

        days = days + timedelta(1)

        

if __name__ == "__main__":
    import sys
    execTime = 1

    if len(sys.argv) >= 2:
        try:
            execTime = int(sys.argv[1])
            print(execTime)
        except:
            print("Didn't provide int so only executing once\n-------------------------------------------------\n")

    for i in range(execTime):
        findV()
        if i + 1 != execTime:
            sleep(600)
