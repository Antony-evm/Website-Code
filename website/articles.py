from flask import Blueprint,render_template,request,redirect,url_for,flash
from website import db
from website.models import Articles,Categories
articles = Blueprint('articles',__name__)

@articles.route('/<cat_slug>/<article_slug>',methods=['GET'])
def go_to_article(cat_slug,article_slug):
	category = Categories.query.filter_by(slug=cat_slug).first()
	article = Articles.query.filter_by(slug=article_slug).first()

	return render_template(f"topics_templates/{category.slug}_templates/{article.slug}/{article.slug}.html",topic=category,article=article)

