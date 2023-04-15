# installed modules
import csv
from datetime import timedelta
from rich.console import Console
from rich import print
from rich.panel import Panel
from rich.markdown import Markdown
from rich.text import Text
from rich.prompt import Prompt
from rich.table import Table
import pandas as pd
from datetime import datetime as dt

# files belonging to Superpyne Apple
import today

def buy(name, quantity, price, expiration_date):
    if name == None or quantity == None or price == None or expiration_date == None:
         shelf = Panel(Text("Please give the name, quantity, price and expiration date", justify="center"), style="red")
         print(shelf)
         return
    if expiration_date.date() <= today.currentday():
        shelf = Panel(Text("The product already passed its experation date.", justify="center"), style="red")
        print(shelf)
        return
    while (True):
        bought = Panel(Text(f"you bought {quantity} x {name} for {price} euro per item. The experation date of the product is {expiration_date.date()}.", justify="center"), style="blue") 
        print(bought)
        x = Prompt.ask("Correct? ", choices=["y", "n"] ) 
        if x == "y":
            with open('bought.csv', 'r') as file:
                csv_reader = csv.reader(file)
                id = (len(list(csv_reader))) #this gives an unique id number to an item.
            with open('bought.csv', 'a', newline='') as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow([id, name, quantity, price, today.currentday(), expiration_date.date()])
            with open('instock.csv', 'a', newline='') as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow([id, name, quantity, round(price, 2), today.currentday(), expiration_date.date()])
            added = Panel(Text("oke, product is added", justify="center"), style="green")
            print(added)
            return
        if x == "n":
            notadded = Panel(Text("Allright, product will not be added", justify="center"), style="red")
            print(notadded)
            return

def sell(name, sell_price, quantity): 
    if name == None or quantity == None or sell_price == None:
        shelf = Panel(Text("Please give the name, quantity and sell-price per item", justify="center"), style="red")
        print(shelf)   
        return
    with open("instock.csv", "r") as file:
        csvreader = csv.reader(file)
        product = []
        for file in csvreader: 
            if file[1] == name: 
                product = file
                break
                # For next version: take the product with expiring day wich comes first
        if product == []:
           print(Panel(Text(f"Product not found, try again..", justify="center", style="red"), border_style="red"))
        elif int(product[2]) < quantity:
            print(Panel(Text(f"Amount not in stock, maximum = {product[2]}.", justify="center", style="red"), border_style="red"))
            # For next version: check alsoif there are other rows with same product if the needed amount exceeds stock
        elif int(product[2]) > quantity:
            with open('sold.csv', 'a', newline='') as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow([product[0], name, quantity, today.currentday(), sell_price, product[3]])
                pf = pd.read_csv("instock.csv")
                index = pf.index[pf['name']==name].tolist()
                # print(index)
                pf.loc[index[0], 'quantity'] = float(product[2]) - quantity
                pf.to_csv("instock.csv", index=False)   
                instock = int(product[2]) - quantity
                print(Panel(Text(f"Congratz, you sold {quantity} x {product[1]}. In stock: {instock} ", justify="center", style="green"), border_style="green"))
        elif int(product[2]) == quantity:
            with open('sold.csv', 'a', newline='') as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow([product[0], name, quantity, today.currentday(), sell_price, product[3]])
                pf = pd.read_csv("instock.csv")
                index = pf.index[pf['name']==name].tolist()
                pf1 = pf.drop(index[0], axis=0)
                pf1.to_csv("instock.csv", index=False)   
                print(Panel(Text(f"Congratz, you sold {quantity} x {product[1]}. Product is now sold out, well done", justify="center", style="green"), border_style="green"))


def inventory():
    console = Console()
    with open("instock.csv", 'r') as file:
        df = csv.reader(file)
        richday = today.currentday()
        table = Table(title="Inventory", caption=f"Date: {richday}", width=100)
        count = 0
        for row in df:
            if count == 0: #header in CSV file
                header = row
                for item in header:
                    table.add_column(item, style="green", no_wrap=True)
                count = count + 1
            else:
                table.add_row(row[0], row[1], row[2], row[3], row[4], row[5])
    console.print(table)
    tip = Panel(Text('Tip: use "python main.py backup" to create a backupfile of this list', justify="center"), style="green")
    print(tip)

def backup():
    bulist = list()
    day = today.currentday()
    with open("instock.csv", "r") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            bulist.append(row)
    with open (f"backups/bu_{day}.csv", "w") as file:
        csvwriter = csv.writer(file)
        for item in bulist:
            csvwriter.writerow(item)
    panel = Panel(Text(f"Back-up is created as: bu_{day}.csv" , justify="center", style="green"), border_style="green")
    print(panel)     

def advance_time(amount):
    newday = today.currentday() + timedelta(days=amount)
    newdaystr = newday.strftime("%Y-%m-%d")
    with open("date.txt", 'w') as file:
        file.write(newdaystr)
    date = newday.strftime("%d-%m-%Y")
    panel = Panel(Text(f"New day is: {date}", justify="center", style="green"), border_style="yellow")
    print(panel)


def readme():
    console = Console()
    readme = open("Readme.md", "r")
    markdown = Markdown(readme.read())
    console.print(markdown)


def userguide():
    console = Console()
    userguide = open("Userguide.md", "r")
    markdown = Markdown(userguide.read())
    console.print(markdown)

def profit(date1, date2):
    if date1 == None or date2 == None:
         shelf = Panel(Text("You have to fill a minimumdate and maximumdate", justify="center"), style="red")
         print(shelf)
         return
    buypricelist = []
    revenuelist = []
    expiredlist = []
    profit = 0
    buyprice = 0
    revenue = 0
    expired = 0
    with open("sold.csv", "r") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if row[4] == "sell_price":
                pass
            else:
                datum = dt.strptime(row[3], '%Y-%m-%d')
                if datum >= date1 and datum <= date2:
                    revenuelist.append(float(row[4]) * float(row[2]))
                    revenue = sum(revenuelist[0:])
                    buypricelist.append(float(row[5]) * float(row[2]))
                    buyprice = sum(buypricelist[0:])
                    profit = revenue - buyprice
    with open("expired.csv", "r") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if row[3] == "buy_price":
                pass
            else:
                datum = dt.strptime(row[5], '%Y-%m-%d')
                if datum >= date1 and datum <= date2:
                    expiredlist.append(float(row[2]) * float(row[3]))
                    expired = sum(expiredlist[0:])
    profit = revenue - buyprice - expired
    revenuetext = Panel(Text(f"Revenue over the period {date1.strftime('%d-%m-%Y')} and {date2.strftime('%d-%m-%Y')} was {('%.2f' %revenue)} euro", justify="center"), style="green")
    print(revenuetext)
    costs = Panel(Text(f"Total buyprice was {('%.2f' %buyprice)} euro", justify="center"), style="green")
    print(costs)
    if expired > 0:
        lost = Panel(Text(f"Total loss due to expired products was {('%.2f' %expired)} euro in this period", justify="center"), style="green")
        print(lost)
    if profit >= 0:
        finalprofit = Panel(Text(f"Total profit was {('%.2f' %profit)} euro", justify="center"), style="green")
        print(finalprofit)
    if profit < 0:
        finalprofit = Panel(Text(f"Total profit was {('%.2f' %profit)} euro", justify="center"), style="red")
        print(finalprofit)
    return revenue

