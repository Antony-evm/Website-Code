from website import db


class Categories(db.Model):
    """
    Class for the Unique Categories in the website.

    Attributes:
        id (int): Unique Identifier.
        topic (str): Descriptive group of the articles it contains as general category.
        slug (str): Website URL.
        img_src (str): Location where the image is stored for this specific category.
        description (str): Short descriptive text.

    Relationships:
        Relates to Articles.
    """

    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(500), unique=True)
    slug = db.Column(db.String(500))
    img_src = db.Column(db.String(500))
    description = db.Column(db.String(500))
    db.relationship("Articles")


class Articles(db.Model):
    """
    Class for the articles in the website.

    Attributes:
        id (int): Unique Identifier.
        title (str): Title of the article.
        slug (str): Website URL.
        cat_id (int): ID of the general category to which the article belongs.
        likes (int): Number of likes for the article (not implemented yet).
        views (int): Number of views for the article (not implemented yet).
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    slug = db.Column(db.String(500))
    cat_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    likes = db.Column(db.Integer, default=0)
    views = db.Column(db.Integer, default=0)
