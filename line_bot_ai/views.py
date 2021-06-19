
from django.shortcuts import render

#lineボット用モジュール
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from .utils import message_creater
from line_bot_ai.line_message import LineMessage

#Webアプリ用モジュール
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import Message
from django.urls import reverse_lazy,reverse

@csrf_exempt
def index(request):
    #postで受け取ったとき・・・
    if request.method == 'POST':
        #pythonで読み込めるように変換　辞書型のデータリストが返される
        request = json.loads(request.body.decode('utf-8'))
        #メッセージ情報はeventsキーに格納されている
        #格納されているデータは複数のメッセージ辞書を含むリスト型
        events=request['events']
        
        for event in events:
            message=event['message']#メッセージのうち一つえ
            reply_token=event['replyToken']#メッセージの暗号を返信の暗号に渡す
            line_message = LineMessage(message_creater.create_single_text_message(message['text']))
            #メッセージ辞書のtextキーを暗号と一緒に返す
            line_message.reply(reply_token)
            
        return HttpResponse('ok')
            
# Create your views here.

class HomeList(CreateView):
    model=Message
    template_name='form.html'
    fields=['medicine','detail']
    success_url=reverse_lazy('form')
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        
        context['medicinelist']=Message.objects.all()
        
        return context

class Update(UpdateView):
    model=Message
    template_name="update.html"
    fields=['medicine','detail']
    
    def get_success_url(self):
        pk=self.kwargs['pk']
        
        return reverse('update',kwargs={'pk':pk})

class Delete(DeleteView):
    model=Message
    template_name='delete.html'
    success_url=reverse_lazy('form')