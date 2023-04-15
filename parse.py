import argparse
from datetime import datetime

class parser():
    parser = argparse.ArgumentParser(prog='SUPERPYNE APPLE!', usage='%(prog)s options-list', description='Use the action "python main.py userguide" for a better explanation!')
    parser.add_argument('actions', choices=['buy', 'sell', 'inventory', 'advance-time', 'backup', 'userguide', 'readme', 'profit'], help='Run "python main.py userguide" for more help')
    parser.add_argument('-n', '--name', type=str, help="Name the product!")
    parser.add_argument('-q', '--quantity', type=int, help="Give the quantity!")
    parser.add_argument('-p', '--price', type=float, help="What was the price per item?")
    parser.add_argument('-ed', '--expiration_date', type=lambda d: datetime.strptime(d, '%d%m%Y'), help="Use ddmmyyyy!")
    parser.add_argument('-min', '--mindate', type=lambda d: datetime.strptime(d, '%d%m%Y'), help="Use ddmmyyyy!")
    parser.add_argument('-max', '--maxdate', type=lambda d: datetime.strptime(d, '%d%m%Y'), help="Use ddmmyyyy!")
    parser.add_argument('-sp', '--sell_price', type=float, help="Give the sell price!")
    parser.add_argument('-d', '--days', type=int, help="Give the amount of days you want to jump in the future!")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()