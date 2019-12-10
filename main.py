import sqlalchemy as db
from eightqueens import QueensSolver

if __name__ == "__main__":
    print("hey")
    engine = db.create_engine('postgresql://brime:panda@localhost/queensdb')
    connection = engine.connect()
    query = db.insert('solutions')
    payload = []

    solver = QueensSolver(8)
    for solution in solver.solutions:
        payload.extend([{
            'solution_string': solution.copy()
        }])
    
    ResultProxy = connection.execute(query, payload)
