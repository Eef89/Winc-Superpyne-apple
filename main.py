#rich
from rich.console import Console

# Files belonging to superpyne apple
import createcsv
import today
from parse import parser
import actions

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.
def main():
    console = Console()
    console.rule("[bold red]SUPERPYNE APPLE")
    createcsv.create_csv_files()
    today.create_datefile()
    if parser.args.actions == "buy":
        actions.buy(parser.args.name, parser.args.quantity, parser.args.price, parser.args.expiration_date)
    elif parser.args.actions == "sell":
        actions.sell(parser.args.name, parser.args.sell_price, parser.args.quantity)
    elif parser.args.actions == "advance-time":
        actions.backup()
        actions.advance_time(parser.args.days)
        today.isexpired()
    elif parser.args.actions == "backup": # creates backup of instock file.
        actions.backup()
    elif parser.args.actions == "inventory":
        actions.inventory()
    elif parser.args.actions == "userguide":
        actions.userguide()
    elif parser.args.actions == "readme":
        actions.readme()
    elif parser.args.actions == "profit":
        actions.profit(parser.args.mindate, parser.args.maxdate)



    



if __name__ == "__main__":
    main()
   