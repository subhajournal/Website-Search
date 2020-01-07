from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from urllib.request import urlopen
from bs4 import BeautifulSoup
import socket  
import ipaddress
import webbrowser

fcol="SeaGreen1"
w1="firebrick1"
w2="blue violet"
w3="magenta2"
w4="DeepPink2"
font1="Tahoma Italic"
font2="Times New Roman bold"
font3="Tahoma bold"

def check_stat():
    try :
        stri = "https://www.google.co.in"
        data = urlopen(stri)
        return "Connected"
    except:
        return "Internet Not Connected"

def htm(link,ext):
    window = Tk()
    style = Style() 
    style.configure('W.TButton', font = 
               ('Times New Roman', 10, 'bold', 'italic'), 
                foreground = 'red',borderwidth = '4') 
    
    window.title("HTML Viewer")
    window.geometry('650x270')
    window.configure(background=w2)
    link="https://"+link+ext
    html = urlopen("http://google.co.in")
    bsObj = BeautifulSoup(html.read());
    t=Text(window,height=15, width=70)
    t.place(x=20,y=20)
    t.insert(END,bsObj)
    window.mainloop()
    
    
def search():
    
    window = Tk()
    style = Style() 
    style.configure('W.TButton', font = 
               ('Times New Roman', 10, 'bold', 'italic'), 
                foreground = 'red',borderwidth = '4') 
    
    window.title("Search Widget")
    window.geometry('700x300')
    window.configure(background=fcol)
    
    canvas = Canvas(width=300, height=300, bg=fcol)
    canvas.pack(expand=YES, fill=BOTH)                

    canvas.create_rectangle(445, 5, 650, 90, width=1, fill=fcol)
    
    show=Label(window, text="Search Widget",font=(font1,20))
    show.place(x=150,y=10)
    show.configure(background=fcol)
    
    chk=show=Label(window, text="           ",font=(font2,14))
    chk.place(x=450,y=10)
    chk.configure(background=fcol,foreground=w1)
    
    hst=show=Label(window, text="          ",font=(font2,12))
    hst.place(x=450,y=30)
    hst.configure(background=fcol,foreground=w2)
    
    ip4=show=Label(window, text="           ",font=(font2,12))
    ip4.place(x=450,y=50)
    ip4.configure(background=fcol,foreground=w3)
    
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)
    
    val=check_stat()
    chk.configure(text="Status: "+val)

    hst.configure(text="Host: "+hostname)
    ip4.configure(text="IPv4: "+str(ipaddress.ip_address(IPAddr)))
    
    lbl = Label(window, text="Search Phrase",font=(font3,10))
    lbl.place(x=50,y=100)
    lbl1 = Label(window, text="Search Link",font=(font3,10))
    lbl1.place(x=50,y=130)
    lbl.configure(background=fcol)
    lbl1.configure(background=fcol)
    
    ent = Entry(window,width=30)
    ent.place(x=150,y=100)
    ent.configure(background=fcol)
    ent1 = Entry(window,width=30)
    ent1.place(x=150,y=130)
    ent1.configure(background=fcol)
    
    allext=Combobox(window,width=7)
    allext['values']= ("Select",".com",".org",".in","co.in",".xyz",".nic.in",".co",".edu",".net",".gov",".mil")
    allext.current(0)
    allext.place(x=340,y=130)
    
    def searchweb():
        link = ent.get()
        webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % link)
    btn1 = Button(window, text="Search Web", command=searchweb,style = 'W.TButton')
    btn1.place(x=150,y=200)
    
    def showhtm():
        link = ent1.get()
        ext=allext.get()
        htm(link,ext)

    btn2 = Button(window, text="Show HTML", command=showhtm,style = 'W.TButton')
    btn2.place(x=250,y=200)
    
    def refresh():
        ent.delete(0,END)
        search()

    btn2 = Button(window, text="Refresh", command=refresh,style = 'W.TButton')
    btn2.place(x=350,y=200)
    window.mainloop()
search()
