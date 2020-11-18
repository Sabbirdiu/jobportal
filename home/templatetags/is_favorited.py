from django import template

from home.models import Favorite

register = template.Library()


@register.simple_tag(name='is_favorited', takes_context=True)
async def is_favorited(context, job):
    request = context['request']
    return Favorite.objects.filter(job_id=job.id, user_id=request.user.id, soft_deleted=False).exists()
