from re import error, template
from typing import Generic
from django.http.response import Http404, StreamingHttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.views import generic
# Create your views here.
from .models import Schedule, Individual_data
from .forms import verify_form

def index(request):
    if request.method == 'POST':
        form = verify_form(request.POST)
        if not form.is_valid():
            return redirect('./main/static/html/index.html',error='必要事項が入力されていません')
        try:
            user = Individual_data.objects.get(user_name=form.name)
        except Individual_data.DoesNotExist:
            return redirect('./main/static/html/index.html',error='そのようなユーザーは存在しません')
        if user.password == form.password:
            return 
        else:
            return redirect(request,'./main/static/html/index.html',error='ユーザー名とパスワードが一致しません')
    else:
        render(request,'./main/static/html/index.html')


def main(request,name):
    all_shedule = Individual_data.objects.filter(user_name=name)
    return render(request, './frontend/html/main.html',all_shedule)

