from random import sample
from unittest import result
from pymysql import *
def conn():
    con=connect(db='ducatemp',user='root',password='1101h',host='localhost')
    return con
def adddept():
    con=conn()
    cur=con.cursor()
    dno=int(input('Dept No'))
    dname=input('Dept Name')
    i=cur.execute("insert into department values(%d,'%s')"%(dno,dname))
    if(i==1):
        con.commit()
        print('Department Created')
        con.close()
def adddesignation():
    con=conn()
    cur=con.cursor()
    desig=input('Designation ')
    minsal=int(input('Minimum Salary'))
    maxsal=int(input('Maximum Salary'))
    i=cur.execute("insert into designation values('%s',%d,%d)"% (desig,minsal,maxsal))
    if(i==1):
        con.commit()
        print('Designation Created')
    con.close()
def addemployee():
    con=conn()
    cur=con.cursor()
    eno=int(input('Employee No'))
    ena=input('Employee Name ')
    desig=input('Designation ')
    dno=int(input('Dept No '))
    salary=int(input('Basic Salary '))
    addr=input('Address ')
    phone=input('Mobile No ')
    uid=input('User Name ')
    pwd=input('Password ')
    utype=input('User Type admin or employee ')
    cur.execute("select * from designation where desig='%s'"%(desig))
    result=cur.fetchall()
    min_sal=result[0][1]
    max_sal=result[0][2]
    if(salary<min_sal or salary>max_sal):
        print('Salary Must be between ',min_sal,' and ',max_sal)
    else:
        i=cur.execute("insert into master values(%d,'%s','%s',%d,%d,'%s','%s')"%(eno,ena,desig,dno,salary,addr,phone))
        if(i==1):
            j=cur.execute("insert into login values(%d,'%s','%s','%s')"%(eno,uid,pwd,utype))
            if(j==1):
                con.commit()
                print('Employee Joined')
                con.close()
def attendence():
    con=conn()
    cur=con.cursor()
    print('Employee No ')
    empno=int(input())
    print('Salary for the Month of ')
    month=input()
    print('Year ')
    year=int(input())
    print('Total days of working')
    wd=int(input())
    i=cur.execute("insert into attendence values(%d,'%s',%d,%d)"%(empno,month,year,wd))
    if(i==1):
        con.commit()
        con.close()
        print('Attendece Saved')
def updtdesignation():
    i=0
    con=conn()
    cur=con.cursor()
    print('Designation for Change Salary Range')
    desig=input()
    print('Input min or max for change Minumum oor Maximum Salary')
    flag=input()
    if(flag=='min'):
        print('Enter Minimum Salary')
        mins=int(input())
        i=cur.execute("update designation set minsal=%d where desig='%s'"%(mins,desig))
        if(i==1):
            print('Minimum Salary Changed')
            con.commit()
            con.close()
    elif(flag=='max'):
        print('Enter Maximum Salary')
        maxs=int(input())
        i=cur.execute("update designation set maxsal=%d where desig='%s'"%(maxs,desig))
        if(i==1):
            print('Maximum Salary Changed')
            con.commit()
            con.close()
def updtemployee():
    con=conn()
    cur=con.cursor()
    print('Employee No for Update')
    eno=int(input())
    print('1. Change Name\n2. Change Salary\n3. Change Designation\n4. Change Department')
    ch=int(input())
    if(ch==1):
        enam=input('New Name ')
        i=cur.execute("update master set ename='%s' where empno=%d"%(enam,eno))
        if(i==1):
            con.commit()
            print('Record Updated')
            con.close()
    elif(ch==2):
        sal=int(input('New Salary  '))
        i=cur.execute("update master set basic_salary=%d where empno=%d"%(sal,eno))
        if(i==1):
            con.commit()
            print('Record Updated')
            con.close()
    elif(ch==3):
        desig=input('New Designation ')
        i=cur.execute("update master set desig='%s' where empno=%d"%(desig,eno))
        if(i==1):
            con.commit()
            print('Record Updated')
            con.close()
    elif(ch==4):
        dno=int(input('New Dept No '))
        i=cur.execute("update master set deptno=%d where empno=%d"%(dno,eno))
        if(i==1):
            con.commit()
            print('Record Updated')
            con.close()
def showsalary():
    con=conn()
    cur=con.cursor()
    cur1=con.cursor()
    eno=int(input('Employee Number '))
    month=input('Month Name ')
    year=int(input('Year '))
    cur.execute("select * from attendence where empno=%d and month='%s' and year=%d"%(eno,month,year))
    record=cur.fetchall()
    if(len(record)==1):
        wd=record[0][3]
        cur1.execute("select * from master where empno=%d"%(eno))
        result=cur1.fetchall()
        bs=result[0][4]
        ns=bs/30*wd
    i=cur.execute("insert into salary values(%d,'%s',%d,%d)"%(eno,month,year,ns))
    if(i==1):
        con.commit()
        con.close()
    print('Name '+result[0][1]+'Designation',result[0][2])
    print('Salary for the',month,'-',year)
    print('Basic Salary',bs)
    print('Working Days',wd)
    print('Net Salary',ns)
def adminFunction():
    ans='y'
    while(ans=='y'):
        print('1. Add Dept')
        print('2. Add Designation')
        print('3. Add Employee')
        print('4. Add Attendence')
        print('5. Modify Designation')
        print('6. Modify Employee')
        print('7. Show Salary')
        print('8. Exit')
        print('Enter Choice 1..9')
        ch=int(input())
        if(ch==1):
            adddept()
        elif(ch==2):
            adddesignation()
        elif(ch==3):
            addemployee()
        elif(ch==4):
            attendence()
        elif(ch==5):
            updtdesignation()
        elif(ch==6):
            updtemployee()
        elif(ch==7):
            showsalary()
        elif(ch==8):
            exit()
        print('Are you want to continue..y/n')
        ans=input()    
    
    