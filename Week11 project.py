from tkinter import *
from tkinter.simpledialog import *
from tkinter import messagebox
import webbrowser
from random import choice

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
def play_game(player_choice):
    choices = ['가위', '바위', '보']
    computer_choice = choice(choices)

    if player_choice == computer_choice:
        result = "비겼습니다!"
    elif (
        (player_choice == '가위' and computer_choice == '보') or
        (player_choice == '바위' and computer_choice == '가위') or
        (player_choice == '보' and computer_choice == '바위')
    ):
        result = "이겼습니다!"
    else:
        result = "졌습니다!"

    messagebox.showinfo("가위바위보 게임 결과", f"플레이어: {player_choice}\n컴퓨터: {computer_choice}\n결과: {result}")


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


#이미지
Rock = PhotoImage(file="RSP/Rock.png")
Scissors = PhotoImage(file="RSP/Scissors.png")
Paper = PhotoImage(file="RSP/Paper.png")

#가위바위보
rock_button = Button(window, image=Rock, bg="#424242", command=lambda: play_game('바위'))
paper_button = Button(window, image=Paper, bg="#424242", command=lambda: play_game('보'))
scissors_button = Button(window, image=Scissors, bg="#424242", command=lambda: play_game('가위'))
rsp = Label(window, text="가위바위보 게임", bg="#1C1C1C", font="맑은고딕", fg="White",)

#Dialog 예제
Dialog1 = Label(window, text = "메모장", bg="#F7F8E0",)

#앵커
button1.pack(side= TOP, fill=X, ipadx=10, ipady=10, padx=10,pady=12)
button2.pack(side= TOP, fill=X, ipadx=10, ipady=10, padx=10,pady=12)
button3.pack(side= TOP, fill=X, ipadx=10, ipady=10, padx=10,pady=12)
button4.pack(side= TOP, fill=X, ipadx=10, ipady=10, padx=10,pady=12)
Dialog1.pack(side= TOP, fill=X, ipadx=10, ipady=10, padx=10,pady=12)

#가위바위보 앵커
rsp.pack(side= LEFT, fill=X, ipadx=10, ipady=10, padx=10,pady=12)
scissors_button.pack(side=LEFT, fill=X, ipadx=10, ipady=10, padx=10, pady=12)
rock_button.pack(side=LEFT, fill=X, ipadx=10, ipady=10, padx=10, pady=12)
paper_button.pack(side=LEFT, fill=X, ipadx=10, ipady=10, padx=10, pady=12)

window.mainloop()