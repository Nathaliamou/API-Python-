from SQLAchemy import create_engine
from SQLAchemy.engine import URL
from SQLAchemy.orm import sessionmaker

url = URL (
    drivername="postgresql",
    username="postgres",
    password="postgres",
    host="localhost",
    database="postgres",
    port=5432
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()