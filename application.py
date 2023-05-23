from website import create_app
from flask import send_from_directory, request
from flask.wrappers import Response


application = create_app()


@application.route("/robots.txt")
@application.route("/sitemap.xml")
def static_from_root() -> Response:
    """
    Outputs the sitemap and the robots files from the static folder
    """
    return send_from_directory(application.static_folder, request.path[1:])


if __name__ == "__main__":
    application.run(debug=True)
