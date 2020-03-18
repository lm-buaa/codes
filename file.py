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

def create():               #定义生成子窗口的函数
    def huimie1():          #定义毁灭1函数，功能为初始窗口关闭
        top.destroy()
    top=Tk()                #生成一个字窗口
    top.geometry("250x100") #大小为长为250，宽为100
    top.title('学生管理系统')  #标题为“学生管理系统”
    add=Button(text='添加成绩',command=aa)  #第一个按钮为“添加成绩”按钮
    check=Button(text='查看成绩',command=cc)  #第二个按钮为“查看成绩”按钮
    likai=Button(text='退出系统',command=huimie1)  #第三个按钮为“退出系统”按钮
    add.grid_configure(column=1,row=1,columnspan=1,rowspan=1)    #设置位置
    check.grid_configure(column=1,row=2,columnspan=1,rowspan=1)
    likai.grid_configure(column=1,row=3,columnspan=1,rowspan=1)
    top1.mainloop()
def aa():                #定义添加学生成绩的aa函数
    def huimie2():       #定义毁灭2函数，功能为把输入学生姓名的窗口关闭
        stu.destroy()
    def xingming():      #定义姓名函数，对输入的姓名进行判断
        x=s.get()        #x为输入框中输入的名字
        if x=='':        #如果x为空白，则提示“请重新输入学生姓名”
            messagebox.showerror('错误','请重新输入学生姓名')
        if x in student_list.keys():  #如果x已存在，则提示“该学生已存在”
            messagebox.showerror('错误','该学生已存在')
        if x not in student_list.keys() and x!='':  #如果x不为空白也为不存在与student_list字典中
            
            def huimie3():    #定义毁灭3函数，功能为把输入学生成绩的窗口关闭
                gra.destroy()
            
            def fenshu():     #定义分数函数，对输入的分数进行判断
                y=g.get()     #y为输入框中输入的分数
                if y=='':     #如果y为空白，则提示“请重新输入学生成绩”
                    messagebox.showerror('错误','请重新输入学生成绩')
                if int(y)<0 or int(y)>100:  #如果分数低于0或高于100，则提示“分数异常”
                    messagebox.showerror('错误','录入失败，分数异常')
                if int(y)>=0 and int(y)<=100:  #如果分数合理，则录入成功
                    messagebox.showinfo('成功','操作成功')  #提示“操作成功”
                    student_list[x]=y   #把姓名和分数添加到字典里
                    huimie3()
            messagebox.showinfo('成功','姓名已保存，请继续录入成绩')  #提示“继续下一步操作”
            huimie2()   #调用毁灭2函数，把输入学生姓名的窗口关闭
            gra=Tk()    #生成新窗口，用以输入学生分数
            gra.geometry("250x100")   #窗口大小为250x100
            gra.title('提示')  #标题为“提示”
            grade=Label(gra,text='请输入学生成绩')   #第一行为“请输入学生成绩”
            g=Entry(gra,width=10)    #第二行为输入框，长为10
            OK2=Button(gra,text='OK',command=fenshu)  #第一个按钮可调用分数函数
            cancel2=Button(gra,text='Cancel',command=huimie3)  #第二个按钮可关闭该窗口
            grade.grid_configure(column=1,row=1,columnspan=1,rowspan=1)   #设置位置
            g.grid_configure(column=1,row=2,columnspan=1,rowspan=1)
            OK2.grid_configure(column=1,row=3,columnspan=1,rowspan=1)
            cancel2.grid_configure(column=2,row=3,columnspan=1,rowspan=1)
            gra.mainloop()
    stu=Tk()   #生成新窗口，用以输入学生姓名
    stu.geometry("250x100")  #窗口大小为250x100
    stu.title('提示')  #标题为“提示”
    student=Label(stu,text='请输入学生姓名')  #第一行为“请输入学生姓名”
    s=Entry(stu,width=10)  #第二行为输入框，长为10
    OK1=Button(stu,text='OK',command=xingming)  #第一个按钮可调用姓名函数
    cancel1=Button(stu,text='Cancel',command=huimie2)  #第二个按钮可关闭该窗口

    student.grid_configure(column=1,row=1,columnspan=1,rowspan=1)  #设置位置
    s.grid_configure(column=1,row=2,columnspan=1,rowspan=1)
    OK1.grid_configure(column=1,row=3,columnspan=1,rowspan=1)
    cancel1.grid_configure(column=2,row=3,columnspan=1,rowspan=1)
    stu.mainloop()

def cc():                 #定义“查看成绩”函数
    for i in student_list.keys():   #对student_list列表中的键遍历，将其和对应的值输出
        print('姓名：',i,'  ','成绩：',student_list[i])
       
top=Tk()  #生成初始窗口
top.title('学生管理系统登陆界面')  #标题为“学生管理系统登陆界面”
un=Label(top,text='用户名：')  #第一行第一列为“用户名：”
pwd=Label(top,text='密码：')  #第二行第一列为“密码：”
uni=Entry(top,width=10)  #第一行第二列为输入框，长为10
pwdi=Entry(top,width=10)  #第二行第二列为输入框，长为10
login=Button(text='Login',command=dengru)  #第三行第一个按钮可调用登陆函数
tuichu=Button(text='退出',command=huimie)  #第三行第二个按钮可关闭该窗口

top.geometry("300x100")  #窗口大小为300x100
un.grid_configure(column=1,row=1,columnspan=1,rowspan=1)  #设置位置
pwd.grid_configure(column=1,row=2,columnspan=1,rowspan=1)
uni.grid_configure(column=2,row=1,columnspan=1,rowspan=1)
pwdi.grid_configure(column=2,row=2,columnspan=1,rowspan=1)
login.grid_configure(column=1,row=3,columnspan=1,rowspan=1)
tuichu.grid_configure(column=2,row=3,columnspan=1,rowspan=1)
top.mainloop()