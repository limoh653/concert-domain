# seed.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Band, Venue, Concert, Base  # Replace with your actual models file

# connection to the database
engine = create_engine('sqlite:///concerts.db')  
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add sample data
try:
    # Bands
    band1 = Band(name="Pink Floyd", hometown="London")
    band2 = Band(name="Led Zeppelin", hometown="Manchester")
    band3 = Band(name="Queen", hometown="Liverpool")
    
    # Venues
    venue1 = Venue(title="Wembley Stadium", city="London")
    venue2 = Venue(title="The Forum", city="Los Angeles")
    venue3 = Venue(title="Sydney Opera House", city="Sydney")
    
    # Concerts
    concert1 = Concert(band=band1, venue=venue1, date="2025-08-15")
    concert2 = Concert(band=band2, venue=venue1, date="2025-09-01")
    concert3 = Concert(band=band3, venue=venue2, date="2025-10-20")
    concert4 = Concert(band=band1, venue=venue2, date="2025-11-11")
    concert5 = Concert(band=band2, venue=venue3, date="2025-12-25")
    concert6 = Concert(band=band3, venue=venue3, date="2026-01-05")

    # Add all the instances to the session
    session.add_all([band1, band2, band3, venue1, venue2, venue3, concert1, concert2, concert3, concert4, concert5, concert6])
    
    # Commit the session to save the data in the database
    session.commit()
    print("Sample data added successfully!")

except Exception as e:
    session.rollback()  # Rollback in case of any errors
    print(f"An error occurred: {e}")

finally:
    session.close()
