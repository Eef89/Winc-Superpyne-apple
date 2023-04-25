from datetime import date, datetime as dt
import os
import csv
from rich import print
from rich.panel import Panel
from rich.text import Text

def create_datefile():
    path_date_file = os.path.join(os.getcwd(),'date.txt')
    if os.path.exists(path_date_file):
         pass
    else:
        today = date.today()
        newdaystr = today.strftime("%Y-%m-%d")
        with open("date.txt", 'a') as file:
            file.write(newdaystr)

def currentday():
    leesdatum = open("date.txt", 'r')
    vandaag = dt.strptime(leesdatum.readline(11), '%Y-%m-%d')
    return vandaag.date()

def isexpired(): #This function deletes products from the stocklist after advancing time when they are expired. To remember to losses, the lost itesm are added in the expired.csv.
    ls = list()
    ls_expired = list()
    with open ("instock.csv", "r") as file:
        dude = csv.reader(file)
        count = 0
        expired_products = 0
        lost = float(0)
        for row in dude:
            if count == 0:
                ls.append(row)
                ls_expired.append(row)
                count += 1
            else:
                expiringdate = dt.strptime(row[5], '%Y-%m-%d')
                if expiringdate.date() > currentday():
                    ls.append(row)
                if expiringdate.date() < currentday():
                    ls_expired.append(row)
                    expired_products += 1
                    lost += (float(row[3]) * float(row[2]))
        if expired_products == 1:
            panel = Panel(Text(f"There was {expired_products} expired product. It deleted from the list. You lost about {lost} euro's.", justify="center", style="green"), border_style="red")
            print(panel)  
        if expired_products > 1:
            panel = Panel(Text(f"There were {expired_products} expired products. They are deleted from the list. You lost about {lost} euro's.", justify="center", style="green"), border_style="red")
            print(panel)  
    with open ("instock.csv", "w") as file:
        writer = csv.writer(file)
        for item in ls:
            writer.writerow(item)
    with open ("expired.csv", "a") as file:
        counter = 0
        writer = csv.writer(file)
        for item in ls_expired:
            if counter == 0:
                counter += 1
                pass
            else:
                writer.writerow(item)
                counter += 1
#  python main.py set-date -dt 01012023

def set_date(datum):
    newdate = datum.date()
    newdaystr = newdate.strftime("%Y-%m-%d")
    with open("date.txt", 'w') as file:
        file.write(newdaystr)
    panel = Panel(Text(f"New day is: {datum.strftime('%d-%m-%Y')}", justify="center", style="green"), border_style="yellow")
    print(panel)
