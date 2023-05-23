from flask import Blueprint, render_template, request
from website.models import Articles, Categories
from website.helper_funcs import sort_search as ss

topics_blueprint = Blueprint("topics", __name__)


@topics_blueprint.route("/<cat_slug>", methods=["GET", "POST"])
def go_to_category(cat_slug: str) -> str:
    """
    View function that displays the categories,
    sorts them based on user preference
    or searches within them to display the relevant categories.

    Args:
        cat_slug (str): The category slug used to
        identify which category's articles should be displayed.

    Returns:
        str: The rendered template for displaying
        the category and its articles.
    """
    if request.method == "GET":
        search = request.args.get("jsdata")
        state = request.args.get("state")
        categories = Categories.query.filter_by(slug=cat_slug).first()
        articles = Articles.query.filter_by(cat_id=categories.id).all()
        articles, search, state = ss.show(articles, search, state)
        return render_template(
            "topics_templates/category.html",
            topic=categories,
            articles=articles,
            state=state,
            search=search,
        )
    else:
        search = request.form.get("search_filter_article")
        state_change = int(request.form.get("state_change_articles"))
        state = int(request.form.get("state_article"))
        categories = Categories.query.filter_by(slug=cat_slug).first()
        articles = Articles.query.filter_by(cat_id=categories.id).all()
        articles, search, state = ss.show(articles, search, state, state_change)
        return render_template(
            "topics_templates/category.html",
            topic=categories,
            articles=articles,
            state=state,
            search=search,
        )
