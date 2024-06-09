from sys import argv
import csv

from database import initiate_db, create_session
from models import Restaurant

def load_csv(filename: str):
    with open(file=filename, mode="r") as file, create_session() as session:
        reader = csv.DictReader(file, delimiter=",")
        for row in reader:
            r = Restaurant()
            r.id = str(row["id"])
            r.rating = int(row["rating"])
            r.name = str(row["name"])
            r.site = str(row["site"])
            r.email = str(row["email"])
            r.phone = str(row["phone"])
            r.street = str(row["street"])
            r.city = str(row["city"])
            r.state = str(row["state"])
            r.lat = float(row["lat"])
            r.lng = float(row["lng"])
            session.add(r)
            
        session.commit()

def main():
    if len(argv) > 1 and argv[1] == "initiate_db":
        initiate_db()
    elif len(argv) > 2 and argv[1] == "load_csv":
        load_csv(argv[2])
    else:
        print("invalid option")
        exit(1)

if __name__ == "__main__":
    main()