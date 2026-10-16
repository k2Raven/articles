from django.shortcuts import render

def index_view(request):
    print(request.GET.get('id'))
    name = request.GET.get('name')
    age = request.GET.get('age')
    context = {
        'name': name,
        'age': age
    }
    return render(request, 'index.html', context)
    # return render(request, 'index.html', {'name': name, 'age': age})

def about_view(request):
    return render(request, 'about.html')


def article_create_view(request):
    if request.method == 'GET':
        return render(request, 'create_article.html')
    elif request.method == 'POST':
        context = {
            'title': request.POST.get('title'),
            'content': request.POST.get('content'),
            'author': request.POST.get('author')
        }
        return render(request, 'article_view.html', context)