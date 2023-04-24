from .models import Car

menu = [
    {'title': "Главная страница", 'url_name': "home"},
    {'title': "О сайте", 'url_name': "about"},
    {'title': "Продать машину", 'url_name': "sell"},
    {'title': "Обратная связь", 'url_name': "contact"},
]


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        posts = Car.objects.all()
        context['menu'] = menu
        context['posts'] = posts

        return context
