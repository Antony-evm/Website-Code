from website import db


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(500), unique=True)
    slug = db.Column(db.String(500))
    img_src = db.Column(db.String(500))
    description = db.Column(db.String(500))
    db.relationship("Articles")


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    slug = db.Column(db.String(500))
    cat_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    likes = db.Column(db.Integer, default=0)
    views = db.Column(db.Integer, default=0)
