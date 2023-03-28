from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import mysql.connector as sql

project_title=''
budgetary_id=''
capex=''
opex=''
date_of_approval=''
fiscal_year=''
fund_center_id=''
fund_center_name=''


# Create your views here.
def signaction(request):
    global project_title,budgetary_id,capex,opex,date_of_approval,fiscal_year,fund_center_id,fund_center_name
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="lavish",database='project_management')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="project_title":
                project_title=value
            if key=="budgetary_id":
                budgetary_id=value
            if key=="capex":
                capex=value
            if key=="opex":
                opex=value
            if key=="date_of_approval":
                date_of_approval=value
            if  key=="fiscal_year":
                fiscal_year=value
            if key=="fund_center_id":
                fund_center_id=value
            if key=="fund_center_name":
                fund_center_name=value
        
        c="insert into users Values('{}','{}','{}','{}','{}','{}','{}','{}')".format(project_title,budgetary_id,capex,opex,date_of_approval,fiscal_year,fund_center_id,fund_center_name)
        cursor.execute(c)
        m.commit()

    return render(request,'form2_project_approved'.html')