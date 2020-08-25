from django.shortcuts import render,HttpResponseRedirect,get_object_or_404,redirect
from .models import Register

# Create your views here.
def index(request):
    return render(request,'index.html')

def display(request):
    if (request.method=="POST"):
        name1=request.POST.get('name1')
        name2=request.POST.get('name2')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        query=Register(medical_name=name1,phone_name=name2,phone_no=phone,address=address)
        query.save()
    posts=Register.objects.all()
    context={'posts': posts}

        
    return render(request,'display.html',context)

def delete_view(request,id,template_name='delete_post.html'):
    form= get_object_or_404(Register, id=id)    
    if request.method=='GET':
        form.delete()
        return redirect('display')

    return render(request, template_name)

def update_view(request,id):
    posts=get_object_or_404(Register,id=id)
    if request.method=='POST':
        form=RegisterForm(request.POST, instance=posts)
        if form.is_valid():
            form.save()
            return redirect('display')

    return render(request,'update_view.html', {'posts':posts})


def detail_view(request):
    if (request.method=="POST"):
        id=request.POST.get('id')
        name1=request.POST.get('name1')
        name2=request.POST.get('name2')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        form= get_object_or_404(Register, id=id)
        s=id
        form.delete()
        query=Register(id=s,medical_name=name1,phone_name=name2,phone_no=phone,address=address)
        query.save()
    posts=Register.objects.all()
    context={'posts': posts}
    
    return render(request,'display.html',context)
