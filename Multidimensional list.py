from tkinter import *
root=Tk()
root.title("Multidimensional Arrays")

root.geometry("500x500")
label= Label(root)


array_1d = ["John", "James", "Thomosan"]
print(array_1d[0])

array_2d = [["john","A"],["james","B"],["thomosan","C"]]
print(array_2d[0][1])

array_3d = [[["John","A+","Excellent"],["James","A","Very Good"],["Thomosan","B","Good"]]]
print(array_3d[0][0][2])

def report():
    label["text"] = array_3d[0][1][0] + " got grade " + array_3d[0][1][1] +" and he is doing " + array_3d[0][1][2]
    
btn = Button(root, text= "Show report", command = report)
btn.place(relx = 0.5, rely =0.5, anchor = CENTER)

label.place(relx = 0.5, rely =0.6, anchor = CENTER)

root.mainloop()
