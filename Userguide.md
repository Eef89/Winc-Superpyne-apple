# Userguide

Thank you for using Superpyne apple!

## Requirements

This programm uses the following modules:
1. rich
2. pandas
3. Os
4. CSV
5. Argparse
6. datetime


## Position arguments
### Buy

Following arguments are mandatory for buying a product:
1. Name: -n or --name
2. Price: -p or --price
3. Quantity: -q or --quantity
4. Experation: date -ed or --experation_date use ddmmyyyy

Examples:
```
python main.py buy -n strawberry -p 12 -q 100 -ed 01012029
python main.py buy -n monkey -p 12 -q 100 -ed 01012999
python main.py buy -n appel -q 100 -p 13.5 -ed 01012025
python main.py buy -n peer -q 50 -p 18.5 -ed 01052023
python main.py buy -n luiers -q 50 -p 10.53 -ed 01052099
python main.py buy -n wceend -q 50 -p 10.53 -ed 01052099
```

### Sell

Following arguments are mandatory for selling a product:
1. Name: -n or --name
2. Sellprice: -sp or --sell_price
3. Quantity: -q or --quantity

Examples:

```
python main.py sell -n aardbei -q 5 -sp 13
python main.py sell -n appel -q 75 -sp 13.5 
python main.py sell -n peer -q 25 -sp 18.5 
python main.py sell -n luiers -q 12 -sp 10.53 
python main.py sell -n wceend -q 10 -sp 10.53 
```

### Inventory

No further arguments are needed.

Examples:

```
python main.py inventory
```

### Profit

Following arguments are mandatory to calculate the profit over a period:
1. Minimum date: -min or --mindate
2. maximum: -max or --maxdate

Example:
```
python main.py profit -min 01012000 -max 01013000
```

### Advance-time

Following argument is mandatory to shift the time:
1. Days: -d or --days

Examples:
```
python main.py advance-time -d 2
python main.py advance-time -d 200
python main.py advance-time -d 2000
```

### Set-date

Following argument is mandatory to set the date:
1. Date: -dt or --date

Examples:
```
python main.py set-date -dt 01012024
python main.py set-date -dt 01013000 (Be carefull, it can be that all your items will be expired after filling in this example!)
```

### Backup

This function creates a backup file of the instock.csv file

No further arguments are needed.

Example:
```
python main.py backup
```

### Readme

No further arguments are needed.

Example:
```
python main.py readme
```

### Userguide

No further arguments are needed.

Example:
```
python main.py userguide
```

## Contact 

www.wincacademy.com