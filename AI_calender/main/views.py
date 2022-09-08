from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from .forms import admission_form, verify_form, edit_form, interval_form
# Create your views here.
from .models import Individual_data, Schedule
from .dbscan import clasify

global_name = ''

def index(request):
    global global_name
    if request.method == 'POST':
        form = verify_form(request.POST)
        if not form.is_valid():
            return render(request,'html/index.html',{'error':'必要事項が入力されていません'})
        try:
            user = Individual_data.objects.get(name=form.cleaned_data['name'])
        except Individual_data.DoesNotExist:
            return render(request,'html/index.html',{'error':'そのようなユーザーは存在しません'})
        if user.password == form.cleaned_data['password']:
            global_name = form.cleaned_data['name'] 
        else:
            return render(request,'html/index.html',{'error':'ユーザー名とパスワードが一致しません'})
    else:
        return render(request,'html/index.html')

def create(request):
    global global_name
    if request.method == 'POST':
        form = admission_form(request.POST)
        print(form)
        if not form.is_valid():
            return render(request,'html/create.html',{'error':'必要事項が入力されていません'})
        try:
            Individual_data.objects.get(name=form.cleaned_data['name'])
            return render(request,'html/create.html',{'error':'その名前は現在使われています'})
        except Individual_data.DoesNotExist:
            pass
        if form.cleaned_data['password'] == form.cleaned_data['verify_password']:
            new = Individual_data(name=form.cleaned_data['name'],password=form.cleaned_data['password'])
            print(new.name,new.password)
            new.save()
            global_name = form.cleaned_data['name']
            return redirect('main/')
        else:
            return render(request,'html/create.html',{'error':'パスワードが一致しません'})
    else:
        return render(request,'html/create.html')

def main(request):
    try:
        user = Individual_data.objects.get(name=global_name)
    except Individual_data.DoesNotExist:
        return Http404()
    all_schedule = Schedule.objects.filter(user_data=user)
    context = {'object':[obj for obj in all_schedule]}
    return render(request,'html/main.html',context)

def edit(request,pk):
    task = Schedule.objects.get(id=pk)
    try:
        user = Individual_data.objects.get(user_name=global_name)
    except Individual_data.DoesNotExist:
        return Http404()
    if request.method == 'POST':
        form = edit_form(request.POST)
        if not form.is_valid():
            return redirect(request,'html/edit.html',{'error':'必要事項が入力されていません','schedule':task})
        task.update(start_date=form.start_date,description=form.description,end_date=form.end_date)
        redirect('main/')
    else:
        return render(request,'html/edit.html',{'schedule':task})

def AI(request):
    try:
        user = Individual_data.objects.get(user_name=global_name)
    except Individual_data.DoesNotExist:
        return Http404()
    if request.method == 'POST':
        form = interval_form(request.POST)
    if not form.is_valid():
        return redirect('AI_choice/')
    else:
        render(request,'html/AI.html')
