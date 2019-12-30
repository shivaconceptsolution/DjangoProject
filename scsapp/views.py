from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact,Register,Feedback
from django.template import RequestContext
from django.conf import settings
from django.core.files.storage import FileSystemStorage
def ajaxload(request):
    return render(request,"scsapp/ajaxsearch.html")
def ajaxdata(request):
    data = request.GET["q"]
    result = Register.objects.filter(fullname__contains=data)
    return render(request,"scsapp/ajaxdata.html",{'res':result})    
def fileupload(request):
     if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'scsapp/fileupload.html', {
            'uploaded_file_url': uploaded_file_url
        })
     return render(request, 'scsapp/fileupload.html')
def setcookie(request):  
    response = HttpResponse("Cookie Set")  
    response.set_cookie('ckey', 'hello')  
    return response  
def getcookie(request):  
    a  = request.COOKIES['ckey']  
    return HttpResponse("value is "+  a);  
def index(request):
	return render(request,"scsapp/index.html")
def about(request):
	return render(request,"scsapp/about.html")
def service(request):
	return render(request,"scsapp/services.html")
def login(request):
    return render(request,"scsapp/login.html")
def logincode(request):
    e=request.POST["txtemail"]
    p=request.POST["txtpass"]
    s = Register.objects.filter(emailid=e,password=p)
   
    if(s.count()==1):
        request.session['uid']=e
       
        return redirect('dashboard')
    else:
        return render(request,"scsapp/login.html",{'msg':'invalid userid and password'})
def contact(request):
	return render(request,"scsapp/contact.html")
def viewcontact(request):
    s=Contact.objects.all()
    return render(request,"scsapp/viewcontact.html",{'res':s})
def Editcontact(request):
    s = Contact.objects.get(pk=request.GET["q"])
    return render(request,"scsapp/editcontact.html",{'res':s}) 
def edit(request):
    e=request.POST["txtemail"]
    m=request.POST["txtmobile"]
    msg=request.POST["txtmsg"]
    s = Contact.objects.get(pk=request.POST["txtid"])
    s.emailid=e
    s.mobile=m
    s.message=msg
    s.save()
    return redirect('viewcontact')
def Deletecontact(request):
    s = Contact.objects.get(pk=request.GET["q"])
    s.delete()
    return redirect('viewcontact')
def contactcode(request):
    e=request.POST["txtemail"]
    m=request.POST["txtmobile"]
    msg=request.POST["txtmsg"]
    obj = Contact(emailid=e,mobile=m,message=msg)
    obj.save()
    return redirect('viewcontact')
   # return render(request,"scsapp/contact.html",{'res':'data submitted successfully'})
def editcontact(request):
    return render(request,"scsapp/editcontact")
def deletecontact(request):
    return render(request,"scsapp/deletecontact")
def gallery(request):
	return render(request,"scsapp/gallery.html")
def dashboard(request):
    if(request.session.has_key('uid')):
     data = request.session['uid'] 
     
     return render(request,"scsapp/dashboard.html",{'u':data})
    else:
     return render(request,"scsapp/login.html")

def dashcode(request):
    e=request.POST["txtemail"]
    m=request.POST["txtto"]
    msg=request.POST["txtdesc"]
    obj = Feedback(emailid=e,feeddesc=msg,feedto=m)
    obj.save()
    return render(request,"scsapp/dashboard.html",{'msg':'feedback submitted successfully'})
def logout(request):
    del request.session['uid']
    return redirect('login')    