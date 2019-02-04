from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import (StudentSignupForm,
                    EmployeeModelForm)
from .models import Student


def home(request):
    all_student = Student.objects.all()
    context = {
        'all_student': all_student
    }
    return render(request, 'index.html', context)


def user_login(request):
    message = None
    if request.method == "POST":
        uname = request.POST['uname']
        upsw = request.POST['psw']

        try:
            Student.objects.get(uname=uname, upass=upsw)
            return HttpResponseRedirect('/blog/')
        except(Exception):
            message = 'User id or password is incorrect!!!'
            # return redirect('/blog/login/',{
            #     'message':"User id or password is incorrect!!!"
            # })

    return render(request, 'users/user_login.html', {'message': message})


def user_signup(request):
    if request.method == "POST":
        name = request.POST['name']
        uname = request.POST['uname']
        upsw = request.POST['psw']
        uemail = request.POST['email']
        umob = request.POST['phone']
        # print("User name:",uname)
        # print("User psw:",upsw)

        st = Student(name=name,
                     uname=uname,
                     upass=upsw,
                     mob=umob,
                     email=uemail)
        st.save()
        print("Resister successfully.")
        return HttpResponseRedirect('/blog/')

    return render(request, 'users/user_signup.html')


# class LoginFormView(TemplateView):
#     pass
#     # template_name = "users/user_view_signup.html"

def signupFormView(request):
    st_form = StudentSignupForm()
    if request.method == 'POST':
        st_form = StudentSignupForm(request.POST)
        if st_form.is_valid():
            name = st_form.cleaned_data.get('name')
            print("Name:", name)
    return render(request, 'users/user_view_signup.html',
                  {
                      "st_form": st_form
                  })


def create_employee(request):
    emp = EmployeeModelForm(request.POST or None)
    if emp.is_valid():
        pass
    context = {
        'emp': emp
    }
    return render(request, 'employee.html', context)
