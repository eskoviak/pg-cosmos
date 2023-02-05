from MyGraph.utils.config import Util

util = Util()
config = util.get_config()

print(config['PGURI'])


"""
engine = create_engine(config['PGURI'])

stmt = '''SELECT *
FROM activity.test;
'''
with engine.connect() as conn:
    result = conn.execute(text(stmt))
    for row in result:
        print(row) #type: ignore
"""
