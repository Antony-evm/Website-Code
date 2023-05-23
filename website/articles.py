from flask import Blueprint, render_template
from website.models import Articles, Categories

articles = Blueprint("articles", __name__)


@articles.route("/<cat_slug>/<article_slug>", methods=["GET"])
def go_to_article(cat_slug: str, article_slug: str) -> str:
    """
    This function is responsible for finding the correct article to display.
    Uses cat_slug and article_slug to find the article within the database and returns the specified template.
    """
    category = Categories.query.filter_by(slug=cat_slug).first()
    article = Articles.query.filter_by(slug=article_slug).first()

    return render_template(
        f"topics_templates/{category.slug}_templates/{article.slug}/{article.slug}.html",
        topic=category,
        article=article,
    )
