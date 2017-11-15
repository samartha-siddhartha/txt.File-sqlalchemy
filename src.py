from numpy import genfromtxt
from sqlalchemy import Column, Integer, Float, Date,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',',dtype=String)

    return data

Base = declarative_base()
class PositionEntry(Base):
    #Tell SQLAlchemy what the table name is and if there's any table-specific arguments it should know about
    __tablename__ = 'PositionEntry'
    __table_args__ = {'sqlite_autoincrement': True}
    #tell SQLAlchemy the name of column and its attributes:
    id = Column(Integer, primary_key=True, nullable=False)
    underlying = Column(String)
    expiry   = Column(String)
    strike   = Column(Float)
    optype = Column(String)
    contract = Column(String)
    buy_sell = Column(Integer)
    quantity = Column(Integer)
    price   =  Column(Float)
    clientcode = Column(String)

if __name__ == "__main__":
    #Create the database
    engine = create_engine('sqlite:///csv_test.db')
    Base.metadata.create_all(engine)

    #Create the session
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    # try:
    file_name = "TradeFo.txt" 
    data = Load_Data(file_name)

    for i in data:
        print(type(i[3]))
        print(i[4])
        print(i[7])

        record = PositionEntry(**{
            # 'underlying' : datetime.strptime(i[0], '%d-%b-%y').date(),
            'underlying':str(i[3].decode('utf-8')).replace(' ', ''),
            'expiry' : str(i[4].decode('utf-8')),
            'strike' : float(i[5].decode('utf-8').replace(' ', '')),
            'optype' : str(i[6].decode('utf-8')),
            'contract' :str(i[7].decode('utf-8').replace(' ', '')),
            'buy_sell' : int(i[13].decode('utf-8')),
            'quantity': int(i[14].decode('utf-8')),
            'price'    : float(i[15].decode('utf-8')),
            'clientcode': str(i[17].decode('utf-8')).replace(' ', '')

        })
        print(type(i[3]))
        print(type(i[4]))
        print(type(i[7]))
        s.add(record)

    s.commit()



