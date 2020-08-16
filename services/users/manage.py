# services/users/manage.py
import sys
import unittest

from flask.cli import FlaskGroup

# from project import app, db  # new
from project import create_app, db  # new
from project.api.models import User  # new


#cli = FlaskGroup(app)
app = create_app()  # new
cli = FlaskGroup(create_app=create_app)

# new


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

# new


@cli.command()
def test():
    """Runs the tests withot code coverage."""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)


@cli.command('seed_db')
def seed_db():
    """Seeds the database."""
    db.session.add(User(username='fredy.huanca', email="abelthf@gmail.com"))
    db.session.add(User(username='abel.huanca',
                        email="abel.huanca@upeu.edu.pe"))
    db.session.commit()


if __name__ == '__main__':
    cli()
