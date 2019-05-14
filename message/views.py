from django.shortcuts import render
from .models import UserMessage

# Create your views here.

"""
渲染并加载message页面
"""


def get_message_form(request):
    """
    查询操作举例
    :param request:
    :return:
    """
    # 查询所有数据
    all_message = UserMessage.objects.all()
    for message in all_message:
        print(message.name)
    # 查询单条数据,使用条件查询
    my_message = UserMessage.objects.filter(name='ylf')[0]
    return render(request, 'message.html')


def insert_message(request):
    """
    插入用户信息数据
    :param request:
    :return: null
    """
    if request.method == 'POST':
        user_message = UserMessage()
        user_message.name = request.POST['name']
        user_message.address = request.POST['address']
        user_message.email = request.POST['email']
        user_message.message = request.POST['message']
        user_message.save()
    return render(request, 'message.html')


def show_user_message(request):
    """
    显示用户的数据到页面中
    :param request:
    :return:
    """
    user_message = UserMessage.objects.filter(name='ylf2')[0]
    return render(request, 'message.html', {
        'my_message': user_message,
    })


def test(request):
    pass
