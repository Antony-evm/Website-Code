from website.models import Articles
from website import attrs

def is_search_empty(search):
	return search == '' or search == None

def is_it_topic_or_article(my_object):
	try:
		topic = my_object.topic
	except:
		topic = my_object.title
	return topic

def in_search(x,y):
	return x.lower() in str(y).lower()

def show(my_objects,search,state,state_change = attrs.STATIC_STATE):
	titles = [is_it_topic_or_article(my_object) for my_object in my_objects]
	if is_search_empty(search):
		search = ''
	else:
		my_objects = [my_object for my_object in my_objects if in_search(search,is_it_topic_or_article(my_object))]
		titles = [is_it_topic_or_article(my_object) for my_object in my_objects if in_search(search,is_it_topic_or_article(my_object))]
	if state_change == attrs.CHANGEABLE_STATE:
		state = state + 1

	if not state:
		state = attrs.DEFAULT_LAYOUT

	elif int(state)%3 == attrs.ALPHABETICAL_ORDER:
		my_objects = [my_objects[i] for i in sorted(range(len(titles)), key=lambda k: titles[k])]

	elif int(state)%3 == attrs.REVERSE_ALPHABETICAL_ORDER:
		my_objects = [my_objects[i] for i in sorted(range(len(titles)), key=lambda k: titles[k])]

	return my_objects,search,state

def displayable_list(l):
	if l:
		l = [Articles.query.filter_by(id=int(i)).first().title for i in l.split(',')]
		l.sort()
	return l