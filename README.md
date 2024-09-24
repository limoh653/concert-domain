# Concerts Domain

## Overview
The Concerts Domain project is a Python application built with SQLAlchemy to manage the relationships between bands, venues, and concerts. This application allows users to query and manipulate data related to musical performances, focusing on the many-to-many relationships between bands and venues.

## Project Structure
The application consists of three primary models:
- **Band**: Represents a musical group with attributes for name and hometown.
- **Venue**: Represents a concert location with attributes for title and city.
- **Concert**: Represents a performance event, linking a band and a venue, with an attribute for the concert date.

## Features
- **Manage Bands**: Create, read, update, and delete band records.
- **Manage Venues**: Create, read, update, and delete venue records.
- **Manage Concerts**: Schedule concerts by linking bands and venues.
- **Querying Data**: Retrieve information about bands, their concerts, and venues.

## Technologies Used
- **Python 3.x**
- **SQLAlchemy**: For ORM and database management
- **SQLite**: As the database for persistent storage

## Database Schema
### Bands Table
| Column  | Type   |
|---------|--------|
| name    | String |
| hometown| String |

### Venues Table
| Column | Type   |
|--------|--------|
| title  | String |
| city   | String |

### Concerts Table
| Column    | Type   |
|-----------|--------|
| date      | String |
| band_id   | Integer (ForeignKey) |
| venue_id  | Integer (ForeignKey) |

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/limoh653/concert-domain
   cd concert-domain
2. Create a Virtual Environment.

3. Install Dependencies: pipinstall

Database Setup. Run Migrations: Before running the application, ensure the database schema is up to date by running
Seed the Database: python seed.py

## Usage
Querying Data:Use the provided query functions in your Python scripts to retrieve data.

## Methods Overview
Band Methods:
-  concerts(): Returns all concerts that the Band has played.
-  venues(): Returns all venues that the Band has performed at.
-  play_in_venue(venue, date): Creates a new concert for the band at the specified venue on the given date.
-  all_introductions(): Returns all introductions for the band.
-  most_performances(): Returns the Band instance with the most concerts.

Venue Methods:
-  concerts(): Returns all concerts for the Venue.
-  bands(): Returns all bands that have performed at the Venue.
-  concert_on(date): Returns the first concert on the given date at the Venue.
-  most_frequent_band(): Returns the band with the most concerts at the venue.

Concert Methods:
-  band(): Returns the Band instance for this Concert.
-  venue(): Returns the Venue instance for this Concert.
-  hometown_show(): Returns True if the concert is in the band's hometown.
-  introduction(): Returns a formatted introduction string for the concert.

## Contributing.
Contributions are welcome! If you have suggestions for improvements or new features, please feel free to submit a pull request or report issues.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries, please contact Hesbon limo at limohesbon7@gmail.com








