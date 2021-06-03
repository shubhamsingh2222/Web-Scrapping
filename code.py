import tkinter as tk
root=tk.Tk()
root.geometry("200*300")
root.title("EDUYEAR")
root.configure(bg="black")

def check():
    city=y.get()
    search = "Weather in {}".format(city)
    
    url = f"https://www.google.com/search?&q={search}"
    
    req = requests.get(url)
    
    sor = BeautifulSoup(req.text, "html.parser")
    
    temp = sor.find("div", class_='BNeawe').text
    
    g=f"temprature in {city} is",temprature
    l2.configure(text=g)
    
    y=tk.StringVar()
    el=tk.Entry(root,textvariable=y)
    l1=tk.Label(root,text="Enter City:")
    l1.place(x=10,y=5)
    e1.place(x=10,y=35,height=35,width=180)
    l2=tk.Label(root,text="",bg="black",fg="yellow")
    l2.place(x=10,y=105)
    b=tk.Button(root,text="Check",command=check)
    b.place(x=10,y=75)
    root.mainloop()
