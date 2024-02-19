import pandas as pd
from sqlalchemy import create_engine

# Database connection parameters
db_host = '192.168.100.55'
db_user = 'admin'
db_password = 'admin'
db_name = 'beacon'
table_name = 'resetcount'  # Specify your table name here

# CSV file path
csv_file_path = 'reset_count.csv'  # Replace with the actual path to your CSV file

# Read CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Convert 'value' column to float
df['uint16__totalResetCount'] = df['uint16__totalResetCount'].astype(float)

# Create a SQLAlchemy engine to connect to the database
engine = create_engine(f"mysql://{db_user}:{db_password}@{db_host}/{db_name}")

# Upload the DataFrame to the specified table in the database
df.to_sql(table_name, con=engine, if_exists='append', index=False)

# Close the database connection
engine.dispose()

print(f"Data has been successfully uploaded to the table: {table_name}")
