from tkinter import *
from tkinter.messagebox import *
#引入tkinter及tkinter.messagebox数据库
teacher_account={'admin':{'Pwd':'123456',         #建立包含原始的用户名及密码字典
                          'Name':'Admin'},
                 'cao':{'Pwd':'99999',
                          'Name':'Cao'},
                 'zhujiao':{'Pwd':'66666',
                          'Name':'Zhujiao'}}
student_list={'BZB':100,'KSJ':99,'LQY':98,'XXY':97}   #建立包含原始姓名及其成绩的字典

def huimie():        #定义毁灭函数，把窗口关闭
    top.destroy()

def dengru():        #定义登陆函数
    x=uni.get()      #x为用户名
    y=pwdi.get()     #y为密码
    if x in teacher_account.keys():      #如果x在字典的所记录的用户名里
        if y in teacher_account[x].values():  #如果y在字典所记录的用户名所对应的密码里
            messagebox.showinfo('登陆成功','欢迎，教师'+teacher_account[x]['Name'])
            #弹出窗口，标题为“登陆成功”，标语为“欢迎，教师+其首字母大写的名字”
            huimie()   #关闭初始界面
            create()   #生成新的操作界面
    if x=='' or y=='':                     #如果未输入用户名或密码
        messagebox.showerror('登陆失败','用户名或密码为空')
        #弹出窗口，标题为“登陆失败”，标语为“用户名或密码为空”
    else:          #如果输入的用户名或密码不为空但错误
        messagebox.showerror('登陆失败','用户名或密码错误')
        #弹出窗口，标题为“登陆失败”，标语为“用户名或密码错误”