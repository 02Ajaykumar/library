from django.shortcuts import render , redirect
from .models import Category,Book

# Create your views here.

def category_view(request,name):

    categories = Category.objects.all()
    books1 = Book.objects.all()
    books = []

    books_category = name
    for book in books1:
        if book.category.lower().strip() == books_category.lower().strip():
            books.append(book)

    return render(request,"index.html",{'categories':categories,'books':books,'books_category':books_category.upper()})



def home(request):

    categories = Category.objects.all()
    books1 = Book.objects.all()
    books = []

    books_category = 'Popular choices'
    for book in books1:
        if book.category.lower().strip() == 'popular choices':
            books.append(book)

    return render(request,"index.html",{'categories':categories,'books':books,'books_category':books_category.upper()})
    

def bookview(request,name):

    book = Book.objects.get(name=name)
    bookname = book.name
    category = book.category
    author = book.author
    publication = book.publication
    availability = book.availability

    return render(request,"bookview.html",{'book':book,'bookname':bookname,'category':category,'author':author,'publication':publication,'availability':availability})

def search(request):

    categories = Category.objects.all()
    books1 = Book.objects.all()
    books = []
    books_category = 'RESULT'
    input = request.POST['str']
    input = input.lower().strip()

    for book in books1:
        if input in book.name.lower().strip() or  input in book.category.lower().strip() or input in book.author.lower().strip() or input in book.publication.lower().strip():
            books.append(book)

    return render(request,"index.html",{'categories':categories,'books':books,'books_category':books_category.upper()})