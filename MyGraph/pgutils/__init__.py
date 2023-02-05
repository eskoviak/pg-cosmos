from sqlalchemy import create_engine #, select, text, func
from sqlalchemy.orm import Session

from models.nodes import NodeType

class PgUtils:
    """class PgUtils
    
       This class contians all the direct database access methods and wrap the ORM models in the models package

    """
     
    def __init__(self, pguri : str):
        self.pguri = pguri