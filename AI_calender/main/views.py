from django.http.response import Http404
from django.shortcuts import redirect, render
from . import forest, decide
from .forms import admission_form, verify_form, edit_form, interval_form
# Create your views here.
from .models import Individual_data, Schedule

global_name = ''
detail_dict = {'1':'生理的行動','2':'社会的行動','3':'文化的行動'}

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
            return redirect('/main/') 
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
            new.save()
            global_name = form.cleaned_data['name']
            return redirect('/main/')
        else:
            return render(request,'html/create.html',{'error':'パスワードが一致しません'})
    else:
        return render(request,'html/create.html')

def main(request):
    try:
        user = Individual_data.objects.get(name=global_name)
    except Individual_data.DoesNotExist:
        raise Http404("this page don't exist")
    all_schedule = Schedule.objects.filter(user_data=user)
    context = {'object':[obj for obj in all_schedule]}
    return render(request,'html/main.html',context)

def edit(request,pk):
    try:
        user = Individual_data.objects.get(name=global_name)
    except Individual_data.DoesNotExist:
        raise Http404()
    if request.method == 'POST':
        form = edit_form(request.POST)
        if not form.is_valid():
            print(form)
            return render(request,'html/edit.html',{'error':'必要事項が入力されていません'})
        start = form.cleaned_data['start_date']
        end = form.cleaned_data['end_date']
        try:
            task = Schedule.objects.get(id=pk)
            cls = forest.classifyer(form.cleaned_data['description'])
            task.update(start_date=start,description=form.cleaned_data['description'],end_date=end,schedule_class=cls)    
        except Schedule.DoesNotExist:
            cls = forest.classifyer(form.cleaned_data['description'])
            task = Schedule(start_date=start,description=form.cleaned_data['description'],end_date=end,schedule_class=cls,user_data=user)
            task.save()
        return redirect('/main/')
    else:
        return render(request,'html/edit.html')

def AI(request):
    try:
        user = Individual_data.objects.get(name=global_name)
    except Individual_data.DoesNotExist:
        raise Http404()
    if request.method == 'POST':
        form = interval_form(request.POST)
        if not form.is_valid():
            return redirect('/AI_choice/')
        plan = decide.clasifyer(form.cleaned_data['start_date'],form.cleaned_data['end_date'])   #start,end
        for ele in plan:
            Schedule(start_date=ele[0],end_date=ele[1],schedule_class=ele[2][1],description=detail_dict[ele[2][1]],user_data=user).save()
        return redirect('/main/')
    else:
        return render(request,'html/AI.html')

def auth(request):
    decide.make()
    return redirect('/')
