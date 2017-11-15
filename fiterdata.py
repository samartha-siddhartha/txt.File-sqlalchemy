
from sqlalchemy import create_engine,Table,MetaData
from sqlalchemy.sql import select

metadata = MetaData()
engine = create_engine('sqlite:///csv_test.db')
connection =engine.connect()

PositionEntry = Table('PositionEntry', metadata, autoload=True, autoload_with=engine)
stmt = select([PositionEntry])
stmt = stmt.where(PositionEntry.columns.clientcode =="60028717" )

results = connection.execute(stmt).fetchall()

print(results[:5])




