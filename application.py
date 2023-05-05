from website import create_app
from flask import send_from_directory, request


application = create_app()


@application.route("/")
def index():
    pass


@application.route("/robots.txt")
@application.route("/sitemap.xml")
def static_from_root():
    return send_from_directory(application.static_folder, request.path[1:])


if __name__ == "__main__":
    application.run(debug=False)
