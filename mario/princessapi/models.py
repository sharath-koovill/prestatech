from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date

Base = declarative_base()

class ShortestPathRequest(Base):
    __tablename__ = "shortest_path_request"
    id = Column(Integer, primary_key=True)    
    grid = Column(String)
    grid_size = Column(Integer)
    request_time = Column(String)    
    
