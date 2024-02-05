from django import template

register = template.Library()

@register.filter
def is_liked_by(feed, user):
    return feed.is_liked(user)