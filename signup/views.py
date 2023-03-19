from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import mysql.connector as sql
m_id=''
email=''
first_name=''
last_name=''
dept_name=''
dept_id=''
location=''
password=''

# Create your views here.
def signaction(request):
    global m_id,email,first_name,last_name,dept_name,dept_id,location,password
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="lavish",database='user')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="m_id":
                m_id=value
            if key=="email":
                email=value
            if key=="first_name":
                first_name=value
            if key=="last_name":
                last_name=value
            if key=="dept_name":
                dept_name=value
            if  key=="dept_id":
                dept_id=value
            if key=="location":
                location=value
            if key=="password":
                password=value
        
        c="insert into users Values('{}','{}','{}','{}','{}','{}','{}','{}')".format(m_id,email,first_name,last_name,dept_name,dept_id,location,password)
        cursor.execute(c)
        m.commit()

    return render(request,'signup.html')
