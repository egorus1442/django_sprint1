from django.shortcuts import render

posts = [
    {
        'id': 0,
        'location': 'Остров приключений',
        'date': '3 сентября 1959 года',
        'category': 'travel',
        'text': '''Мы с моим другом Джоном прибыли на Остров
                Приключений ранним утром. Наш гид Марио предложил
                отправиться в глубину острова, где скрывались древние
                тайны. Мы согласились и отправились в путь через густые
                джунгли, полные звуков дикой природы.''',
    },
    {
        'id': 1,
        'location': 'Остров приключений',
        'date': '4 октября 1959 года',
        'category': 'not-my-day',
        'text': '''Вдруг, среди зарослей, мы наткнулись на старинную карту,
                указывающую путь к таинственному храму. Следуя указаниям карты,
                мы добрались до величественного сооружения, украшенного резьбой
                и древними символами. Внутри храма нас ждали ловушки и
                головоломки, которые нужно было решить, чтобы добраться
                до сокровища.''',
    },
    {
        'id': 2,
        'location': 'Остров приключений',
        'date': '28 октября 1959 года',
        'category': 'not-my-day',
        'text': '''Мы с Джоном работали вместе, используя все свои знания
                и смекалку. В конце концов, мы добрались до главного зала, где
                нас ждал золотой амулет с магической силой. Вернувшись на
                берег, мы были полны впечатлений и чувством выполненного
                долга, зная, что это приключение останется в
                нашей памяти навсегда.''',
    },
]


def index(request):
    template = 'blog/index.html'
    context = {'posts_list': reversed(posts)}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    id = int(id)
    if 0 <= id < len(posts):
        context = {
            'post': posts[id],
            'id': id,
        }
    else:
        # Обработка случая, когда id выходит за пределы диапазона
        context = {
            'post': None,
            'id': id,
        }
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {
        'category_slug': category_slug,
    }
    return render(request, template, context)
