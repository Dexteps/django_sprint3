from django.utils.timezone import now


def filter_objects(objs):
    """Общая функция выборки постов"""
    return objs.select_related(
        'author',
        'category',
        'location'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__date__lte=now(),
    )
