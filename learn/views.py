# coding:utf-8
from django.shortcuts import render
from django.contrib.auth import logout
from .models import Article, Classify, Comment, User, Share
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms.login import LoginForm
import hashlib
import time
import random
from .forms.login import UserRegister
from django.shortcuts import redirect
import datetime
import smtplib
from email.mime.text import MIMEText


#用户登录
def login(request):
    flag = ''
    if request.method == "POST":
        f = LoginForm(request.POST)
        if f.is_valid():
            username = f.cleaned_data["username"]
            passwd = f.cleaned_data["passwd"]
            password = take_md5(passwd)
            user = User.objects.filter(userName=username, userPassword=password)
            if user:
                request.session["name"] = username
                return redirect('/blog/')
            else:
                flag = "Your username and password didn't match. Please try again."
                return render(request, 'learn/login.html', {"title": "登录", "form": f, "flag": flag})
        else:
            return render(request, 'learn/login.html', {"title": "登录", "form": f, "error": f.errors})
    else:
        f = LoginForm()
        return render(request, 'learn/login.html', {"title": "登录", "form": f, "flag": flag})


#用户密码hash加密
def take_md5(content):
    hash = hashlib.md5()    #创建hash加密实例
    hash.update(content.encode("utf8"))    #hash加密
    result = hash.hexdigest()  #得到加密结果
    return result


#用户注册
def register(request):
    error = ''
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():

            name = form.cleaned_data["username"]
            passwd1 = form.cleaned_data["password1"]
            passwd2 = form.cleaned_data["password2"]
            phonenum = form.cleaned_data["phonenum"]
            email = form.cleaned_data["email"]

            if User.objects.filter(userName=name):
                error = 'The username has existed,please change your username'

            elif User.objects.filter(userEmail=email):
                error = 'The e-mail has existed,please change your e-mail'

            elif not form.phone_validate(phonenum):
                error = 'The phonenumber is invalid'

            elif User.objects.filter(userPhonenum=phonenum):
                error = 'The phonenumber has existed,please change your phonenumber'

            elif not form.pwd_validate(passwd1, passwd2):
                error = 'Please input the same password'
            else:
                password = take_md5(passwd1)
                token = str(time.time() + random.randrange(1, 10000))
                user = User.createuser(name, password, email, phonenum, token)
                user.save()
                return redirect("/login/")
            return render(request, 'learn/register.html', {"title": '注册', "form": form, "flag": error})
    else:
        form = UserRegister()
    return render(request, 'learn/register.html', {"title": '注册', "form": form, "flag": error})


#存放session
def base(request):
    info = {}
    # 取出session
    username = request.session.get("name", "Welcome")
    # status检查
    if username == "Welcome":
        status = "log in"
        href = "/login/"
    else:
        status = "log out"
        href = "/quit/"
    info["username"] = username
    info["status"] = status
    info["href"] = href
    return (info)


#注销账户
def quit(request):
    logout(request)
    return redirect("/login/")


#主页
def home(request):
    info = base(request)
    return render(request, 'learn/index.html', {"username": info["username"], "status": info["status"],
                                               "href": info["href"]})

def page(request, articles):
    # 倒序取出内容
    articles = articles[::-1]
    paginator = Paginator(articles, 3)
    page = request.GET.get('page')
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
        content = paginator.page(1)
    except EmptyPage:
        content = paginator.page(paginator.num_pages)
    return (content)


#博客主体
def blog(request):
    info = base(request)
    articles = Article.objects.all()
    content = page(request, articles)
    classifies = Classify.objects.all()
    return render(request, 'learn/blog.html', {"content": content, "class": classifies, "title": "Blog",
                                               "username": info["username"], "status": info["status"],
                                              "href": info["href"], "name": "Blog"})


#展示博客和处理评论（ajax）
def content(request, num):
    articles = Article.objects.get(pk=num)
    comment_list = Comment.objects.filter(article_id=num)
    comment_list = comment_list[::-1]
    classifies = Classify.objects.all()
    username = request.session.get("name", "Welcome")
    # status检查,如果username不存在，请用户登录
    if username == "Welcome":
        tips = status = "Login"
        href = "/login/"
    #否则，改成退出，信息改发送
    else:
        status = "log out"
        href = "/quit/"
        tips = "Send"

    #处理评论
    if request.is_ajax():
        username = request.session.get("name", "Welcome")
        if username == "Welcome":
            return redirect("/login/")
        else:
            comt = request.POST.get("comment")
            length = len(comt)
            if 0 < length <= 100 and comt.strip() != '':
                user = User.objects.get(userName=username)
                print(user.id)
                user_id = user.id
                date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                comment = Comment.objects.create(date=date_time, comment=comt, user_id_id=user_id, article_id_id=num)
                comment.save()

    return render(request, 'learn/showblog.html', {"details": articles, "name": "Blog", "comment_list": comment_list,
                                                   "classifies": classifies, "title": "Blog", "username": username,
                                                   "status": status, "href": href, "tips": tips})


#博客分类
def category(request, num):
    info = base(request)
    articles = Article.objects.filter(classify=num)
    content = page(request, articles)
    classifies = Classify.objects.all()
    return render(request, 'learn/blog.html', {"content": content, "class": classifies, "title": "Blog",
                                              "username": info["username"], "status": info["status"],
                                              "href": info["href"]})


#博客搜索引擎
def search(request):
    info = base(request)
    errormessage = ""
    q = request.GET.get("q")
    articles = Article.objects.filter(introduction__icontains=q)
    content = page(request, articles)
    classifies = Classify.objects.all()
    if not articles:
        errormessage = "想搜啥就搜啥，我不要面子的？？"
    return render(request, 'learn/blog.html', {"content": content, "class": classifies, "title": "Blog",
                                              "username": info["username"], "status": info["status"],
                                              "href": info["href"], "name": "Blog", "errormessage": errormessage})


#联系
def contact(request):
    info = base(request)
    test_contact(request)
    return render(request, 'learn/contact.html', {"username": info["username"], "status": info["status"],
                                                 "href": info["href"]})


#后台验证contact的name，email，message
def test_contact(request):
    if request.is_ajax():
        name = request.POST.get("name").replace(' ','')
        email = request.POST.get("email").replace(' ','')
        message = request.POST.get("message").replace(' ','')
        if len(name)*len(email)*len(message)!=0:
            post_email(name, email, message)
        else:
            print("不符合条件--------")


# 邮件发送
#coding=utf-8
def post_email(name, email, message):
    msg_from = '1102533916@qq.com'  # 发送方邮箱
    passwd = 'yhgqqlcpzhuihaai'  # 填入发送方邮箱的授权码
    msg_to = '1102533916@qq.com'  # 收件人邮箱

    subject = "Name:"+str(name)+"---From"+str(email)  # 主题改成发件人的邮箱号码
    content = str(message)  # 获取contact内容
    # 正文
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        # 邮件服务器及端口号
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("发送成功")
    except s.SMTPException as e:
        print("发送失败")
    finally:
        s.quit()


# share主体
def share(request):
    share = Share.objects.all()[::-1]
    info = base(request)
    return render(request, "learn/share.html", {"share": share, "username": info["username"], "status": info["status"],
                                                 "href": info["href"]})


def autoplay(request):
    return render(request, "learn/autoplay.html")