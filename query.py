from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Band, Venue, Concert  

# Create the database engine
engine = create_engine('sqlite:///concerts.db')
Session = sessionmaker(bind=engine)
session = Session()

def query_all_bands():
    """Query all bands and their concerts."""
    bands = session.query(Band).all()
    for band in bands:
        print(f"{band.name} from {band.hometown} has performed in the following concerts:")
        for concert in band.all_concerts:
            print(f"- {concert.date} at {concert.concert_venue.title} in {concert.concert_venue.city}")

def query_band_concerts(band_name):
    """Query concerts for a specific band."""
    band = session.query(Band).filter_by(name=band_name).first()
    if band:
        print(f"{band.name} has performed in the following concerts:")
        for concert in band.all_concerts:
            print(f"- {concert.date} at {concert.concert_venue.title} in {concert.concert_venue.city}")
    else:
        print("Band not found.")

def query_venues_for_band(band_name):
    """Query venues where a specific band has performed."""
    band = session.query(Band).filter_by(name=band_name).first()
    if band:
        venues = band.venues  # Access the venues
        print(f"{band.name} has performed at the following venues:")
        for venue in venues:
            print(f"- {venue.title} in {venue.city}")
    else:
        print("Band not found.")

def query_all_venues():
    """Query all venues and their concerts."""
    venues = session.query(Venue).all()
    for venue in venues:
        print(f"{venue.title} in {venue.city} has hosted the following concerts:")
        for concert in venue.all_concerts:
            print(f"- {concert.date} by {concert.concert_band.name}")

if __name__ == "__main__":
    print("Querying all bands:")
    query_all_bands()
    print("\nQuerying specific band concerts:")
    query_band_concerts("Led Zeppelin")
    print("\nQuerying venues for Pink Floyd:")
    query_venues_for_band("Pink Floyd")
    print("\nQuerying all venues:")
    query_all_venues()

    session.close()  # Close the session after all queries
