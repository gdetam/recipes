"""this is loader for flask project."""

from app import app
from routers import loader_routers


if __name__ == '__main__':
    app.run(debug=True)
