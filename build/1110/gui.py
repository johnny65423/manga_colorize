
# https://github.com/ParthJadhav/Tkinter-Designer
import os, shutil
import glob
import numpy as np
from PIL import Image, ImageTk
#import sketch as sk
# noinspection PyInterpreter
print("load model...")
import Pic2Sketch as ps
#import sketch as sk
import grayscale2 as gc
import colorimage2 as ci
import matplotlib.pyplot as plt
import matplotlib
from skimage.color import rgb2lab, lab2rgb
import windnd
print("done.")
if os.path.exists(".imagetemp") :
	shutil.rmtree(".imagetemp")
os.mkdir(".imagetemp")
# 以上導入上色所需的函式庫 ##################################################################################################
import time
from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog
import tkinter as tk
counter = 0
if __name__ == "__main__":
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window = Tk()
    window.geometry("1280x720")
    window.configure(bg = "#CFF0FF")
    window.iconbitmap("icon.ico")
    window.title("Mange Colorization")

    welcomeFrame = tk.Frame(window) # 歡迎介面
    aboutFrame = tk.Frame(window) # 關於介面
    instructionFrame = tk.Frame(window) # 說明介面
    runFrame = tk.Frame(window) # 執行介面
    # 以下是歡迎介面的設計 #################################################################################################
    canvas = Canvas(
        welcomeFrame,
        bg = "#CFF0FF",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    button_image_1 = PhotoImage( # 開始探索
        file=relative_to_assets("button_1.png"))
    button_image_1_click = PhotoImage( # 開始探索_click
        file=relative_to_assets("button_1_click.png"))
    button_1 = Button(
        welcomeFrame,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: button_1_change_to_runFrame(),
        relief="flat",
        bg="#D1F0FF",
        activebackground="#D1F0FF"
    )
    button_1.place(
        x=160.0,
        y=450.0,
        width=240.0,
        height=240.0
    )
    def button_1_hover(e):
        button_1["image"] = button_image_1_click
        print("開始探索")
    def button_1_hover_leave(e):
        button_1["image"] = button_image_1
    button_1.bind("<Enter>", button_1_hover)
    button_1.bind("<Leave>", button_1_hover_leave)
    def button_1_change_to_runFrame():
        runFrame.pack(fill='both', expand=1)
        welcomeFrame.forget()
        print("點擊開始探索")

    button_image_2 = PhotoImage( # 關於
        file=relative_to_assets("button_2.png"))
    button_image_2_click = PhotoImage( # 關於_click
        file=relative_to_assets("button_2_click.png"))
    button_2 = Button(
        welcomeFrame,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: button_2_change_to_aboutFrame(),
        relief="flat",
        bg="#D1F0FF",
        activebackground="#D1F0FF"
    )
    button_2.place(
        x=640.0,
        y=450.0,
        width=240.0,
        height=240.0
    )
    def button_2_hover(e):
        button_2["image"] = button_image_2_click
        print("關於")
    def button_2_hover_leave(e):
        button_2["image"] = button_image_2
    button_2.bind("<Enter>", button_2_hover)
    button_2.bind("<Leave>", button_2_hover_leave)
    def button_2_change_to_aboutFrame():
        aboutFrame.pack(fill='both', expand=1)
        welcomeFrame.forget()
        print("點擊關於")

    button_image_3 = PhotoImage( # 離開
        file=relative_to_assets("button_3.png"))
    button_image_3_click = PhotoImage( # 離開_click
        file=relative_to_assets("button_3_click.png"))
    button_3 = Button(
        welcomeFrame,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: button_3_exit(window),
        relief="flat",
        bg="#D1F0FF",
        activebackground="#D1F0FF"
    )
    button_3.place(
        x=880.0,
        y=450.0,
        width=240.0,
        height=240.0
    )
    def button_3_hover(e):
        button_3["image"] = button_image_3_click
        print("離開")
    def button_3_hover_leave(e):
        button_3["image"] = button_image_3
    button_3.bind("<Enter>", button_3_hover)
    button_3.bind("<Leave>", button_3_hover_leave)
    def button_3_exit(window):
        print("點擊離開")
        window.destroy()

    button_image_4 = PhotoImage( # 使用說明
        file=relative_to_assets("button_4.png"))
    button_image_4_click = PhotoImage( # 使用說明_click
        file=relative_to_assets("button_4_click.png"))
    button_4 = Button(
        welcomeFrame,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: button_4_change_to_instructionFrame(),
        relief="flat",
        bg="#D1F0FF",
        activebackground="#D1F0FF"
    )
    button_4.place(
        x=400.0,
        y=450.0,
        width=240.0,
        height=240.0
    )
    def button_4_hover(e):
        button_4["image"] = button_image_4_click
        print("使用說明")
    def button_4_hover_leave(e):
        button_4["image"] = button_image_4
    button_4.bind("<Enter>", button_4_hover)
    button_4.bind("<Leave>", button_4_hover_leave)
    def button_4_change_to_instructionFrame():
        instructionFrame.pack(fill='both', expand=1)
        welcomeFrame.forget()
        print("點擊使用說明")

    image_image_1 = PhotoImage( # 調色盤圖示
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        640.0,
        200.0,
        image=image_image_1
    )
    # 以上是歡迎介面的設計 ################################################################################################
    # 以下是關於介面的設計 ################################################################################################
    canvas2 = Canvas(
        aboutFrame,
        bg="#CFF0FF",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas2.place(x=0, y=0)
    canvas2.create_rectangle(
        100.0,
        134.0,
        564.0,
        670.0,
        fill="#F5FFE9",
        outline="")

    canvas2.create_rectangle(
        666.0,
        134.0,
        1130.0,
        520.0,
        fill="#FFDDDD",
        outline="")

    canvas2.create_rectangle(
        666.0,
        520.0,
        1130.0,
        670.0,
        fill="#FEFFDA",
        outline="")
    image2_image_1 = PhotoImage( # 作品簡介
        file=relative_to_assets("image2_1.png"))
    image2_1 = canvas2.create_image(
        100.0,
        100.0,
        image=image2_image_1
    )

    image2_image_2 = PhotoImage( # 參與人員
        file=relative_to_assets("image2_2.png"))
    image2_2 = canvas2.create_image(
        666.0,
        484.0,
        image=image2_image_2
    )

    image2_image_3 = PhotoImage( # 作品簡介的文字
        file=relative_to_assets("image2_3.png"))
    image2_3 = canvas2.create_image(
        332.0,
        341.0,
        image=image2_image_3
    )

    image2_image_4 = PhotoImage( # 參與人員的文字
        file=relative_to_assets("image2_4.png"))
    image2_4 = canvas2.create_image(
        913.0,
        603.0,
        image=image2_image_4
    )

    image2_image_5 = PhotoImage( # 設計理念的文字
        file=relative_to_assets("image2_5.png"))
    image2_5 = canvas2.create_image(
        898.0,
        305.0,
        image=image2_image_5
    )

    image2_image_6 = PhotoImage( # 設計理念
        file=relative_to_assets("image2_6.png"))
    image2_6 = canvas2.create_image(
        666.0,
        100.0,
        image=image2_image_6
    )

    image2_image_7 = PhotoImage( # 版權聲明
        file=relative_to_assets("image2_7.png"))
    image2_6 = canvas2.create_image(
        666.0,
        17.0,
        image=image2_image_7
    )

    button2_image_1 = PhotoImage( # 返回
        file=relative_to_assets("button2_1.png"))
    button2_image_1_click = PhotoImage(
        file=relative_to_assets("button2_1_click.png"))
    button2_1 = Button(
        aboutFrame,
        image=button2_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: button2_1_change_to_welcomeFrame(),
        relief="flat",
        bg="#D1F0FF",
        activebackground="#D1F0FF"
    )
    button2_1.place(
        x=1150.0,
        y=590.0,
        width=130.0,
        height=130.0
    )
    def button2_1_hover(e):
        button2_1["image"] = button2_image_1_click
        print("返回")
    def button2_1_hover_leave(e):
        button2_1["image"] = button2_image_1
    button2_1.bind("<Enter>", button2_1_hover)
    button2_1.bind("<Leave>", button2_1_hover_leave)
    def button2_1_change_to_welcomeFrame():
        welcomeFrame.pack(fill='both', expand=1)
        aboutFrame.forget()
        print("點擊返回")

    welcomeFrame.pack(fill='both', expand=1)
    # 以上是關於介面的設計 ################################################################################################
    # 以下是說明介面的設計 ################################################################################################
    canvas3 = Canvas(
        instructionFrame,
        bg="#CFF0FF",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas3.place(x=0, y=0)
    image3_image_0 = None
    image3_0 = None
    image3_image_1 = PhotoImage( # 對話框：你好，我是上色AI...
        file=relative_to_assets("instruction_image_1.png"))
    image3_1 = canvas3.create_image(
        680.0,
        140.0,
        image=image3_image_1
    )

    image3_image_2 = PhotoImage( # 人物立繪
        file=relative_to_assets("instruction_image_2.png"))
    image3_2 = canvas3.create_image(
        1080.0,
        360.0,
        image=image3_image_2
    )

    button3_image_1 = PhotoImage( # 返回
        file=relative_to_assets("instruction_button_1.png"))
    button3_image_1_click = PhotoImage( # 返回_click
        file=relative_to_assets("instruction_button_1_click.png"))
    button3_1 = Button(
        instructionFrame,
        image=button3_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: button3_1_change_to_welcomeFrame(),
        relief="flat",
        bg="#D1F0FF",
        activebackground="#D1F0FF"
    )
    button3_1.place(
        x=0.0,
        y=590.0,
        width=130.0,
        height=130.0
    )
    def button3_1_hover(e):
        button3_1["image"] = button3_image_1_click
        print("返回")
    def button3_1_hover_leave(e):
        button3_1["image"] = button3_image_1

    button3_1.bind("<Enter>", button3_1_hover)
    button3_1.bind("<Leave>", button3_1_hover_leave)

    def button3_1_change_to_welcomeFrame():
        welcomeFrame.pack(fill='both', expand=1)
        instructionFrame.forget()
        print("點擊返回")

    button3_image_2 = PhotoImage( # 操作說明
        file=relative_to_assets("instruction_button_2.png"))
    button3_image_2_resize = PhotoImage( # 操作說明_click
        file=relative_to_assets("instruction_button_2_resize.png"))
    button3_2 = Button(
        instructionFrame,
        image=button3_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("點擊操作說明"),
        relief="flat",
        bg="#D1F0FF",
        activebackground="#D1F0FF"
    )
    button3_2.place(
        x=155.0,
        y=51.0,
        width=300.0,
        height=120.0
    )
    def button3_2_hover(e):
        button3_2["image"] = button3_image_2_resize
        print("操作說明")
    def button3_2_hover_leave(e):
        button3_2["image"] = button3_image_2
    def nextFunction_button3_2(e):
        global canvas3, image3_image_1, image3_1, image3_image_0, image3_0, counter
        if counter == 0:
            image3_image_0 = PhotoImage(
                file=relative_to_assets("001_display.png"))
            image3_0 = canvas3.create_image(
                400.0,
                420.0,
                image=image3_image_0
            )
            image3_image_1 = PhotoImage(
                file=relative_to_assets("001_dialog.png"))
            image3_1 = canvas3.create_image(
                680.0,
                140.0,
                image=image3_image_1
            )
        elif counter == 1:
            image3_image_0 = PhotoImage(
                file=relative_to_assets("002_display.png"))
            image3_0 = canvas3.create_image(
                400.0,
                420.0,
                image=image3_image_0
            )
            image3_image_1 = PhotoImage(
                file=relative_to_assets("002_dialog.png"))
            image3_1 = canvas3.create_image(
                680.0,
                140.0,
                image=image3_image_1
            )
        elif counter == 2:
            image3_image_0 = PhotoImage(
                file=relative_to_assets("003_display.png"))
            image3_0 = canvas3.create_image(
                400.0,
                420.0,
                image=image3_image_0
            )
            image3_image_1 = PhotoImage(
                file=relative_to_assets("003_dialog.png"))
            image3_1 = canvas3.create_image(
                680.0,
                140.0,
                image=image3_image_1
            )
        elif counter == 3:
            image3_image_0 = PhotoImage(
                file=relative_to_assets("004_display.png"))
            image3_0 = canvas3.create_image(
                400.0,
                420.0,
                image=image3_image_0
            )
            image3_image_1 = PhotoImage(
                file=relative_to_assets("004_dialog.png"))
            image3_1 = canvas3.create_image(
                680.0,
                140.0,
                image=image3_image_1
            )
        elif counter == 4:
            image3_image_0 = None
            image3_0 = None
            image3_image_1 = PhotoImage(
                file=relative_to_assets("instruction_image_1.png"))
            image3_1 = canvas3.create_image(
                680.0,
                140.0,
                image=image3_image_1
            )
            button3_1.place(
                x=0.0,
                y=590.0,
                width=130.0,
                height=130.0
            )
            button3_2.place(
                x=155.0,
                y=51.0,
                width=300.0,
                height=120.0
            )
            button3_3.place(
                x=155.0,
                y=217.0,
                width=300.0,
                height=120.0
            )
            button3_4.place(
                x=155.0,
                y=383.0,
                width=300.0,
                height=120.0
            )
            button3_5.place(
                x=155.0,
                y=549.0,
                width=300.0,
                height=120.0
            )
            counter = 0
            window.unbind("<ButtonRelease>")
            return
        counter = counter + 1
    def startInstruction(e):
        global canvas3, image3_image_1, image3_1
        image3_image_1 = PhotoImage(
            file=relative_to_assets("000_dialog.png"))
        image3_1 = canvas3.create_image(
            680.0,
            140.0,
            image=image3_image_1
        )
        button3_1.place_forget()
        button3_2.place_forget()
        button3_3.place_forget()
        button3_4.place_forget()
        button3_5.place_forget()
        window.bind("<ButtonRelease>", nextFunction_button3_2)

    button3_2.bind("<Enter>", button3_2_hover)
    button3_2.bind("<Leave>", button3_2_hover_leave)
    button3_2.bind("<ButtonRelease>", startInstruction)

    button3_image_3 = PhotoImage( # 上色模型
        file=relative_to_assets("instruction_button_3.png"))
    button3_image_3_resize = PhotoImage( # 上色模型_click
        file=relative_to_assets("instruction_button_3_resize.png"))
    button3_3 = Button(
        instructionFrame,
        image=button3_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("點擊上色模型"),
        relief="flat",
        bg="#D1F0FF",
        activebackground="#D1F0FF"
    )
    button3_3.place(
        x=155.0,
        y=217.0,
        width=300.0,
        height=120.0
    )
    def button3_3_hover(e):
        button3_3["image"] = button3_image_3_resize
        print("上色模型")
    def button3_3_hover_leave(e):
        button3_3["image"] = button3_image_3
    def nextFunction_button3_3(e):
        global canvas3, image3_image_1, image3_1, image3_image_0, image3_0, counter
        if counter == 0:
            image3_image_0 = PhotoImage(
                file=relative_to_assets("001_model_display.png"))
            image3_0 = canvas3.create_image(
                400.0,
                420.0,
                image=image3_image_0
            )
            image3_image_1 = PhotoImage(
                file=relative_to_assets("001_model.png"))
            image3_1 = canvas3.create_image(
                680.0,
                140.0,
                image=image3_image_1
            )
        elif counter == 1:
            image3_image_0 = PhotoImage(
                file=relative_to_assets("002_model_display.png"))
            image3_0 = canvas3.create_image(
                400.0,
                420.0,
                image=image3_image_0
            )
            image3_image_1 = PhotoImage(
                file=relative_to_assets("002_model.png"))
            image3_1 = canvas3.create_image(
                680.0,
                140.0,
                image=image3_image_1
            )
        elif counter == 2:
            image3_image_0 = PhotoImage(
                file=relative_to_assets("003_model_display.png"))
            image3_0 = canvas3.create_image(
                400.0,
                420.0,
                image=image3_image_0
            )
            image3_image_1 = PhotoImage(
                file=relative_to_assets("003_model.png"))
            image3_1 = canvas3.create_image(
                680.0,
                140.0,
                image=image3_image_1
            )
        elif counter == 3:
            image3_image_0 = PhotoImage(
                file=relative_to_assets("004_model_display.png"))
            image3_0 = canvas3.create_image(
                400.0,
                420.0,
                image=image3_image_0
            )
            image3_image_1 = PhotoImage(
                file=relative_to_assets("004_model.png"))
            image3_1 = canvas3.create_image(
                680.0,
                140.0,
                image=image3_image_1
            )
        elif counter == 4:
            image3_image_0 = None
            image3_0 = None
            image3_image_1 = PhotoImage(
                file=relative_to_assets("instruction_image_1.png"))
            image3_1 = canvas3.create_image(
                680.0,
                140.0,
                image=image3_image_1
            )
            button3_1.place(
                x=0.0,
                y=590.0,
                width=130.0,
                height=130.0
            )
            button3_2.place(
                x=155.0,
                y=51.0,
                width=300.0,
                height=120.0
            )
            button3_3.place(
                x=155.0,
                y=217.0,
                width=300.0,
                height=120.0
            )
            button3_4.place(
                x=155.0,
                y=383.0,
                width=300.0,
                height=120.0
            )
            button3_5.place(
                x=155.0,
                y=549.0,
                width=300.0,
                height=120.0
            )
            counter = 0
            window.unbind("<ButtonRelease>")
            return
        counter = counter + 1
    def startModel(e):
        global canvas3, image3_image_1, image3_1
        global canvas3, image3_image_1, image3_1
        image3_image_1 = PhotoImage(
            file=relative_to_assets("000_model.png"))
        image3_1 = canvas3.create_image(
            680.0,
            140.0,
            image=image3_image_1
        )
        button3_1.place_forget()
        button3_2.place_forget()
        button3_3.place_forget()
        button3_4.place_forget()
        button3_5.place_forget()
        window.bind("<ButtonRelease>", nextFunction_button3_3)

    button3_3.bind("<Enter>", button3_3_hover)
    button3_3.bind("<Leave>", button3_3_hover_leave)
    button3_3.bind("<ButtonRelease>", startModel)

    button3_image_4 = PhotoImage( # 上色資料集
        file=relative_to_assets("instruction_button_4.png"))
    button3_image_4_resize = PhotoImage( # 上色資料集_click
        file=relative_to_assets("instruction_button_4_resize.png"))
    button3_4 = Button(
        instructionFrame,
        image=button3_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("點擊上色資料集"),
        relief="flat",
        bg="#D1F0FF",
        activebackground="#D1F0FF"
    )
    button3_4.place(
        x=155.0,
        y=383.0,
        width=300.0,
        height=120.0
    )
    def button3_4_hover(e):
        button3_4["image"] = button3_image_4_resize
        print("上色資料集")
    def button3_4_hover_leave(e):
        button3_4["image"] = button3_image_4
    def nextFunction_button3_4(e):
        global canvas3, image3_image_1, image3_1, image3_image_0, image3_0, counter
        if counter == 0:
            image3_image_0 = PhotoImage(
                file=relative_to_assets("001_dataset_display.png"))
            image3_0 = canvas3.create_image(
                400.0,
                420.0,
                image=image3_image_0
            )
            image3_image_1 = PhotoImage(
                file=relative_to_assets("001_dataset.png"))
            image3_1 = canvas3.create_image(
                680.0,
                140.0,
                image=image3_image_1
            )
        elif counter == 1:
            image3_image_0 = PhotoImage(
                file=relative_to_assets("002_dataset_display.png"))
            image3_0 = canvas3.create_image(
                400.0,
                420.0,
                image=image3_image_0
            )
            image3_image_1 = PhotoImage(
                file=relative_to_assets("002_dataset.png"))
            image3_1 = canvas3.create_image(
                680.0,
                140.0,
                image=image3_image_1
            )
        elif counter == 2:
            image3_image_0 = None
            image3_0 = None
            image3_image_1 = PhotoImage(
                file=relative_to_assets("instruction_image_1.png"))
            image3_1 = canvas3.create_image(
                680.0,
                140.0,
                image=image3_image_1
            )
            button3_1.place(
                x=0.0,
                y=590.0,
                width=130.0,
                height=130.0
            )
            button3_2.place(
                x=155.0,
                y=51.0,
                width=300.0,
                height=120.0
            )
            button3_3.place(
                x=155.0,
                y=217.0,
                width=300.0,
                height=120.0
            )
            button3_4.place(
                x=155.0,
                y=383.0,
                width=300.0,
                height=120.0
            )
            button3_5.place(
                x=155.0,
                y=549.0,
                width=300.0,
                height=120.0
            )
            counter = 0
            window.unbind("<ButtonRelease>")
            return
        counter = counter + 1
    def startDataset(e):
        global canvas3, image3_image_1, image3_1
        global canvas3, image3_image_1, image3_1
        image3_image_1 = PhotoImage(
            file=relative_to_assets("000_dataset.png"))
        image3_1 = canvas3.create_image(
            680.0,
            140.0,
            image=image3_image_1
        )
        button3_1.place_forget()
        button3_2.place_forget()
        button3_3.place_forget()
        button3_4.place_forget()
        button3_5.place_forget()
        window.bind("<ButtonRelease>", nextFunction_button3_4)

    button3_4.bind("<Enter>", button3_4_hover)
    button3_4.bind("<Leave>", button3_4_hover_leave)
    button3_4.bind("<ButtonRelease>", startDataset)

    button3_image_5 = PhotoImage( # 聊天
        file=relative_to_assets("instruction_button_5.png"))
    button3_image_5_resize = PhotoImage( # 聊天_click
        file=relative_to_assets("instruction_button_5_resize.png"))
    button3_5 = Button(
        instructionFrame,
        image=button3_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("點擊聊天"),
        relief="flat",
        bg="#D1F0FF",
        activebackground="#D1F0FF"
    )
    button3_5.place(
        x=155.0,
        y=549.0,
        width=300.0,
        height=120.0
    )
    def button3_5_hover(e):
        button3_5["image"] = button3_image_5_resize
        print("聊天")
    def button3_5_hover_leave(e):
        button3_5["image"] = button3_image_5

    button3_5.bind("<Enter>", button3_5_hover)
    button3_5.bind("<Leave>", button3_5_hover_leave)

    # 以上是說明介面的設計 ################################################################################################
    # 以下是執行介面的設計 ################################################################################################
    imgpath = "" # 紀錄圖片的路徑
    imgindex = 0 # 紀錄資料夾內圖片的index
    canvas4 = Canvas(
        runFrame,
        bg="#CFF0FF",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas4.place(x=0, y=0)
    image4_image_1 = PhotoImage(
        file=relative_to_assets("image4_1.png"))

    #image4_image_1 = PhotoImage(file=relative_to_assets("0002.png"))

    image4_1 = canvas4.create_image(
        183.0,
        246.0,
        image=image4_image_1
    )

    image4_image_2 = PhotoImage(
        file=relative_to_assets("image4_2.png"))
    image4_2 = canvas4.create_image(
        488.0,
        246.0,
        image=image4_image_2
    )

    image4_image_3 = PhotoImage(
        file=relative_to_assets("image4_3.png"))
    image4_3 = canvas4.create_image(
        793.0,
        246.0,
        image=image4_image_3
    )

    image4_image_4 = PhotoImage(
        file=relative_to_assets("image4_4.png"))
    image4_4 = canvas4.create_image(
        1098.0,
        246.0,
        image=image4_image_4
    )

    image4_image_5 = PhotoImage(
        file=relative_to_assets("image4_5.png"))
    image4_5 = canvas4.create_image(
        335.0,
        246.0,
        image=image4_image_5
    )

    image4_image_6 = PhotoImage(
        file=relative_to_assets("image4_6.png"))
    image4_6 = canvas4.create_image(
        640.0,
        246.0,
        image=image4_image_6
    )

    image4_image_7 = PhotoImage(
        file=relative_to_assets("image4_7.png"))
    image4_7 = canvas4.create_image(
        945.0,
        246.0,
        image=image4_image_7
    )

    image4_image_8 = PhotoImage(
        file=relative_to_assets("image4_8.png"))
    image4_8 = canvas4.create_image(
        335.0,
        580.0,
        image=image4_image_8
    )

    button4_image_1 = PhotoImage(
        file=relative_to_assets("button4_1.png"))
    button4_1 = Button(
        runFrame,
        image=button4_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button4_1 clicked"),
        relief="flat",
        bg="#F0FAFF",
        activebackground="#F0FAFF"
    )  # #D1F0FF
    button4_1.place(
        x=49.0,
        y=500.0,
        width=90.0,
        height=90.0
    )

    button4_image_2 = PhotoImage(
        file=relative_to_assets("button4_2.png"))
    button4_2 = Button(
        runFrame,
        image=button4_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button4_2 clicked"),
        relief="flat",
        bg="#F0FAFF",
        activebackground="#F0FAFF"
    )
    button4_2.place(
        x=139.0,
        y=500.0,
        width=90.0,
        height=90.0
    )

    button4_image_3 = PhotoImage(
        file=relative_to_assets("button4_3.png"))
    button4_3 = Button(
        runFrame,
        image=button4_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button4_3 clicked"),
        relief="flat",
        bg="#F0FAFF",
        activebackground="#F0FAFF"
    )
    button4_3.place(
        x=229.0,
        y=500.0,
        width=90.0,
        height=90.0
    )

    button4_image_4 = PhotoImage(
        file=relative_to_assets("button4_4.png"))
    button4_4 = Button(
        runFrame,
        image=button4_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button4_4 clicked"),
        relief="flat",
        bg="#F0FAFF",
        activebackground="#F0FAFF"
    )
    button4_4.place(
        x=50.0,
        y=590.0,
        width=90.0,
        height=90.0
    )

    button4_image_5 = PhotoImage(
        file=relative_to_assets("button4_5.png"))
    button4_5 = Button(
        runFrame,
        image=button4_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button4_5 clicked"),
        relief="flat",
        bg="#F0FAFF",
        activebackground="#F0FAFF"
    )
    button4_5.place(
        x=140.0,
        y=590.0,
        width=90.0,
        height=90.0
    )

    button4_image_6 = PhotoImage(
        file=relative_to_assets("button4_6.png"))
    button4_6 = Button(
        runFrame,
        image=button4_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button4_6 clicked"),
        relief="flat",
        bg="#F0FAFF",
        activebackground="#F0FAFF"
    )
    button4_6.place(
        x=230.0,
        y=590.0,
        width=90.0,
        height=90.0
    )

    button4_image_7 = PhotoImage(
        file=relative_to_assets("button4_7.png"))
    button4_7 = Button(
        runFrame,
        image=button4_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button4_7 clicked"),
        relief="flat",
        bg="#F0FAFF",
        activebackground="#F0FAFF"
    )
    button4_7.place(
        x=394.0,
        y=507.0,
        width=90.0,
        height=90.0
    )

    button4_image_8 = PhotoImage(
        file=relative_to_assets("button4_8.png"))
    button4_8 = Button(
        runFrame,
        image=button4_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button4_8 clicked"),
        relief="flat",
        bg="#F0FAFF",
        activebackground="#F0FAFF"
    )
    button4_8.place(
        x=494.0,
        y=507.0,
        width=90.0,
        height=90.0
    )

    button4_image_9 = PhotoImage(
        file=relative_to_assets("button4_9.png"))
    button4_9 = Button(
        runFrame,
        image=button4_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button4_9 clicked"),
        relief="flat",
        bg="#F0FAFF",
        activebackground="#F0FAFF"
    )
    button4_9.place(
        x=389.0,
        y=624.0,
        width=200.0,
        height=66.87898254394531
    )

    button4_image_10 = PhotoImage(
        file=relative_to_assets("button4_10.png"))
    button4_10 = Button(
        runFrame,
        image=button4_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button4_10 clicked"),
        relief="flat",
        bg="#D1F0FF",
        activebackground="#D1F0FF"
    )
    button4_10.place(
        x=690.0,
        y=462.0,
        width=195.0,
        height=65.0
    )

    button4_image_11 = PhotoImage(
        file=relative_to_assets("button4_11.png"))
    button4_11 = Button(
        runFrame,
        image=button4_image_11,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button4_11 clicked"),
        relief="flat",
        bg="#D1F0FF",
        activebackground="#D1F0FF"
    )
    button4_11.place(
        x=690.0,
        y=547.0,
        width=195.0,
        height=65.0
    )

    button4_image_12 = PhotoImage(
        file=relative_to_assets("button4_12.png"))
    button4_12 = Button(
        runFrame,
        image=button4_image_12,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button4_12 clicked"),
        relief="flat",
        bg="#D1F0FF",
        activebackground="#D1F0FF"
    )
    button4_12.place(
        x=674.0,
        y=649.0,
        width=50.0,
        height=50.0
    )

    button4_image_13 = PhotoImage(
        file=relative_to_assets("button4_13.png"))
    button4_13 = Button(
        runFrame,
        image=button4_image_13,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button4_13 clicked"),
        relief="flat",
        bg="#D1F0FF",
        activebackground="#D1F0FF"
    )
    button4_13.place(
        x=733.0,
        y=649.0,
        width=50.0,
        height=50.0
    )

    def change_img(imagepath):
		
        inputimage = Image.open(imagepath)
        tkimg1 = ImageTk.PhotoImage(inputimage.resize((256, 394)))
		
        image4_1 = canvas4.create_image(183.0, 246.0, image=tkimg1 )
        
        sketchimage = Image.fromarray(ps.pictosketch(inputimage))
        tkimg2 = ImageTk.PhotoImage(sketchimage.resize((256, 394)))
        image4_2 = canvas4.create_image(
            488.0,
            246.0,
            image=tkimg2
        )

        grayimage = gc.sketchtograyscale(sketchimage)
        tkimg3 = ImageTk.PhotoImage(grayimage.resize((256, 394)))

        image4_3 = canvas4.create_image(
            793.0,
            246.0,
            image=tkimg3
        )

        colorimage = ci.graytocolor(grayimage)
        tkimg4 = ImageTk.PhotoImage(colorimage.resize((256, 394)))
        image4_4 = canvas4.create_image(
            1098.0,
            246.0,
            image=tkimg4
        )


        window.mainloop()


    button4_image_14 = PhotoImage(
        file=relative_to_assets("button4_14.png"))
    button4_14 = Button(
        runFrame,
        image=button4_image_14,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: change_img(imgpath),
        relief="flat",
        bg="#D1F0FF",
        activebackground="#D1F0FF"
    )
    button4_14.place(
        x=792.0,
        y=649.0,
        width=50.0,
        height=50.0
    )

    button4_image_15 = PhotoImage(
        file=relative_to_assets("button4_15.png"))
    button4_15 = Button(
        runFrame,
        image=button4_image_15,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button4_15 clicked"),
        relief="flat",
        bg="#D1F0FF",
        activebackground="#D1F0FF"
    )
    button4_15.place(
        x=851.0,
        y=649.0,
        width=50.0,
        height=50.0
    )


    def dragimage(ls):
        global imgpath
        global imgindex

        if len(ls) == 1:
            print(ls[0].decode("utf-8"))
            path = ls[0].decode("utf-8")
            imgpath = path
            '''
            dragspace['text'] = path
            
            if os.path.isdir(path):
                button1['state'] = tk.DISABLED
                # button2['state'] = tk.NORMAL
                button3['state'] = tk.NORMAL
                button4['state'] = tk.NORMAL
                imgindex = -1
                imgpath = glob.glob(path + "/*.jpg")
            else:
                button1['state'] = tk.NORMAL
                button3['state'] = tk.DISABLED
                button4['state'] = tk.DISABLED
			'''

    def chooseimage():
        global imgpath
        global imgindex
        imgpath = filedialog.askopenfilename()

		


    button4_image_16 = PhotoImage(
        file=relative_to_assets("button4_16.png"))
    button4_16 = Button(
        runFrame,
        image=button4_image_16,
        borderwidth=0,
        highlightthickness=0,
        command=chooseimage,
        relief="flat",
        bg="#D1F0FF",
        activebackground="#D1F0FF"
    )
    button4_16.place(
        x=933.0,
        y=457.0,
        width=150.0,
        height=150.0
    )
    windnd.hook_dropfiles(button4_16.winfo_id(), dragimage)

    button4_image_17 = PhotoImage(
        file=relative_to_assets("button4_17.png"))
    button4_17 = Button(
        runFrame,
        image=button4_image_17,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button4_17 clicked"),
        relief="flat",
        bg="#D1F0FF",
        activebackground="#D1F0FF"
    )
    button4_17.place(
        x=1014.0,
        y=624.0,
        width=80.0,
        height=80.0
    )

    button4_image_18 = PhotoImage(
        file=relative_to_assets("button4_18.png"))
    button4_18 = Button(
        runFrame,
        image=button4_image_18,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button4_18 clicked"),
        relief="flat",
        bg="#D1F0FF",
        activebackground="#D1F0FF"
    )
    button4_18.place(
        x=934.0,
        y=624.0,
        width=80.0,
        height=80.0
    )

    button4_image_19 = PhotoImage(
        file=relative_to_assets("button4_19.png"))
    button4_19 = Button(
        runFrame,
        image=button4_image_19,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button4_19 clicked"),
        relief="flat",
        bg="#D1F0FF",
        activebackground="#D1F0FF"
    )
    button4_19.place(
        x=1150.0,
        y=590.0,
        width=130.0,
        height=130.0
    )

    button4_image_20 = PhotoImage(
        file=relative_to_assets("button4_20.png"))
    button4_20 = Button(
        runFrame,
        image=button4_image_20,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button4_20 clicked"),
        relief="flat",
        bg="#D1F0FF",
        activebackground="#D1F0FF"
    )
    button4_20.place(
        x=0.0,
        y=0.0,
        width=100.0,
        height=33.333343505859375
    )




    # runFrame.bind("<Return>", change_img)
    # 以上是執行介面的設計 ################################################################################################
    window.resizable(False, False)
    window.mainloop()
