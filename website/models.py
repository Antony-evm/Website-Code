from website import db


class Categories(db.Model):
    """
    Class for the Unique Categories in the website
    id-> Unique Identifier
    topic->Descriptive group of the articles it contains as general category
    slug->website url
    img_src->where the image is stored for this specific category
    description->short descriptive text
    Relates to articles
    """

    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(500), unique=True)
    slug = db.Column(db.String(500))
    img_src = db.Column(db.String(500))
    description = db.Column(db.String(500))
    db.relationship("Articles")


class Articles(db.Model):
    """
    Class for the artciles in the website
    id-> Unique Identifier
    title-> Title of the article
    slug-> website url
    cat_id-> which general category does the article fall under
    likes-> not implemented yet
    views-> not implemented yet
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    slug = db.Column(db.String(500))
    cat_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    likes = db.Column(db.Integer, default=0)
    views = db.Column(db.Integer, default=0)
