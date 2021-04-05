from django.shortcuts import render,redirect,get_object_or_404
from .forms import DayCreateForm
from .models import Day

# Create your views here.
def index(request):
    context = {
        #dbに保存されているデータ(Day)をすべて取り出す(model名.objects.all())
        'day_list': Day.objects.all(),
    }
    return render(request, 'diary/day_list.html',context)

def add(request):
    #送信内容(POST)をもとにフォームを作る。POSTではなければ、空のフォーム
    form = DayCreateForm(request.POST or None)

    #method=POST,つまり送信ボタン押下時、入力内容に問題がなければ(form.is_vaid())
    if request.method == 'POST' and form.is_valid():
        form.save()
        #Redirect：ページ（ここでいうとdiary:index）にアクセスする
        #diary:indexは,urls.py内で指定しているapp_nameとurlpatterns内のnameになる
        return redirect('diary:index')

    #通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'form':form
    }
    #render：contextの内容をdiary/day_form.htmlにレンダリングする
    return render(request, 'diary/day_form.html',context)

def update(request,pk):
    #urlのpkを基に、Dayを取得  get_object_or_404：そのデータがデータベース内にあればそれを返し、なかったら404を表示
    day = get_object_or_404(Day,pk=pk)

    #フォームに、取得したDayを紐づける
    form = DayCreateForm(request.POST or None,instance=day)

    #method=POST、つまり送信ボタン押下時、入力内容に問題がなければ
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')
    
    #通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'form':form
    }
    return render(request, 'diary/day_form.html',context)

def delete(request,pk):
    #urlのpkを基に、Dayを取得  get_object_or_404：そのデータがデータベース内にあればそれを返し、なかったら404を表示
    day = get_object_or_404(Day,pk=pk)

    #method=POST、つまり送信ボタン押下時、入力内容に問題がなければ
    if request.method == 'POST' :
        day.delete()
        return redirect('diary:index')
    
    #通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'day':day
    }
    return render(request, 'diary/day_confirm_delete.html',context)

def detail(request,pk):
    #urlのpkを基に、Dayを取得  get_object_or_404：そのデータがデータベース内にあればそれを返し、なかったら404を表示
    day = get_object_or_404(Day,pk=pk)
   
    #通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'day':day
    }
    return render(request, 'diary/day_detail.html',context)

