from django.shortcuts import render 
from django.http import HttpResponse 
from .models import Book, Author, BookInstance, Genre
from django.views import generic
 
 
# Create your views here. 
def index(request):
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'На складе')
    # Здесь метод 'all()' применен по умолчанию.
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    # Авторы книг,
    num_authors = Author.objects.count()
    # Отрисовка HTML-шаблона index.html с данными
    # внутри переменной context
    num_visits = request.session.get('num_visits', 0)     
    request.session['num_visits'] = num_visits + 1 
    return render(request, 'index.html', context={
    'num_books': num_books,
    'num_instances': num_instances,
    'num_instances_available': num_instances_available,
    'num_authors': num_authors,
    'num_visits': num_visits}) 

class BookDetailView(generic.DetailView):
    model = Book

class BookListView(generic.ListView):
    model = Book
    paginate_by = 3

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4
