from website import attrs
from typing import Union
from website.models import Categories as Cat, Articles as Art


def is_search_empty(search: str) -> bool:
    """
    Check if the search query is
    empty or None.

    Args:
        search (str): The search query.

    Returns:
        bool: True if the search query
        is empty or None, False otherwise.
    """
    return search == "" or not search


def is_it_topic_or_article(my_object: Union[Cat, Art]) -> str:
    """
    Check if the object is a topic or an article
    and return the corresponding title.

    Args:
        my_object: The object to check.

    Returns:
        str: The title of the topic or article.
    """
    print(type(my_object))
    try:
        topic = my_object.topic
    except Exception:
        topic = my_object.title
    return topic


def in_search(x: str, y: str) -> bool:
    """
    Check if the search term is present in a given string.

    Args:
        x (str): The search term.
        y (str): The string to search in.

    Returns:
        bool: True if the search term is found in the string, False otherwise.
    """
    return x.lower() in str(y).lower()


def show(my_objects: list, search: Union[str, None], state: Union[str, None], state_change: int = attrs.STATIC_STATE):
    """
    Apply filters and sorting based on search query and state.

    Args:
        my_objects: The list of objects (categories or articles) to filter and sort.
        search (str): The search query.
        state (int): The state value indicating the sorting option.
        state_change (int, optional):
        The state change value. Defaults to attrs.STATIC_STATE.

    Returns:
        Tuple: A tuple containing the filtered and
        sorted objects, search query, and updated state value.
    """
    titles = [is_it_topic_or_article(my_object) for my_object in my_objects]
    if is_search_empty(search):
        search = ""
    else:
        my_objects = [my_object for my_object in my_objects if in_search(search, is_it_topic_or_article(my_object))]
        titles = [
            is_it_topic_or_article(my_object)
            for my_object in my_objects
            if in_search(search, is_it_topic_or_article(my_object))
        ]
    if state_change == attrs.CHANGEABLE_STATE:
        state = state + 1

    if not state:
        state = attrs.DEFAULT_LAYOUT

    elif int(state) % 3 == attrs.ALPHABETICAL_ORDER:
        my_objects = [my_objects[i] for i in sorted(range(len(titles)), key=lambda k: titles[k])]

    elif int(state) % 3 == attrs.REVERSE_ALPHABETICAL_ORDER:
        my_objects = [my_objects[i] for i in sorted(range(len(titles)), key=lambda k: titles[k], reverse=True)]

    return my_objects, search, state
