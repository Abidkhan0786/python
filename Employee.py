from random import sample
from pymysql import *
def conn():
    con=connect(db='ducatemp',user='root',password='1101h',host='localhost')
    return con
def changepwd():
    i=0
    con=conn()
    cur=con.cursor()
    npwd=input('New password ')
    eno=int(input('Employee no to change password'))
    i=cur.execute("update login set passwd='%s' where empno=%d"%(npwd,eno))
    if(i==1):
        con.commit()
        print('Password Changed')
        con.close()
def showattendence():
    con=conn()
    cur=con.cursor()
    eno=int(input('Employee no. to show record'))
    month=input('Attendence for the month of ')
    cur.execute("select * from attendence where empno=%d and month='%s'"%(eno,month))
    record=cur.fetchall()
    year=record[0][2]
    wd=record[0][3]
    con.close()
    print('EmpNo\t\tMonth\t\tYear\t\tWorkingy_Days')
    print(eno,'\t''\t',month,'\t''\t',year,'\t''\t',wd)
def showsalary():
    con=conn()
    cur=con.cursor()
    cur1=con.cursor()
    eno=int(input('employee no'))
    month=input('Salary for the month of')
    year=int(input('enter year'))
    cur.execute("select * from master where empno=%d"%(eno))
    result=cur.fetchall()
    cur1.execute("select * from salary where empno=%d and month='%s' and year=%d"%(eno,month,year))
    record=cur1.fetchall()
    bsal=result[0][4]
    netsal=record[0][3]
    print('EmpNo \t\tMonth \t\tYear \t\t Basic_Salary\t\t Net_Salary')
    print(eno,'\t''\t',month,'\t''\t',year,'\t''\t',bsal,'\t''\t',netsal)
def empFunction():
    ans='y'
    while(ans=='y'):
        print('1. Change Password')
        print('2. Show Attendence')
        print('3. Show Salary')
        print('4. Exit')
        print('Enter Choice 1..4')
        ch=int(input())
        if(ch==1):
            changepwd()
        elif(ch==2):
            showattendence()
        elif(ch==3):
            showsalary()
        elif(ch==4):
            exit()
        print('Do you want to continue..y/n')
        ans=input()    
    
    