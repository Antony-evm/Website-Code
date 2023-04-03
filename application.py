from website import create_app
from flask_mail import Mail
application = create_app()
if __name__ == '__main__':
	application.run(debug=True)