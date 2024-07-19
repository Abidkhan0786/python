from pymysql import *
from Admin import *
from Employee import *
def check(uid,pwd):
    con=connect(db='ducatemp',user='root',password='1101h',host='localhost')
    cur=con.cursor()
    cur.execute("select * from login where userid='%s' and passwd='%s'"%(uid,pwd))
    result=cur.fetchall()
    if(len(result)==1):
        if(result[0][3]=='admin'):
            adminFunction()
        else:
            empFunction()
    else:
        print('Username or password is wrong')
    con.close()
print('User Name')
uname=input()
print('Password') 
passwd=input()
check(uname,passwd) 