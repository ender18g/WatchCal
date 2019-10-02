from app import app, db
from app.models import User, Schedule


@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Schedule':Schedule}