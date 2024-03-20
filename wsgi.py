import os

from blog.app import app
from blog.models.database import db


def init_db():
    db.create_all()
    print("done!")


if __name__ == '__main__':
    app.run(

        debug=True,
    )
    init_db()


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


@app.cli.command("create-tags")
def create_tags():
    """
    Run in your terminal:
    ➜ flask create-tags
    """
    from blog.models import Tag
    for name in [
        "flask",
        "django",
        "python",
        "sqlalchemy",
        "news",
    ]:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print("created tags")
