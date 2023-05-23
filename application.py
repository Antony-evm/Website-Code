from typing import Union
from flask import request
from flask.wrappers import Response
from werkzeug.utils import send_from_directory
from website import create_app


application = create_app()


@application.route("/robots.txt")
@application.route("/sitemap.xml")
def static_from_root() -> Union[str, Response]:
    """
    Outputs the sitemap and the robots files from the static folder.

    Returns:
        Union[str, Response]: The response containing the requested file.
    """
    file_path = request.path[1:]
    environ = request.environ
    return send_from_directory(str(application.static_folder), file_path, environ=environ)


if __name__ == "__main__":
    application.run(debug=False)
