from tkinter import *
from tkinter.simpledialog import *
from tkinter import messagebox
import webbrowser

#함수 선언
def place():
    messagebox.showinfo("\'Place()\'의 기능", "\'Place()\'는 위젯의 위치와 크기를 정확하게 지정하여 배치하는 방법이다. \n \n ● 위젯의 위치와 크기를 픽셀 단위로 정확하게 제어할 수 있다. \n  \n ● \'Pack()\'보다 더 자세한 제어가 필요한 경우 사용된다. \n \n ● 직접 크기와 위치를 조정해야 하므로 상대적으로 더 많은 작업이 필요다.")
def pack():
    messagebox.showinfo("\'Pack()\'의 기능", "\'Pack()\'은 위젯들을 수직 또는 수평으로 정렬하는 방법이다. \n  \n ● 위젯들이 충분한 공간이 있을 때, 위젯들이 동일한 크기로 배치된다. \n \n ● 위젯들은 부모 위젯 내에서 가능한 한 빈 공간을 채우기 위해 확장된다. \n \n ● 자동으로 크기 조절이 이루어지므로 크기를 직접 조정할 필요가 없다.")
def dialog():
    messagebox.showinfo("\'Dialog\'의 기능", "\'Dialog\'는 현재 윈도우 위에 다른 창을 띄울 때 사용한다. \n \n ● 파이썬 기본 대화상자이다. \n \n ● 데이터를 입력, 수정, 어플리케이션의 설정을 변경하는 등의 작업을 하는데 사용한다.")
def dialogTest():
    value = askstring("메모장", "메모 입력")
    Dialog1.configure(text = str(value), font="바탕체")
def open():
    webbrowser.open("https://namnambiz.notion.site/Week11-c2843dba0f454790a4fd07194430f011")
def exit():
    window.quit()
    window.destroy()

#창 설정
window = Tk()
window.title("11주차 상시과제")
window.geometry("1280x720")
window.resizable(width=False, height=False)
window.configure(bg="#1C1C1C")

#메뉴 설정
mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="Menu", menu=fileMenu)
fileMenu.add_command(label="go to Notion", command=open)

fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exit)

#버튼
button1 = Button(window, text="\'Pack()\'의 기능 설명", bg="#424242", font="맑은고딕", fg="White", command=pack)
button2 = Button(window, text="\'Place()\'의 기능 설명", bg="#424242", font="맑은고딕", fg="White",command=place)
button3 = Button(window, text="\'Dialog\'의 기능 설명", bg="#424242", font="맑은고딕", fg="White",command=dialog)
button4 = Button(window, text="\'Dialog\'의 기능 예제", bg="#424242", font="맑은고딕", fg="White",command=dialogTest)

#Dialog 예제
Dialog1 = Label(window, text = "메모장", bg="#F7F8E0",)

#앵커
button1.pack(side= TOP, fill=X, ipadx=10, ipady=10, padx=10,pady=12)
button2.pack(side= TOP, fill=X, ipadx=10, ipady=10, padx=10,pady=12)
button3.pack(side= TOP, fill=X, ipadx=10, ipady=10, padx=10,pady=12)
button4.pack(side= TOP, fill=X, ipadx=10, ipady=10, padx=10,pady=12)
Dialog1.pack(side= TOP, fill=X, ipadx=10, ipady=10, padx=10,pady=12)

window.mainloop()