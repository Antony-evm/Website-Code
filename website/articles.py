from flask import Blueprint, render_template
from website.models import Articles, Categories

articles_blueprint = Blueprint("articles", __name__)


@articles_blueprint.route("/<cat_slug>/<article_slug>", methods=["GET"])
def go_to_article(cat_slug: str, article_slug: str) -> str:
    """
    View function responsible for finding the correct article to display.

    Args:
        cat_slug (str): The category slug used to
        identify the category of the article.
        article_slug (str): The article slug used to
        identify the article.

    Returns:
        str: The rendered template for displaying the article.
    """
    category = Categories.query.filter_by(slug=cat_slug).first()
    article = Articles.query.filter_by(slug=article_slug).first()

    return render_template(
        f"topics_templates/{category.slug}_templates/{article.slug}/{article.slug}.html",
        topic=category,
        article=article,
    )
