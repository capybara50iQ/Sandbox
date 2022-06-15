from pydoc import text
from tkinter import *
import time, random
def game(dlina):
    l1.configure(text=0)
    razm=15
    oknx=dlina
    okny=oknx
    grn=okny//razm+2
    grm=oknx//razm+2
    a=[0]*grn
    for i in range(grn):
        a[i]=[0]*grm
    for i in range (grm):
        a[i][0]=-1
        a[i][grm-1]=-1
    for j in range (grn):
        a[0][j]=-1
        a[grn-1][j]=-1
    can.configure(width=oknx+2*razm, height=okny+2*razm, bg='black')
    can.place(x=40,y=30)
    particle = can.create_rectangle(0, 0, razm, razm, fill="yellow")
    can.create_rectangle(0, 0, razm, okny+2*razm, fill="Purple",outline='Purple')
    can.create_rectangle(0, 0, oknx+2*razm, razm, fill="Purple",outline='Purple')
    can.create_rectangle(0, okny+razm, oknx+2*razm, okny+2*razm, fill="Purple",outline='Purple')
    can.create_rectangle(oknx+razm, 0, oknx+2*razm, okny+2*razm, fill="Purple",outline='Purple')
    b=[]
    recs=[]
    def fly():
        global grn,grn
        for i in range (len(b)):
            if i<len(b):
                if b[i][0]>0:
                    if a[b[i][0]][b[i][1]]==1:# sand
                        if a[b[i][0]+1][b[i][1]]==0:
                            a[b[i][0]][b[i][1]]=0
                            a[b[i][0]+1][b[i][1]]=1
                            b[i][0]+=1
                            can.move(recs[i], 0, razm)
                        elif a[b[i][0]+1][b[i][1]]==2:
                            ind = b.index([b[i][0] + 1, b[i][1]])
                            a[b[i][0]][b[i][1]]=2
                            a[b[i][0]+1][b[i][1]]=1
                            b[i][0]+=1
                            can.move(recs[i], 0, razm)
                            b[ind][0]+=-1
                            can.move(recs[ind], 0, -razm)
                        elif a[b[i][0] + 1][b[i][1]-1] == 0 and a[b[i][0]][b[i][1]-1] == 0:
                            a[b[i][0]][b[i][1]] = 0
                            a[b[i][0] + 1][b[i][1]-1] = 1
                            b[i][0] += 1
                            b[i][1]+=-1
                            can.move(recs[i], -razm, razm)
                        elif a[b[i][0] + 1][b[i][1]-1]==2 and a[b[i][0]][b[i][1]-1] != 3:
                            ind = b.index([b[i][0] + 1, b[i][1]-1])
                            a[b[i][0]][b[i][1]]=2
                            a[b[i][0] + 1][b[i][1]-1]=1
                            b[i][0]+=1
                            b[i][1] += -1
                            can.move(recs[i], -razm, razm)
                            b[ind][0]+=-1
                            b[ind][1] += +1
                            can.move(recs[ind],  razm, -razm)
                        elif a[b[i][0] + 1][b[i][1]+1] == 0 and a[b[i][0]][b[i][1]+1] == 0:
                            a[b[i][0]][b[i][1]] = 0
                            a[b[i][0] + 1][b[i][1]+1] = 1
                            b[i][0] += 1
                            b[i][1]+=1
                            can.move(recs[i], razm, razm)
                        elif a[b[i][0] + 1][b[i][1]+1]==2 and a[b[i][0]][b[i][1]+1] != 3:
                            ind = b.index([b[i][0] + 1, b[i][1]+1])
                            a[b[i][0]][b[i][1]]=2
                            a[b[i][0] + 1][b[i][1]+1]=1
                            b[i][0]+=1
                            b[i][1] +=1
                            can.move(recs[i], razm, razm)
                            b[ind][0]+=-1
                            b[ind][1] +=-1
                            can.move(recs[ind],  -razm, -razm)
                    elif a[b[i][0]][b[i][1]] == 2:      # water
                        if a[b[i][0]+1][b[i][1]]==0:
                            a[b[i][0]][b[i][1]]=0
                            a[b[i][0]+1][b[i][1]]=2
                            b[i][0]+=1
                            can.move(recs[i], 0, razm)
                        elif a[b[i][0] + 1][b[i][1]-1] == 0 and a[b[i][0]][b[i][1]-1] != 3:
                            a[b[i][0]][b[i][1]] = 0
                            a[b[i][0] + 1][b[i][1]-1] = 2
                            b[i][0] += 1
                            b[i][1]+=-1
                            can.move(recs[i], -razm, razm)
                        elif a[b[i][0] + 1][b[i][1]+1] == 0 and a[b[i][0]][b[i][1]+1] != 3:
                            a[b[i][0]][b[i][1]] = 0
                            a[b[i][0] + 1][b[i][1]+1] = 2
                            b[i][0] += 1
                            b[i][1]+=1
                            can.move(recs[i], razm, razm)
                        elif a[b[i][0]][b[i][1]-1] == 0:
                            a[b[i][0]][b[i][1]] = 0
                            a[b[i][0]][b[i][1]-1] = 2
                            b[i][1] += -1
                            can.move(recs[i], -razm, 0)
                        elif a[b[i][0]][b[i][1]+1] == 0:
                            a[b[i][0]][b[i][1]] = 0
                            a[b[i][0]][b[i][1]+1] = 2
                            b[i][1] += +1
                            can.move(recs[i], razm, 0)
                        elif a[b[i][0]+1][b[i][1]]==5:
                            ind = b.index([b[i][0]+1,b[i][1]])
                            a[b[i][0]][b[i][1]]=5
                            a[b[i][0]+1][b[i][1]]=2
                            b[i][0]+=1
                            can.move(recs[i], 0, razm)
                            b[ind][0]+=-1
                            can.move(recs[ind], 0, -razm)
                        elif a[b[i][0] + 1][b[i][1]-1]==5 and a[b[i][0]][b[i][1]-1] != 3:
                            ind = b.index([b[i][0] + 1, b[i][1]-1])
                            a[b[i][0]][b[i][1]]=5
                            a[b[i][0] + 1][b[i][1]-1]=2
                            b[i][0]+=1
                            b[i][1] += -1
                            can.move(recs[i], -razm, razm)
                            b[ind][0]+=-1
                            b[ind][1] += +1
                            can.move(recs[ind],  razm, -razm)
                        elif a[b[i][0] + 1][b[i][1]+1]==5 and a[b[i][0]][b[i][1]+1] != 3:
                            ind = b.index([b[i][0] + 1, b[i][1]+1])
                            a[b[i][0]][b[i][1]]=5
                            a[b[i][0] + 1][b[i][1]+1]=2
                            b[i][0]+=1
                            b[i][1] +=1
                            can.move(recs[i], razm, razm)
                            b[ind][0]+=-1
                            b[ind][1] +=-1
                            can.move(recs[ind],  -razm, -razm)
                    elif a[b[i][0]][b[i][1]] == 3:
                        if b[i][2]>0:
                            if b[i][2]>80:
                                pts = int(l1.cget("text"))
                                a[b[i][0]][b[i][1]] = 0
                                can.delete(recs[i])
                                recs.pop(i)
                                b.pop(i)
                                pts=pts-1
                                l1.configure(text=pts)
                            else:
                                if a[b[i][0]-1][b[i][1]]==0:
                                    randfire=random.randint(0,10)
                                    pts = int(l1.cget("text"))
                                    d = []
                                    b.append(d)
                                    firre = random.randint(0, 1)
                                    if randfire>1:
                                        if firre == 0:
                                            recs.append(can.create_rectangle(b[i][1] * razm, (b[i][0]-1) * razm, (b[i][1] + 1) * razm, b[i][0] * razm,fill="orange"))  # огонь
                                        else:
                                            recs.append(can.create_rectangle(b[i][1] * razm, (b[i][0]-1) * razm, (b[i][1] + 1) * razm, b[i][0] * razm,fill="red"))  # огонь
                                        a[b[i][0]-1][b[i][1]] = 4
                                        b[pts] = [b[i][0]-1, b[i][1], 0]
                                        pts += 1
                                        l1.configure(text=pts)
                                    else:
                                        recs.append(can.create_rectangle(b[i][1] * razm, (b[i][0]-1) * razm, (b[i][1] + 1) * razm, b[i][0] * razm,fill="grey"))  # огонь
                                        a[b[i][0]-1][b[i][1]] = 5
                                        b[pts] = [b[i][0]-1, b[i][1]]
                                        pts += 1
                                        l1.configure(text=pts)
                                elif a[b[i][0]+1][b[i][1]]==0:
                                    randfire=random.randint(0,10)
                                    pts = int(l1.cget("text"))
                                    d = []
                                    b.append(d)
                                    firre = random.randint(0, 1)
                                    if randfire>1:
                                        if firre == 0:
                                            recs.append(can.create_rectangle(b[i][1] * razm, (b[i][0]+1) * razm, (b[i][1] + 1) * razm, (b[i][0]+2) * razm,fill="orange"))  # огонь
                                        else:
                                            recs.append(can.create_rectangle(b[i][1] * razm, (b[i][0]+1) * razm, (b[i][1] + 1) * razm, (b[i][0]+2) * razm,fill="red"))  # огонь
                                        a[b[i][0]+1][b[i][1]] = 4
                                        b[pts] = [b[i][0]+1, b[i][1], 0]
                                        pts += 1
                                        l1.configure(text=pts)
                                    else:
                                        recs.append(can.create_rectangle(b[i][1] * razm, (b[i][0]+1) * razm, (b[i][1] + 1) * razm, (b[i][0]+2) * razm,fill="grey"))  # огонь
                                        a[b[i][0]+1][b[i][1]] = 5
                                        b[pts] = [b[i][0]+1, b[i][1]]
                                        pts += 1
                                        l1.configure(text=pts)
                                    
                                b[i][2] += 1
                    elif a[b[i][0]][b[i][1]] == 4:
                        b[i][2]+=1
                        brand=random.randint(2,18)
                        if b[i][2]>brand:
                            pts = int(l1.cget("text"))
                            a[b[i][0]][b[i][1]] = 0
                            can.delete(recs[i])
                            recs.pop(i)
                            b.pop(i)
                            pts=pts-1
                            l1.configure(text=pts)
                        else:
                            if a[b[i][0] - 1][b[i][1]] == 0:
                                a[b[i][0]][b[i][1]] = 0
                                a[b[i][0] - 1][b[i][1]] = 4
                                b[i][0] += -1
                                can.move(recs[i], 0, -razm)
                            elif a[b[i][0] - 1][b[i][1] - 1] == 0 and a[b[i][0]][b[i][1] - 1] != 3:
                                a[b[i][0]][b[i][1]] = 0
                                a[b[i][0] - 1][b[i][1] - 1] = 4
                                b[i][0] += -1
                                b[i][1] += -1
                                can.move(recs[i], -razm, -razm)
                            elif a[b[i][0] - 1][b[i][1] + 1] == 0 and a[b[i][0]][b[i][1] + 1] != 3:
                                a[b[i][0]][b[i][1]] = 0
                                a[b[i][0] - 1][b[i][1] + 1] = 4
                                b[i][0] += -1
                                b[i][1] += 1
                                can.move(recs[i], razm, -razm)
                            elif a[b[i][0]][b[i][1] - 1] == 0:
                                a[b[i][0]][b[i][1]] = 0
                                a[b[i][0]][b[i][1] - 1] = 4
                                b[i][1] += -1
                                can.move(recs[i], -razm, 0)
                            elif a[b[i][0]][b[i][1] + 1] == 0:
                                a[b[i][0]][b[i][1]] = 0
                                a[b[i][0]][b[i][1] + 1] = 4
                                b[i][1] += +1
                                can.move(recs[i], razm, 0)
                            if a[b[i][0] - 1][b[i][1]] == 3:   # firing wood
                                try:
                                    ind = b.index([b[i][0] - 1, b[i][1],0])
                                    b[ind][2] += 1
                                except ValueError:
                                    pass
                            elif a[b[i][0] - 1][b[i][1] - 1] == 3:
                                try:
                                    ind = b.index([b[i][0] - 1, b[i][1]-1,0])
                                    b[ind][2] += 1
                                except ValueError:
                                    pass
                            elif a[b[i][0] - 1][b[i][1] + 1] == 3:
                                try:
                                    ind = b.index([b[i][0] - 1, b[i][1]+1,0])
                                    b[ind][2] += 1
                                except ValueError:
                                    pass
                            elif a[b[i][0]][b[i][1] - 1] == 3:
                                try:
                                    ind = b.index([b[i][0], b[i][1]-1,0])
                                    b[ind][2] += 1
                                except ValueError:
                                    pass
                            elif a[b[i][0]][b[i][1] + 1] == 3:
                                try:
                                    ind = b.index([b[i][0], b[i][1]+1,0])
                                    b[ind][2] += 1
                                except ValueError:
                                    pass
                            elif a[b[i][0]+1][b[i][1]] == 3:
                                try:
                                    ind = b.index([b[i][0]+1, b[i][1],0])
                                    b[ind][2] += 1
                                except ValueError:
                                    pass
                            elif a[b[i][0]+1][b[i][1] + 1] == 3:
                                try:
                                    ind = b.index([b[i][0]+1, b[i][1]+1,0])
                                    b[ind][2] += 1
                                except ValueError:
                                    pass
                            elif a[b[i][0]+1][b[i][1] - 1] == 3:
                                try:
                                    ind = b.index([b[i][0]+1, b[i][1]-1,0])
                                    b[ind][2] += 1
                                except ValueError:
                                    pass
                            if a[b[i][0] - 1][b[i][1]] == 2:   # firing water
                                try:
                                    ind = b.index([b[i][0] - 1, b[i][1]])
                                    a[b[i][0] - 1][b[i][1]]=5
                                    can.itemconfig(recs[ind],fill="gray88")
                                except ValueError:
                                    pass
                            elif a[b[i][0] - 1][b[i][1] - 1] == 2:
                                try:
                                    ind = b.index([b[i][0] - 1, b[i][1]-1])
                                    a[b[i][0] - 1][b[i][1]-1]=5
                                    can.itemconfig(recs[ind],fill="gray88")
                                except ValueError:
                                    pass
                            elif a[b[i][0] - 1][b[i][1] + 1] == 2:
                                try:
                                    ind = b.index([b[i][0] - 1, b[i][1]+1])
                                    a[b[i][0] - 1][b[i][1]+1]=5
                                    can.itemconfig(recs[ind],fill="gray88")
                                except ValueError:
                                    pass
                            elif a[b[i][0]][b[i][1] - 1] == 2:
                                try:
                                    ind = b.index([b[i][0], b[i][1]-1])
                                    a[b[i][0]][b[i][1]-1]=5
                                    can.itemconfig(recs[ind],fill="gray88")
                                except ValueError:
                                    pass
                            elif a[b[i][0]][b[i][1] + 1] == 2:
                                try:
                                    ind = b.index([b[i][0], b[i][1]+1])
                                    a[b[i][0]][b[i][1]+1]=5
                                    can.itemconfig(recs[ind],fill="gray88")
                                except ValueError:
                                    pass
                    elif a[b[i][0]][b[i][1]] == 5:
                        brand=random.randint(2,500)
                        if 10>brand:
                            pts = int(l1.cget("text"))
                            a[b[i][0]][b[i][1]] = 0
                            can.delete(recs[i])
                            recs.pop(i)
                            b.pop(i)
                            pts=pts-1
                            l1.configure(text=pts)
                        else:
                            if a[b[i][0] - 1][b[i][1]] == 0:
                                a[b[i][0]][b[i][1]] = 0
                                a[b[i][0] - 1][b[i][1]] = 5
                                b[i][0] += -1
                                can.move(recs[i], 0, -razm)
                            elif a[b[i][0] - 1][b[i][1] - 1] == 0 and a[b[i][0]][b[i][1] - 1] != 3:
                                a[b[i][0]][b[i][1]] = 0
                                a[b[i][0] - 1][b[i][1] - 1] = 5
                                b[i][0] += -1
                                b[i][1] += -1
                                can.move(recs[i], -razm, -razm)
                            elif a[b[i][0] - 1][b[i][1] + 1] == 0 and a[b[i][0]][b[i][1] + 1] != 3:
                                a[b[i][0]][b[i][1]] = 0
                                a[b[i][0] - 1][b[i][1] + 1] = 5
                                b[i][0] += -1
                                b[i][1] += 1
                                can.move(recs[i], razm, -razm)
                            elif a[b[i][0]][b[i][1] - 1] == 0:
                                a[b[i][0]][b[i][1]] = 0
                                a[b[i][0]][b[i][1] - 1] = 5
                                b[i][1] += -1
                                can.move(recs[i], -razm, 0)
                            elif a[b[i][0]][b[i][1] + 1] == 0:
                                a[b[i][0]][b[i][1]] = 0
                                a[b[i][0]][b[i][1] + 1] = 5
                                b[i][1] += +1
                                can.move(recs[i], razm, 0)

        window.after(90, fly)
    def draw(event):
        pts=int(l1.cget("text"))
        x=event.x//razm
        y=event.y//razm
        particle=R.get()
        if a[y][x]==0:
            d=[]
            b.append(d)
            if particle == 1:
                recs.append(can.create_rectangle(x*razm, y*razm, (x+1)*razm, (y+1)*razm, fill="yellow",outline='black')) #песок
                a[y][x]=1
                b[pts] = [y, x]
            elif particle == 2:
                recs.append(can.create_rectangle(x*razm, y*razm, (x+1)*razm, (y+1)*razm, fill="blue",outline='black')) #Вода
                a[y][x]=2
                b[pts] = [y, x]
            elif particle == 3:
                recs.append(can.create_rectangle(x*razm, y*razm, (x+1)*razm, (y+1)*razm, fill="brown",outline='brown')) #дерево
                a[y][x]=3
                b[pts] = [y, x, 0]
            elif particle == 4:
                firre=random.randint(0,1)
                if firre==0:
                    recs.append(can.create_rectangle(x*razm, y*razm, (x+1)*razm, (y+1)*razm, fill="orange")) #огонь
                else:
                    recs.append(can.create_rectangle(x*razm, y*razm, (x+1)*razm, (y+1)*razm, fill="red")) #огонь
                a[y][x]=4
                b[pts] = [y, x, 0]
            else:
                recs.append(can.create_rectangle(x*razm, y*razm, (x+1)*razm, (y+1)*razm, fill="grey")) #дерево
                a[y][x]=5
                b[pts] = [y, x]
            pts += 1
        l1.configure(text=pts)
    fly()
    def drawdel(event):
        x=event.x//razm
        y=event.y//razm
        try:
            if a[y][x]!=-1:
                pts = int(l1.cget("text"))
                a[y][x] = 0
                indd=b.index([y,x,0])
                can.delete(recs[indd])
                recs.pop(indd)
                b.pop(indd)
                pts=pts-1
                l1.configure(text=pts)
        except ValueError:
            pass
    def vyh():
        window.destroy()
    def sett():
        def obnovl():
            can.delete("all")
            game(scc.get())
            window2.destroy()
        window2 = Toplevel()
        window2.title("Тирлирир2")
        window2.geometry('50x100')
        scc=Scale(window2,length=100,from_=200, to=500,orient=HORIZONTAL,resolution=20)
        scc.place(x=0,y=0)
        b1=Button(window2,text="Готово",command=obnovl)
        b1.place(x=0,y=40)
    def aa(event):
        for i in range (grn):
            print(a[i])
    m_menu=Menu()
    m_menu.add_cascade(label="settings",command=sett)
    m_menu.add_cascade(label="выход",command=vyh)
    window.config(menu=m_menu)
    R=IntVar()
    R1=Radiobutton(window,text='Песок',variable=R,value=1)
    R2=Radiobutton(window,text='Вода',variable=R,value=2)
    R3=Radiobutton(window,text='Дерево',variable=R,value=3)
    R4 = Radiobutton(window, text='Огонь', variable=R, value=4)
    R5 = Radiobutton(window, text='Дым', variable=R, value=5)
    R1.place(x=0,y=0)
    R2.place(x=70,y=0)
    R3.place(x=140,y=0)
    R4.place(x=210, y=0)
    R5.place(x=280, y=0)
    can.bind('<Control-Motion>', draw)
    can.bind('<Shift-Motion>', drawdel)
    window.bind('<Left>', aa)
    l1.place(x=oknx+2*razm+40,y=30)
    window.mainloop()
window = Tk()
window.title("Тирлирир")
window.geometry('800x800')
can = Canvas(window, width=2, height=2, bg='white')
l1 = Label(window, text='0', font=('Century Gothic', 17))
game(500)
window.mainloop()
