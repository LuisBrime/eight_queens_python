import sqlalchemy as db
from sqlalchemy import table
from eightqueens import QueensSolver

if __name__ == "__main__":
    engine = db.create_engine('postgresql+psycopg2://brime:panda@db/queensdb')
    connection = engine.connect()
    metadata = db.MetaData()
    solutions_table = db.Table('solutions', metadata, db.Column('solution_id', db.Integer(), db.Sequence('id'), primary_key=True), db.Column('solution_string', db.String(25), nullable=False))

    metadata.create_all(engine)

    payload = []

    solver = QueensSolver(8)
    for solution in solver.solutions:
        query = db.insert(solutions_table).values(solution_string = str(solution))
        ResultProxy = connection.execute(query)
