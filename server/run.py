from app import create_app
from config import variables


if __name__ == '__main__':
    app = create_app()
    app.app_context().push()
    app.run(
        host=variables.HOST,
        port=int(variables.PORT),
        debug=bool(variables.DEBUG)
    )
