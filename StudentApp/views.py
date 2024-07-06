from django.shortcuts import render, redirect

from StudentApp.models import Student


# Create your views here.
def home(request):
    return render(request,'home.html')


def display_fun(request):
    s=Student.objects.all()
    s1={'s':s}
    return render(request,'displaystudent.html',s1)


def add_studs(request):
    if request.method=='GET':
        return render(request,'addstudent.html')
    else:
        student=Student()
        student.Name=request.POST['tbname']
        student.Age=request.POST['tbage']
        student.City=request.POST['tbcity']
        student.Email=request.POST['tbemail']
        student.Phone=request.POST['tbphone']
        student.save()
        return redirect('displaystudent')



def edit_studs(request,id):
    st = Student.objects.get(id=id)
    if request.method=='GET':
        d={'st':st}
        return render(request,'editstudent.html',d)
    else:
        st.Name=request.POST['tbname']
        st.Age=request.POST['tbage']
        st.City=request.POST['tbcity']
        st.Email=request.POST['tbemail']
        st.Phone=request.POST['tbphone']
        st.save()
        return redirect('displaystudent')


def delete_student(request,id):
    st = Student.objects.get(id=id)
    st.delete()
    return redirect('displaystudent')
