from tkinter import *
import tkinter.messagebox
import stuman_studentlogin
from tkinter import ttk
import random
import time
import datetime
    



def main():
          root=Tk()
          app=Window1(root)


class Window1:
          def __init__(self,master):
                    self.master=master
                    self.master.title("Student_login")
                    self.master.geometry('1350x750+0+0')
                    self.master.config(bg='light blue')
                    self.frame=Frame(self.master,bg='light blue')
                    self.frame.pack()

                    self.Username = StringVar()
                    self.Password = StringVar()

                    self.lblTitle=Label(self.frame,text='Student Login',font=('arial',50,'bold'),bg='light blue',
                                        fg='black')

                    self.lblTitle.grid(row=0,column=0,columnspan=2,pady=40)
                    #====================================================================================================================
                    self.LoginFrame1=LabelFrame(self.frame,width=1350,height=600,font=('arrial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
                    self.LoginFrame1.grid(row=1,column=0)

                    self.LoginFrame2=LabelFrame(self.frame,width=1000,height=600,font=('arrial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
                    self.LoginFrame2.grid(row=2,column=0)
                    #=============================================Label and entry=======================================================================
                    self.lblUsername=Label(self.LoginFrame1,text='username',font=('arrial',20,'bold'),bd=22,bg='cadet blue',fg='cornsilk')
                    self.lblUsername.grid(row=0,column=0)
                    self.lblUsername=Entry(self.LoginFrame1,font=('arrial',20,'bold'),textvariable=self.Username)
                    self.lblUsername.grid(row=0,column=1)

                    self.lblPassword=Label(self.LoginFrame1,text='Password',font=('arrial',20,'bold'),bd=22,bg='cadet blue',fg='cornsilk')
                    self.lblPassword.grid(row=1,column=0)
                    self.lblPassword=Entry(self.LoginFrame1,font=('arrial',20,'bold'),show='*',textvariable=self.Password)
                    self.lblPassword.grid(row=1,column=1)


                    #=============================================buttons=======================================================================

                    self.btnLogin = Button(self.LoginFrame2,text='Login',width=17,font=('arrial',20,'bold'),command=self.new_Window)
                    self.btnLogin.grid(row=3,column=0,pady=20,padx=8)

                    self.btnReset = Button(self.LoginFrame2,text='Reset',width=17,font=('arrial',20,'bold'),command=self.Reset)
                    self.btnReset.grid(row=3,column=1,pady=20,padx=8)

                    self.btnExit = Button(self.LoginFrame2,text='Exit',width=17,font=('arrial',20,'bold'),command=self.iExit)
                    self.btnExit.grid(row=3,column=2,pady=20,padx=8)

                     #=============================================buttons=======================================================================

          

          def Reset(self):
                    self.Username.set("")
                    self.Password.set("")
                    '''self.txtUsername.focus()'''


          def iExit(self):
                    self.iExit=tkinter.messagebox.askyesno("Login system","confirm if you want to exit")
                    if self.iExit>0:
                              self.master.destroy()
                    else:
                              command=self.new_window
                              return
                    



          def new_Window(self):
                    stuman_studentlogin.main()

class Window2:
          def __init__(self,master):
                    stuman_studentlogin.main()


if __name__ == '__main__':
          main()
