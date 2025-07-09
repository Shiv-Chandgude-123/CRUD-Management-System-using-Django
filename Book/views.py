from email.mime import message
from django.shortcuts import redirect, render
from .models import book, employee
# Create your views here.
def home(request):
    return render(request, 'home.html')

def show(request):
    obj = book.objects.all() #ORM command
    context = {"data": obj}
    return render(request, 'home.html', context)

def showemployee(request):
    obj = employee.objects.all()  
    context = {"empdata": obj}
    return render(request, 'home.html', context)
def add(request):

    if request.method == "POST":

        bname = request.POST.get('book_name')
        price = int(request.POST.get('book_price'))
        author= request.POST.get('author')
        pdate = request.POST.get('pubdate')
        qty = int(request.POST.get('qty'))
        obj = book(book_name=bname, book_price=price, author=author, pubdate=pdate, qty=qty)
        obj.save()
        return redirect('show')



    return render(request, 'addbook.html')


def addemp(request):

    if request.method == "POST":

        ename = request.POST.get('ename')
        sal = int(request.POST.get('sal'))
        deptno = int(request.POST.get('deptno'))
        job = request.POST.get('job')
        age = int(request.POST.get('age'))
        obj = employee(ename=ename, sal=sal, deptno=deptno, job=job, age=age)
        obj.save()
        return redirect('showemployee')



    return render(request, 'addemp.html')




def deleteb(request, id):
    b = book.objects.get(id=id)
    b.delete()
    return redirect('show')

def deletee(request, id):
    e = employee.objects.get(id=id)
    e.delete()
    return redirect('showemployee')


def updateb(request, id):
    b = book.objects.get(id=id)


    if request.method == "POST":

        bname = request.POST.get('book_name')
        price = float(request.POST.get('book_price'))
        author= request.POST.get('author')
        pdate = request.POST.get('pubdate')
        qty = int(request.POST.get('qty'))
        
        b = book.objects.get(id=id)
        b.book_name = bname
        b.book_price = price
        b.author = author
        b.pubdate = pdate
        b.qty = qty
        b.save()
        return redirect('show')

    
    return render(request, 'update.html', {"data": b})



def updateemp(request, id):
    e = employee.objects.get(id=id)


    if request.method == "POST":

        ename = request.POST.get('ename')
        sal = float(request.POST.get('sal'))
        deptno = int(request.POST.get('deptno'))
        job = request.POST.get('job')
        age = int(request.POST.get('age'))
        
        e = employee.objects.get(id=id)
        e.ename = ename
        e.sal = sal
        e.deptno = deptno
        e.job = job
        e.age = age
        e.save()
        return redirect('showemployee')

    
    return render(request, 'updateemp.html', {"data": e})
