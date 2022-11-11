import os

# Import Pandas
import pandas as pd

# Import environment variables (python-dotenv: https://pypi.org/project/python-dotenv/)
from dotenv import load_dotenv
load_dotenv()

# Import SQLalchemy to connect to postgres db (https://docs.sqlalchemy.org/en/14/core/connections.html)
from sqlalchemy import create_engine
import psycopg2

# Load CSV file, convert to pandas df, and export to SQL db
def csv_to_sql(csv_path):
    # Read CSV
    df = pd.read_csv(csv_path)
    
    # Get the database URI/URL
    db_url = f"postgresql://{os.environ['USER']}:{os.environ['POSTGRES_PASS']}@{os.environ['POSTGRES_HOST']}:{os.environ['POSTGRES_PORT']}/{os.environ['POSTGRES_DB']}"
        # or "sqlite:///" + os.path.join(os.path.abspath(os.path.dirname(__file__)), "deathrow.db")
    
    # Create engine
    engine = create_engine(db_url, echo=False)
    
    # Convert df to SQL
    with engine.begin() as connection:
        df.to_sql("executions", con=connection, if_exists="replace")
    
    print("Ready")


if __name__ == '__main__':
    csv_path = './data/tx_deathrow_full.csv'
    csv_to_sql(csv_path)


# References
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html#r689dfd12abe5-1
# https://gist.github.com/amotl/8727ea2aa6e46c5b51a34c28b767d72c