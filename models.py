from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hometown = Column(String, nullable=False)
    concerts = relationship('Concert', back_populates='band')

    @property
    def all_concerts(self):
        """Returns all the concerts the band has played."""
        return self.concerts

    @property
    def venues(self):
        """Returns all the venues the band has performed at."""
        return {concert.venue for concert in self.concerts}

    def play_in_venue(self, venue, date):
        """Creates a new concert for the band at the given venue and date."""
        new_concert = Concert(band=self, venue=venue, date=date)
        session.add(new_concert)
        session.commit()
    
    def all_introductions(self):
        """Returns all the introductions for the band."""
        return [
            f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}"
            for concert in self.concerts
        ]

    @classmethod
    def most_performances(cls, session):
        """Returns the band that has played the most concerts."""
        band_counts = {}
        for concert in session.query(Concert).all():
            band_counts[concert.band] = band_counts.get(concert.band, 0) + 1
        return max(band_counts, key=band_counts.get)

class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    city = Column(String, nullable=False)
    concerts = relationship("Concert", back_populates="venue")

    @property
    def all_concerts(self):
        """Returns all the concerts held at this venue."""
        return self.concerts

    @property
    def bands(self):
        """Returns all the bands that have performed at this venue."""
        return {concert.band for concert in self.concerts}

    def concert_on(self, date):
        """Finds and returns the concert at this venue on the given date."""
        return next((concert for concert in self.concerts if concert.date == date), None)

    def most_frequent_band(self, session):
        """Returns the band with the most concerts at this venue."""
        band_counts = {}
        for concert in self.concerts:
            band_counts[concert.band] = band_counts.get(concert.band, 0) + 1
        return max(band_counts, key=band_counts.get) 

class Concert(Base):
    __tablename__ = 'concerts'

    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))

    band = relationship("Band", back_populates="concerts")
    venue = relationship("Venue", back_populates="concerts")

    @property
    def concert_band(self):
        """Returns the band for this concert."""
        return self.band

    @property
    def concert_venue(self):
        """Returns the venue for this concert."""
        return self.venue

    def hometown_show(self):
        """Returns True if the concert is in the band's hometown, False otherwise."""
        return self.venue.city == self.band.hometown

    def introduction(self):
        """Returns the band's introduction for this concert."""
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
