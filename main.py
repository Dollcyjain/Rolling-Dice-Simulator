import tkinter
import PIL.Image, PIL.ImageTk
import cv2
import random
import imutils
from pygame import mixer

SET_WIDTH = 951
SET_HEIGHT = 556
MONEY = 10000

dices = {
    11: "gallery\\images\\dice11.png",
    12: "gallery\\images\\dice12.png",
    13: "gallery\\images\\dice13.png",
    14: "gallery\\images\\dice14.png",
    15: "gallery\\images\\dice15.png",
    16: "gallery\\images\\dice16.png",
    21: "gallery\\images\\dice21.png",
    22: "gallery\\images\\dice22.png",
    23: "gallery\\images\\dice23.png",
    24: "gallery\\images\\dice24.png",
    25: "gallery\\images\\dice25.png",
    26: "gallery\\images\\dice26.png",
    31: "gallery\\images\\dice31.png",
    32: "gallery\\images\\dice32.png",
    33: "gallery\\images\\dice33.png",
    34: "gallery\\images\\dice34.png",
    35: "gallery\\images\\dice35.png",
    36: "gallery\\images\\dice36.png",
    41: "gallery\\images\\dice41.png",
    42: "gallery\\images\\dice42.png",
    43: "gallery\\images\\dice43.png",
    44: "gallery\\images\\dice44.png",
    45: "gallery\\images\\dice45.png",
    46: "gallery\\images\\dice46.png",
    51: "gallery\\images\\dice51.png",
    52: "gallery\\images\\dice52.png",
    53: "gallery\\images\\dice53.png",
    54: "gallery\\images\\dice54.png",
    55: "gallery\\images\\dice55.png",
    56: "gallery\\images\\dice56.png",
    61: "gallery\\images\\dice61.png",
    62: "gallery\\images\\dice62.png",
    63: "gallery\\images\\dice63.png",
    64: "gallery\\images\\dice64.png",
    65: "gallery\\images\\dice65.png",
    66: "gallery\\images\\dice66.png"
}
numbers = [1, 2, 3, 4, 5, 6]

def play():
    num = random.randint(1, 12)
    result1 = random.choice(numbers)
    result2 = random.choice(numbers)
    user = result1+result2
    key = int(str(result1)+str(result2))
    frame = cv2.cvtColor(cv2.imread(dices[key]), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    canvas.create_text(470, 70, fill="white", font="Times 37 bold", text=f"Your number is: {num}")
    global MONEY
    canvas.create_text(470, 450, fill="cyan2", font="Times 37 italic", text=f"Your Total Amount is: {MONEY}")
    if num == user:
        canvas.create_text(470, 140, fill="#9acd32", font="Times 37 bold", text="You Won!!")
        MONEY += 1000
    else:
        canvas.create_text(470, 140, fill="red", font="Times 37 bold", text="You lose!!")
        MONEY -= 100
    mixer.init()
    mixer.music.load("gallery\\audios\\throw.mp3")
    mixer.music.play()


window = tkinter.Tk()
window.title("Rolling Dice Simulator")
cv_img = cv2.cvtColor(cv2.imread("gallery\\images\\welcome.jpg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()
btn = tkinter.Button(window,font="Times 17 bold italic", background='red', foreground='white', text="Roll Dice >", width=50, command=play)
btn.pack()
window.mainloop()
