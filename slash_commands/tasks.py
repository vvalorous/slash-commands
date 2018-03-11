import pickle
from slash_commands.celery import app

@app.task
def executor(func, *args, **kwargs):
    # func = pickle.loads(func)
    func(*args, **kwargs)
