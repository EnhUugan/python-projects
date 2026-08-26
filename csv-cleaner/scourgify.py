import sys
import csv

def check_inp(input):
    if len(input) == 2:
        if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
            return True
        else:
            sys.exit("Not a CSV file")
    elif len(input) < 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

if check_inp(sys.argv[1:]):
    try:
        with open (f"{sys.argv[1]}") as infile:
            reader = csv.DictReader(infile)
            with open (f"{sys.argv[2]}", "w") as outfile:
                writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                    pieces = row["name"].split(", ")
                    writer.writerow({"first": pieces[1], "last": pieces[0], "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
