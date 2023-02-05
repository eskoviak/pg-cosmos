from sqlalchemy import (Column, DateTime, Float, ForeignKey, Integer, MetaData,
                        String, Text)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base(metadata=MetaData(schema='mygraph'))

#import enum

class NodeType(Base):
   """class NodeType
   
      Enumeration of the types of Nodes allowed

   """
   __tablename__ = 'node_type'

   type_id = Column(Integer, primary_key=True)
   type_name = Column(String(15), nullable=False)

   def __repr__(self):
      return(f'NodeType (type_id: {self.type_id}, type_name: {self.type_name})')



