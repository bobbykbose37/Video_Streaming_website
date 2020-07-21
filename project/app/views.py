import fnmatch
import os

from django.http import HttpResponse
from django.shortcuts import render, redirect

from project import settings
from .import models
from .models import signup,releases,discover,features,ads,add

# Create your views here.
def signupp(request):
    if request.method=="POST":
        name=request.POST["name"]
        age=request.POST["age"]
        occupation=request.POST["occupation"]
        gender=request.POST["gender"]
        email=request.POST["email"]
        password=request.POST["password"]
        secret_number=request.POST["secret_number"]
        obj=models.signup()
        obj.gender=gender
        obj.name=name
        obj.occupation=occupation
        obj.age=age
        obj.email=email
        obj.password=password
        obj.secret_number=secret_number
        obj.save()
        return redirect('signup')
    return render(request,"signup.html")

def home(request):
    obj_releases=releases.objects.all()
    obj_discover=discover.objects.all()
    obj_features=features.objects.all()
    for i in obj_releases:
        print("55555555", type(i),i.image)
    obj_ads=ads.objects.all()
    print("ccccccccount",obj_releases.count())
    obj_add=add.objects.all()
    for i in obj_add:
        linkkk=i.ad
    return render(request,"home.html",{'obj_releases':obj_releases,
                                       'count':obj_releases.count(),'obj_discover':obj_discover,
                                       'obj_ads':obj_ads,'obj_features':obj_features,'linkkk':linkkk})



def loginn(request):
    if request.method=="POST":
        name=request.POST["name"]
        password=request.POST["password"]
        obj=signup.objects.all()
        print(obj,type(obj),"hhhhhhhhhhhhhhhhhhh")
        for i in obj:
            if i.name==name:
                if i.password==password:
                    return redirect('home')
    return render(request,"login.html")


def video_page_releases(request,sid):
    obj=releases.objects.all().filter(id=sid)
    for i in obj:
        print("lllllllllllll",i.video)
        linkk="https://www.youtube.com/embed/"+str(i.video)
        print(linkk)
    return render(request,"video page.html",{'obj':obj,'linkk':linkk})

def video_page_discover(request,sid):
    obj=discover.objects.all().filter(id=sid)
    for i in obj:
        print("lllllllllllll", i.video)
        linkk = "https://www.youtube.com/embed/" + str(i.video)
        print(linkk)
    return render(request,"video page.html",{'obj':obj,'linkk':linkk})

def video_page_features(request,sid):
    obj=features.objects.all().filter(id=sid)
    for i in obj:
        print("lllllllllllll", i.video)
        linkk = "https://www.youtube.com/embed/" + str(i.video)
        print(linkk)
    return render(request,"video page.html",{'obj':obj,'linkk':linkk})

def forgot_password(request):
    if request.method=="POST":
        name=request.POST["name"]
        answer=request.POST["answer"]
        new_password=request.POST["new_password"]
        new_password2=request.POST["new_password2"]
        if new_password==new_password2:
            obj=signup.objects.get(name=name)
            if obj.secret_number==answer:
                obj.password=new_password2
                obj.save()
            return redirect('loginn')
    return render(request,"forgot_password.html")

def search(request):
    print("entered search")
    if request.method=="POST":
        search=request.POST["search"]
        obj1=releases.objects.all()
        obj2=discover.objects.all()
        obj3=features.objects.all()
        for i in obj1:
            if search==i.name:
                obj = releases.objects.all().filter(id=i.id)
                for i in obj:
                    print("lllllllllllll", i.video)
                    linkk = "https://www.youtube.com/embed/" + str(i.video)
                    print(linkk)
                return render(request, "video page.html", {'obj': obj, 'linkk': linkk})
        for i in obj2:
            if search==i.name:
                obj = discover.objects.all().filter(id=i.id)
                for i in obj:
                    print("lllllllllllll", i.video)
                    linkk = "https://www.youtube.com/embed/" + str(i.video)
                    print(linkk)
                return render(request, "video page.html", {'obj': obj, 'linkk': linkk})
        for i in obj3:
            if search==i.name:
                obj = features.objects.all().filter(id=i.id)
                for i in obj:
                    print("lllllllllllll", i.video)
                    linkk = "https://www.youtube.com/embed/" + str(i.video)
                    print(linkk)
                return render(request, "video page.html", {'obj': obj, 'linkk': linkk})
    return render(request,"forgot_password.html")

def display_video(request,vid=None):
    if vid is None:
        return HttpResponse("No Video")

    #Finding the name of video file with extension, use this if you have different extension of the videos
    video_name = ""
    for fname in os.listdir(settings.MEDIA_ROOT):
        if fnmatch.fnmatch(fname, vid+".*"): #using pattern to find the video file with given id and any extension
            video_name = fname
            break


    '''
        If you have all the videos of same extension e.g. mp4, then instead of above code, you can just use -

        video_name = vid+".mp4"

    '''

    #getting full url -
    video_url = settings.MEDIA_URL+video_name

    return render(request, "video_template.html", {"url":video_url})