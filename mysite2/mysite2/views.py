from django.http import HttpResponse
from django.shortcuts import render

get_form = '''
<form method='get' action="/test_get_form">
    姓名:<input type="text" name="uname">
    <input type='submit' value='干'>
</form>
'''

# action进入相对路径
post_form = '''
<form method='post' action="/test_post_form"> 
    姓名:<input type="text" name="uname">
    <input type='submit' value='干post'>
</form>
'''

def test_post(request):

    if request.method == 'GET':
        return HttpResponse(post_form)
    elif request.method == 'POST':
        uname = request.POST.get('uname')
        return HttpResponse('---%s post is ok----'%(uname))
    return HttpResponse('---Please use GET or POST !---')

def test_get(request):
    #测试 获取查询字符串
    #http://127.0.0.1:8000/test_get?a=100&b=200
    if request.method == 'GET':
        #获取方式1 request.GET[参数名]
        # a = request.GET['a']
        #获取方式2 request.GET.get('参数名','默认值'), 如果不给默认值 返回None
        a = request.GET.get('a')
        #获取方式3 request.GET.getlist('参数名'),在key为多个value使用该方式，返回数组
        # a = request.GET.getlist('a')
        html = 'a= %s'%(a)

        # 输出 request.GET value为数组类型，方式1与方式2会自动输出数组的最后一个值
        # g = str(dict(request.GET))
        # html = 'request.GET = %s'%(g)
        return HttpResponse(html)

        # 测试form_get
        # return HttpResponse(get_form)
    elif request.method == 'POST':
        pass
    else:
        pass
    return HttpResponse('-----test----error------')

# def sum(request):
#     if request.method == 'GET':
#         sum = 0
#         try:
#             start = int(request.GET.get('start','0'))
#             step = int(request.GET.get('step','1'))
#             stop = int(request.GET.get('stop'))
#         except Exception:
#             return HttpResponse('输入地址错误')
#         else:
#             for i in range(start,stop,step):
#                 sum += i
#             info = '结果: %s'%(sum)
#             return HttpResponse(info)

def sum_view(request):
    if request.method == 'GET':
        try:
            start = int(request.GET.get('start', '0'))
            step = int(request.GET.get('step', '1'))
            stop = request.GET.get('stop')
            if not stop:
                return HttpResponse('输入地址错误')
            else:
                stop = int(stop)
                # for i in range(start, stop, step):
                #     sum += i
                mysum = sum(range(start,stop,step))
                info = '结果: %s' % (mysum)
                return HttpResponse(info)
        except Exception as e:
            print('sum error is %s'%(e))
            return HttpResponse('Please use normal input')
        # return HttpResponse('请求错误')

def test_login_html(request):
    # #1 导入loader
    # from django.template import loader
    # #2 通过loader加载模板
    # t = loader.get_template('login.html')
    # #3 执行render 转化成字符串
    # html = t.render({'name':'huhaidi'})
    # #将内容响应给浏览器
    # return HttpResponse(html)

    #方案2
    from django.shortcuts import render
    return render(request,'login.html',{'name':'huhaidi'})

def say_hi():
    return 'Hi everyone'

def test_html(request):
    dic = {}
    dic['str'] = 'huhaidi'
    dic['lst'] = ['北京','上海','天津']
    dic['d'] = {'name':'huhaidi','age':18}
    dic['say_hi'] = say_hi
    dic['class_obj'] = Dog()

    return render(request,'test_html.html',dic) #传进去的一定是个字典

class Dog:
    def say(self):
        return 'wang wang!'

def test_if(request):
    dic = {'x':-5}
    return render(request,'test_if.html',dic)

def my_cal(request):
    # get 访问 获取页面
    if request.method == 'GET':
        return render(request,'mycal.html')
    elif request.method == 'POST':
        dic = {}
        x = int(request.POST.get('x',0))
        y = int(request.POST.get('y',0))
        op = request.POST.get('op')
        result = 0
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            result = x / y
        # dic['result'] = result
        # dic['op'] = op
        # dic['x'] = x
        # dic['y'] = y
        # return render(request, 'mycal.html', dic)
        return render(request, 'mycal.html', locals()) #看情况使用，可能会传一些无用的参数
    return HttpResponse('Please use GET or POST')

def test_base(request):
    return render(request,'base.html')

def test_music(request):
    return render(request,'music.html')

def test_sport(request):
    return render(request,'sport.html')








