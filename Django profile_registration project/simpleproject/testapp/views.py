from django.shortcuts import render
def name_view(request):
    return render(request,'testapp/name.html')
def age_view(request):
    name=request.GET['uname']
    response=render(request,'testapp/age.html',{'name':name})
    response.set_cookie('name',name)
    return response
def qualification_view(request):
    age=request.GET['uage']
    response=render(request,'testapp/qualification.html')
    response.set_cookie('age',age)
    return response
def address_view(request):
    qualification=request.GET['uqualification']
    response=render(request,'testapp/address.html')
    response.set_cookie('qualification',qualification)
    return response
def mob_view(request):
    address=request.GET['uaddress']
    response=render(request,'testapp/mob.html')
    response.set_cookie('address',address)
    return response
def gender_view(request):
    mob=request.GET['umob']
    response=render(request,'testapp/gender.html')
    response.set_cookie('mob',mob)
    return response
def email_view(request):
    gender=request.GET['ugender']
    response=render(request,'testapp/email.html')
    response.set_cookie('gender',gender)
    return response
def result_view(request):
    email=request.GET['uemail']
    name=request.COOKIES['name']
    age=request.COOKIES['age']
    qualification=request.COOKIES['qualification']
    address=request.COOKIES['address']
    mob=request.COOKIES['mob']
    gender=request.COOKIES['gender']
    #email=request.COOKIES['email']
    return render(request,'testapp/result.html',{'name':name,'age':age,'qualification':qualification,'address':address,'mob':mob,'gender':gender,'email':email})
