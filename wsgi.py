import os

from blog.app import app
from blog.models.database import db

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True,
    )


# @app.cli.command("init-db")
# def init_db():
#     """
#     Run in your terminal:
#     flask init-db
#     """
#     db.create_all()
#     print("done!")


@app.cli.command("create-users")
def create_users():
    """
    Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from blog.models.user import User
    admin = User(username="admin", is_staff=True)
    admin.password = os.environ.get('ADMIN_PASSWORD') or 'adminpass'
    db.session.add(admin)
    db.session.commit()
    print("done! created users:", admin)
