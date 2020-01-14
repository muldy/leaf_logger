from sqlalchemy import *

db = create_engine('sqlite:///trips.db')

db.echo = False  # Try changing this to True and see what happens

metadata = BoundMetaData(db)

users = Table('trips', metadata,
    Column('trip_id', Integer, primary_key=True),
    Column('Trip', Integer),
    Column('DevBat', Integer),
    Column('Gids', Integer),
    Column('Seq', Integer),
    Column('Odo', Integer),
    Column('SOC', Float),
    Column('AHr', Float),
    Column('BatTemp', Float),
    Column('Amb', Float),
    Column('Wpr', Integer),
    Column('PlugState', Integer),
    Column('ChrgMode', Integer),
    Column('ChrgPwr', Integer),
    Column('VIN', String(40)),
    Column('PwrSw', Integer),
    Column('Tunits', String),
    Column('RPM', Integer),
    Column('SOH', Float),
)
users.create(checkfirst=True)
