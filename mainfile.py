def gui():
    import tkinter as tk
    import signdetection
    import scrlmodel
    import hand_detect
    import volumeincreaser
    import finalvirmouse
    import virtualkeyboard
    sc = tk.Tk()

    def scr1():
        sc.destroy()
        hand_detect.handdetect()
        gui()


    def scr2():
        sc.destroy()
        signdetection.model_()
        gui()


    def scr3():
        sc.destroy()
        scrlmodel.model_()
        gui()

    def scr4():
        sc.destroy()
        finalvirmouse.vir_mouse()
        gui()


    def scr5():
        sc.destroy()
        volumeincreaser.volumesigndetecter()
        gui()

    def scr6():
        sc.destroy()
        virtualkeyboard.vir_kry()
        gui()


    sc.geometry("1000x4000")
    sc.configure(bg="white")
    l = tk.Label(text="WELCOME", bg="white", fg="black", font="comicsms 22 bold").pack()
    l2 = tk.Label(text="HSDCS-software", bg="white", fg="black", font="comicsms 22 bold").pack()
    l3 = tk.Label(text="HAND SIGN DETECTION CONTROL SYSTEM", bg="white", fg="black", font="comicsms 22 bold").pack()
    l4 = tk.Label(text="Forget the keyboard and mouse\n lets run everything on your fingertips", bg="white", fg="black", font="comicsms 22 bold").pack()
    l4 = tk.Label(text="To close any program press 'Esc' two times..", bg="white", fg="black",font="comicsms 18 bold").pack()

    #  1
    b1 = tk.Button(text="    HAND DETECTION    ", bg="white", fg="black",font="comicsms 25 bold", borderwidth=4, command=scr1).pack()

    # 2
    b2 = tk.Button(text="     SIGN DETECTION     ", bg="white", fg="black",font="comicsms 25 bold", borderwidth=4, command=scr2).pack()

    # 3
    b3 = tk.Button(text="             SCROLL             ", bg="white", fg="black",font="comicsms 25 bold", borderwidth=4,command=scr3).pack()

    # 4
    b4 = tk.Button(text="     VIRTUAL MOUSE       ", bg="white", fg="black",font="comicsms 25 bold", borderwidth=4,command=scr4).pack()

    # 5
    b5 = tk.Button(text="VOLUME CONTROLLER", bg="white", fg="black",font="comicsms 25 bold", borderwidth=4, command=scr5).pack()

    # 6
    b6 = tk.Button(text="   VIRTUAL KEYBOARD  ", bg="white", fg="black",font="comicsms 25 bold", borderwidth=4, command=scr6).pack()

    #  7
    b7 = tk.Button(text="                EXIT                ", bg="white", fg="black",font="comicsms 25 bold", borderwidth=4, command=sc.destroy).pack()

    sc.mainloop()


if __name__ == '__main__':
    gui()