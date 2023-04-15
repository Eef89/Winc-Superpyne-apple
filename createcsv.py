import os
import csv
from rich.panel import Panel
from rich.text import Text
from rich import print

def create_csv_files():
    path_bought_file = os.path.join(os.getcwd(),'bought.csv')
    path_sold_file = os.path.join(os.getcwd(),'sold.csv')
    path_stock_file = os.path.join(os.getcwd(),'instock.csv')
    path_expired_file = os.path.join(os.getcwd(),'expired.csv')
    path_backup_folder = os.path.join(os.getcwd(),'backups')
    if os.path.exists(path_bought_file):
         pass
    else:
        with open('bought.csv', 'a') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(['id', 'name', 'quantity', 'buy_price', 'buy_date', 'experation_date'])
        panel = Panel(Text(f"File created: bought.csv" , justify="center", style="green"), border_style="green")
        print(panel)   
    if os.path.exists(path_sold_file):
         pass
    else:
        with open('sold.csv', 'a') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(['id', 'name', 'quantity', 'sell_date', 'sell_price', 'buy_price'])
        panel = Panel(Text(f"File created: sold.csv" , justify="center", style="green"), border_style="green")
        print(panel) 
    if os.path.exists(path_stock_file):
         pass
    else:
        with open('instock.csv', 'a') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(['id', 'name', 'quantity', 'buy_price', 'buy_date', 'experation_date'])
            panel = Panel(Text(f"File created: instock.csv" , justify="center", style="green"), border_style="green")
            print(panel) 
    if os.path.exists(path_expired_file):
         pass
    else:
        with open('expired.csv', 'a') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(['id', 'name', 'quantity', 'buy_price', 'buy_date', 'experation_date'])
            panel = Panel(Text(f"File created: expired.csv" , justify="center", style="green"), border_style="green")
            print(panel) 
    if os.path.exists(path_backup_folder):
         pass
    else:
            os.mkdir(path_backup_folder)
        