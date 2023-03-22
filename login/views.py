from django.shortcuts import render
import mysql.connector as sql
m_id=''
password=''
# Create your views here.
def loginaction(request):
    global m_id,password
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="lavish",database='user')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="m_id":
                m_id=value
            if key=="password":
                password=value
        
        c="select * from users where m_id='{}' and password='{}'".format(m_id,password)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"dashboard.html") 

    return render(request,'login.html')
