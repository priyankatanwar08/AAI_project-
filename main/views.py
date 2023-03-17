from django.shortcuts import render
import mysql.connector as sql
pid =''
ptl =''
ptr =''
pmdid =''
cpx =''
opx =''
# Create your views here.

def submit_data(request):
    global pid,ptl,ptr,pmdid,cpx,opx
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="priyanka",database='before_approval')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="project_id":
                pid=value
            if key=="p_title":
                ptl=value
            if key=="p_tenure":
                ptr=value
            if key=="pm_dept_id":
                pmdid=value
            if key=="capex":
                cpx=value
            if key=="opex":
                opx=value
                                 
        
        c="insert into users Values('{}','{}','{}','{}','{}','{}')".format(pid,ptl,ptr,pmdid,cpx,opx)
        cursor.execute(c)
        m.commit()

    return render(request,'main.html')