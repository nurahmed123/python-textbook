import os
import pyttsx3
import googletrans
import textblob
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox as msg
from tkinter import font , colorchooser
from tkinter.filedialog import askopenfilename ,asksaveasfilename

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice",voices[0].id)
# lenth_voice = len(voices)
# print(lenth_voice)
engine.setProperty('rate', 172)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def new(event = ""):
    global file
    root.title("Untitled - Notepad")
    file = None
    txt_area.delete(1.0 , "end")

#Todo : main_bar tools
def bold(event=""):
    txt_get = font.Font(font = txt_area["font"])
    if txt_get.actual()["weight"] == "normal":
        txt_area.configure(font =(clt_font_from_combo_box,clt_font_size_from_combo_box,"bold"))
    elif txt_get.actual()["weight"] == "bold":
        txt_area.configure(font =(clt_font_from_combo_box,clt_font_size_from_combo_box,"normal"))

def italic(event = ""):
    txt_get = font.Font(font=txt_area["font"])
    if txt_get.actual()["slant"] == "roman":
        txt_area.configure(font =(clt_font_from_combo_box,clt_font_size_from_combo_box,"italic"))
    elif txt_get.actual()["slant"] == "italic":
        txt_area.configure(font=(clt_font_from_combo_box, clt_font_size_from_combo_box, "roman"))
#
def under_line(event =""):
    # print(font.Font(font=txt_area["font"]).actual())
    txt_get = font.Font(font=txt_area["font"])
    if txt_get.actual()["underline"] == 0:
        txt_area.configure(font =(clt_font_from_combo_box,clt_font_size_from_combo_box,"underline"))
    elif txt_get.actual()["underline"] == 1:
        txt_area.configure(font=(clt_font_from_combo_box, clt_font_size_from_combo_box, "normal"))
def chose_color(event = ""):
    chose_colors = colorchooser.askcolor()
    txt_area.configure(fg = chose_colors[1])

#Todo :finish
def open_file(event = ""):
    global file
    file = askopenfilename(initialdir = os.getcwd(),title = "Select File",filetypes = [("Text  file","*.txt") , ("All Doucument","*.*")])
    try:
        with open(file,"r") as for_read:
            txt_area.delete(1.0,END)
            txt_area.insert(1.0,for_read.read())
    except FileNotFoundError:
        return
    except:
        return
    root.title(os.path.basename(file))
    # file = askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
    # if file == "":
    #     file = None
    # else:
    #     root.title(os.path.basename(file) + " - Notepad")
    #     txt_area.delete(1.0, END)
    #     f = open(file, "r")
    #     txt_area.insert(1.0, f.read())
    #     f.close()

def save_file(event = ""):
    global file
    # if file:
    #     content = str(txt_area.get(1.0,END))
    #     with open (file , "w",encoding = "utf-8") as for_read:
    #         for_read.write(content)
    # else:
    #     file = asksaveasfilename(mode = "w" , defaultextension = "txt",filetypes =[("All Files", "*.*"),("Text Documents", "*.txt")])
    #     content2 = txt_area.get(1.0,END)
    #     file.write(content2)
    #     file.close()
    try:
        if file == None:
            file = asksaveasfilename(initialfile = "Untitled file" , defaultextension = ".txt" ,
                                     filetypes = [("All Files" , "*.*") , ("Text_Document" , "*.txt")])
            if file == "":
                file=None
            else:
                # with open(file, "w", encoding="utf-8") as for_read:
                #     for_read.write(txt_area.get(1.0,END))
                # root.title(os.path.basename(file) + " - Notepad")
                with open(file, "w") as for_read:
                    for_read.write(txt_area.get(1.0,END))
                root.title(os.path.basename(file) + " - Notepad")
        else:
            # with open(file, "w", encoding="utf-8") as for_read:
            #     for_read.write(txt_area.get(1.0,END))
            # root.title(os.path.basename(file) + " - Notepad")
            with open(file, "w") as for_read:
                for_read.write(txt_area.get(1.0,END))
            root.title(os.path.basename(file) + " - Notepad")
    except:
        return

def exit(event = ""):
    global file
    try:
        if file == None:
            if file == "":
                file=None
            else:
                if txt_area.get(1.0,END) != "\n":
                    result = msg.askyesnocancel("Notice", "Do you want to save this file")
                    if result:
                        file = asksaveasfilename(initialfile="Untitled file", defaultextension=".txt",
                                                 filetypes=[("All Files", "*.*"), ("Text_Document", "*.txt")])
                        # with open(file, "w", encoding="utf-8") as for_read:
                        #     for_read.write(txt_area.get(1.0,END))
                        # root.destroy()
                        with open(file, "w") as for_read:
                            for_read.write(txt_area.get(1.0,END))
                        root.destroy()
                    else:
                        root.destroy()
                else:
                    root.destroy()
        else:
            # with open(file, "w", encoding="utf-8") as for_read:
            #     for_read.write(txt_area.get(1.0,END))
            # root.destroy()
            with open(file, "w") as for_read:
                for_read.write(txt_area.get(1.0,END))
            root.destroy()
    except:
        return

def translate_now(event=""):
    global language_box
    global language_box1
    global languageVar
    global languageVar1
    try:
        # src_txt = language_box.get()
        tgr_txt = language_box1.get()
        message = txt_area.get(1.0,END)

        language_key = googletrans.LANGUAGES
        language_key_ = language_key.keys()

        if txt_area:
            words=textblob.TextBlob(message)
            lan=words.detect_language()
            for i,j in language.items():
                if j == tgr_txt:
                    lang = i
            words=words.translate(from_lang=lan , to=str(lang))
            txt_area.delete(1.0,END)
            txt_area.insert(END,words)
        # translator = google_translator()
        # for i in range(2):
        #     print(src_txt[i],end = "")
        # print()
        # for j in range(2):
        #     print(tgr_txt[j],end = "")
        # print()

        # src = "en"
        # tgr = "bn"
        # if src == tgr:
        #     txt_area.delete(1.0,"end")
        #     txt_area.insert(1.0," ")
        # else:
        #     translate_text = translator.translate(message, lang_src=src, lang_tgt=tgr)
        #     txt_area.delete(1.0,"end")
        #     txt_area.insert(1.0,translate_text)
    except EXCEPTION as e:
        msg.showerror("Error!" , "You didn't select language")

def copy(event = ""):
    txt_area.event_generate("<<Copy>>")

def cut(event = ""):
    txt_area.event_generate("<<Cut>>")

def paste(event = ""):
    txt_area.event_generate("<<Paste>>")

def help(event = ""):
    msg.showinfo("About Note pad" , "Note Pad By Nur Ahmed")

def status_bar_hide(event = ""):
    global show_status_bar
    if show_status_bar:
        sbar.pack_forget()
        show_status_bar = False
    else:
        sbar.pack(side=BOTTOM, fill=BOTH)
        show_status_bar = True
def tool_bar_hide(event = ""):
    global show_tool_bar
    if show_tool_bar:
        tool_bar.pack_forget()
        show_tool_bar = False
    else:
        txt_area.pack_forget()
        sbar.pack_forget()
        tool_bar.pack(side= TOP, fill= X)
        txt_area.pack(fill = BOTH , expand = True)
        sbar.pack(side=BOTTOM, fill=BOTH)
        show_tool_bar=True

def find_fun(event=""):
    def find(event=None):
        word = find_input.get()
        txt_area.tag_remove("match", "1.0", END)
        matches = 0
        if word:
            start_pos = "1.0"
            while True:
                start_pos = txt_area.search(word, start_pos, stopindex=END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                txt_area.tag_add("match", start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                txt_area.tag_config("match", foreground="red", background="yellow")
        elif word is False:
            msg.showinfo("Find Text","No word matched")

    def replace():
        word = find_input.get()
        replace_txt = replace_input.get()
        content = txt_area.get(1.0,"end")
        new_content = content.replace(word,replace_txt)
        txt_area.delete(1.0,"end")
        txt_area.insert(1.0,new_content)
    find_window = Toplevel(root)
    find_window.wm_iconbitmap("icon\\note pad.ico")
    find_window.title("Find Text")
    find_window.geometry("450x200+350+100")
    find_window.resizable(0,0)

    #Todo :find frm
    find_frm = ttk.LabelFrame(find_window,text = "Find and Replace word" )
    find_frm.pack(pady = 20)

    txt_find = ttk.Label(find_frm , text = "Find")
    txt_replace = ttk.Label(find_frm , text = "Replace")

    find_input = ttk.Entry(find_frm , width=30)
    replace_input = ttk.Entry(find_frm , width=30)
    find_input.focus()

    find_btn = ttk.Button(find_frm,text = "Find" , command = find)
    replace_btn = ttk.Button(find_frm,text = "Replace" , command = replace)

    txt_find.grid(row = 0 ,column = 0 ,padx = 4 ,pady = 4)
    txt_replace.grid(row = 1 ,column = 0 ,padx = 4 ,pady = 4)

    find_input.grid(row = 0 ,column = 1 ,padx = 4 ,pady = 4)
    replace_input.grid(row = 1 ,column = 1 ,padx = 4 ,pady = 4)

    find_btn.grid(row = 2 ,column = 0 ,padx = 4 ,pady = 4)
    replace_btn.grid(row = 2 ,column = 1 ,padx = 4 ,pady = 4)

def clear(event=""):
    txt_area.delete(1.0,"end")

def txt_left_align(event=""):
    str_all_txt = txt_area.get(1.0,"end")
    txt_area.tag_config("left",justify = LEFT)#Todo : .tsg_config is use to change text align
    txt_area.delete(1.0,END)
    txt_area.insert(INSERT,str_all_txt,"left")

def change_them(*args):
    # ld = Light_Default.get()
    # lp =Light_Plus.get()
    # d= Dark.get()
    # r = Red.get()
    # m = Monokai.get()
    # nb = Night_Blue.get()
    # if ld == "Light_Default":
    #     print("ld")
    color_dict = {
        "Light Default": ("#000000", "#ffffff"),
        "Light Plus": ("#474747", "#e0e0e0"),
        "Dark": ("#c4c4c4", "#2d2d2d"),
        "Red": ("#2d2d2d", "#ffe8e8"),
        "Monokai": ("#d3b774", "#474747"),
        "Night Blue": ("#ededed", "#6b9dc2")
    }
    global i
    if i.get() == 1:
        txt_area.config(fg = "#000000" , bg = "#ffffff")
    elif i.get() == 2:
        txt_area.config(fg="#474747" , bg="#e0e0e0")
    elif i.get() == 3:
        txt_area.config(fg="#c4c4c4" , bg="#2d2d2d")
    elif i.get() == 4:
        txt_area.config(fg="#2d2d2d" , bg="#ffe8e8")
    elif i.get() == 5:
        txt_area.config(fg="#d3b774" , bg="#474747")
    elif i.get() == 6:
        txt_area.config(fg="#ededed" , bg="#6b9dc2")

def txt_right_align():
    str_all_txt = txt_area.get(1.0, "end")
    txt_area.tag_config("right", justify=RIGHT)
    txt_area.delete(1.0, END)
    txt_area.insert(INSERT, str_all_txt, "right")

def txt_center_align():
    str_all_txt = txt_area.get(1.0, "end")
    txt_area.tag_config("center", justify=CENTER)
    txt_area.delete(1.0, END)
    txt_area.insert(INSERT, str_all_txt, "center")

def speaker(event=""):
    try:
        str_wrd_spk = txt_area.get(1.0 , "end-1c")
        speak(str_wrd_spk)
    except EXCEPTION as e:
        msg.showinfo("Language Error" , "It supported english language\nPlease Type English and try again")

def sht_cut_keys_window(event=""):
    def ok():
        key_window.destroy()
    key_window = Toplevel(root)
    key_window.title("Shortcut Keys")
    key_window.wm_iconbitmap("icon\\note pad.ico")
    f1 = Frame(key_window , pady  = 5 , bg = "white")
    f1.pack(side = BOTTOM , pady = 5)
    Button(f1 , text = "Ok", command = ok , padx = 10).pack(side = BOTTOM , padx = 10)
    key_window.geometry("420x260")
    key_window.configure(background = "white")
    key_window.focus()
    key_window.resizable(0,0)
    image = Image.open("icon\\short cut.png")
    photo = ImageTk.PhotoImage(image)

    varun_label = Label(key_window , image=photo)
    varun_label.pack()
    key_window.mainloop()



if __name__ == '__main__':
    root = Tk()
    height = 665
    width = 1200
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    # print(f"{w}x{h}")

    root.geometry(f"{w-200}x{h-120}")
    root.minsize(705,55)
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("icon\\note pad.ico")
    root.configure(background = "white")
    #Todo use srt cut
    root.bind("<Control-n>", new)
    root.bind("<Control-o>", open_file)
    root.bind("<Control-s>", save_file)
    root.bind("<Control-e>", exit)
    root.bind("<Control-x>", cut)
    root.bind("<Control-h>", help)
    root.bind("<Control-f>", find_fun)
    root.bind("<Control-j>", clear)
    root.bind("<Control-d>", status_bar_hide)
    root.bind("<Control-t>", tool_bar_hide)
    root.bind("<Control-q>", speaker)
    root.bind("<Control-r>", sht_cut_keys_window)
    root.bind("<Control-b>", bold)
    root.bind("<Control-i>", italic)
    root.bind("<Control-u>", under_line)
    root.bind("<Control-p>", chose_color)

    #Todo : end srt cut

    #TODO : importing imagaes that will use in this app
    new_icon  =  Image.open("icon\\new.png")
    open_icon = Image.open("icon\\open.png")
    save_icon = Image.open("icon\\save.png")
    exit_icon = Image.open("icon\\exit.png")

    copy_icon = Image.open("icon\\copy.png")
    cut_icon  =  Image.open("icon\\cut.png")
    paste_icon = Image.open("icon\\paste.png")
    undo_icon = Image.open("icon\\undo.png")
    redo_icon = Image.open("icon\\redo.png")
    find_icon = Image.open("icon\\find.png")
    shtcut_keys_icon = Image.open("icon\\shtcut keys.png")
    clear_icon = Image.open("icon\\clear.png")
    help_icon = Image.open("icon\\help.png")
    speaker_icon = Image.open("icon\\speker.png")
    tool_bar_icon = Image.open("icon\\tool bar.png")
    sts_bar_icon = Image.open("icon\\status bar.png")
    #Todo : finish

    #Todo making a base format of all imagaes
    re_sz_new_icon  = new_icon.resize((20,20) , Image.ANTIALIAS)
    re_sz_open_icon = open_icon.resize((20,20) , Image.ANTIALIAS)
    re_sz_save_icon = save_icon.resize((20,20) , Image.ANTIALIAS)
    re_sz_exit_icon = exit_icon.resize((20,20) , Image.ANTIALIAS)
    re_sz_copy_icon = copy_icon.resize((20,20) , Image.ANTIALIAS)
    re_sz_cut_icon = cut_icon.resize((20,20) , Image.ANTIALIAS)
    re_sz_paste_icon = paste_icon.resize((20,20) , Image.ANTIALIAS)
    re_sz_undo_icon = undo_icon.resize((20,20) , Image.ANTIALIAS)
    re_sz_redo_icon = redo_icon.resize((20,20) , Image.ANTIALIAS)
    re_sz_help_icon = help_icon.resize((20,20) , Image.ANTIALIAS)

    re_sz_speaker_icon = speaker_icon.resize((20,20), Image.ANTIALIAS)
    re_sz_find_icon = find_icon.resize((20,20) , Image.ANTIALIAS)
    re_sz_shtcut_keys_icon = shtcut_keys_icon.resize((20,20) , Image.ANTIALIAS)
    re_sz_clear_icon = clear_icon.resize((20,20) , Image.ANTIALIAS)
    re_sz_tool_bar_icon = tool_bar_icon.resize((20,20) , Image.ANTIALIAS)
    re_sz_sts_bar_icon = sts_bar_icon.resize((20,20) , Image.ANTIALIAS)

    # Todo : finish

    #Todo : store resized images into variable
    r_sz_new_icon = ImageTk.PhotoImage(re_sz_new_icon)
    r_sz_open_icon = ImageTk.PhotoImage(re_sz_open_icon)
    r_sz_save_icon = ImageTk.PhotoImage(re_sz_save_icon)
    r_sz_exit_icon = ImageTk.PhotoImage(re_sz_exit_icon)
    r_sz_copy_icon = ImageTk.PhotoImage(re_sz_copy_icon)
    r_sz_cut_icon = ImageTk.PhotoImage(re_sz_cut_icon)
    r_sz_redo_icon = ImageTk.PhotoImage(re_sz_redo_icon)
    r_sz_undo_icon = ImageTk.PhotoImage(re_sz_undo_icon)
    r_sz_paste_icon = ImageTk.PhotoImage(re_sz_paste_icon)
    r_sz_help_icon = ImageTk.PhotoImage(re_sz_help_icon)
    r_sz_shtcut_keys_icon = ImageTk.PhotoImage(re_sz_shtcut_keys_icon)

    r_sz_speaker = ImageTk.PhotoImage(re_sz_speaker_icon)
    r_sz_find_icon = ImageTk.PhotoImage(re_sz_find_icon)
    r_sz_clear_icon = ImageTk.PhotoImage(re_sz_clear_icon)
    r_sz_tool_bar_icon = ImageTk.PhotoImage(re_sz_tool_bar_icon)
    r_sz_sts_bar_icon = ImageTk.PhotoImage(re_sz_sts_bar_icon)
    #Todo : finish

    #Todo : tool bar icons
    bold_icon = Image.open("icon\\bold.png")
    italic_icon = Image.open("icon\\iatalic.png")
    left_align = Image.open("icon\\left side.png")
    right_align = Image.open("icon\\right side.png")
    center_align = Image.open("icon\\center text align.png")
    under_line_align = Image.open("icon\\under line.png")
    color_icon = Image.open("icon\\color change.png")

    re_sz_bold_icon = bold_icon.resize((20, 20), Image.ANTIALIAS)
    re_sz_italic_icon = italic_icon.resize((20, 20), Image.ANTIALIAS)
    re_sz_left_align = left_align.resize((20, 20), Image.ANTIALIAS)
    re_sz_right_align = right_align.resize((20, 20), Image.ANTIALIAS)
    re_sz_center_align = center_align.resize((20, 20), Image.ANTIALIAS)
    re_sz_under_line_align = under_line_align.resize((20, 20), Image.ANTIALIAS)
    re_sz_color_icon = color_icon.resize((20, 20), Image.ANTIALIAS)

    r_sz_bold_icon = ImageTk.PhotoImage(re_sz_bold_icon)
    r_sz_italic_icon = ImageTk.PhotoImage(re_sz_italic_icon)
    r_sz_right_align = ImageTk.PhotoImage(re_sz_right_align)
    r_sz_left_align = ImageTk.PhotoImage(re_sz_left_align)
    r_sz_center_align = ImageTk.PhotoImage(re_sz_center_align)
    r_sz_under_line_align = ImageTk.PhotoImage(re_sz_under_line_align)
    r_sz_color_icon = ImageTk.PhotoImage(re_sz_color_icon)

    #Todo : them color
    #Todo : black
    black_them_icon = Image.open("icon\\black circle.png")
    re_sz_black_them_icon = black_them_icon.resize((20, 20), Image.ANTIALIAS)
    r_sz_black_them_icon = ImageTk.PhotoImage(re_sz_black_them_icon)

    light_default_icon = Image.open("icon\\light defaul.png")
    re_sz_light_default_icon = black_them_icon.resize((20, 20), Image.ANTIALIAS)
    r_sz_light_default_icon = ImageTk.PhotoImage(re_sz_light_default_icon)
    #Todo : finish

    #TODO : creating menubar
    main_menu = Menu(root)
    #Todo : menu items
    sub_menu = Menu(main_menu , tearoff = 0)
    sub_menu.add_command(label = "New" , image = r_sz_new_icon, compound = LEFT,accelerator ="Ctrl+N",command = new)
    sub_menu.add_command(label = "Open", image = r_sz_open_icon, compound = LEFT,accelerator ="Ctrl+O", command = open_file)
    sub_menu.add_command(label = "Save" , image = r_sz_save_icon , compound = LEFT , accelerator = "Ctrl+S" ,command = save_file)
    sub_menu.add_separator()
    sub_menu.add_command(label = "Exit" , image = r_sz_exit_icon , compound = LEFT , accelerator = "Ctrl+E" , command = exit)
    main_menu.add_cascade(label = "File" , menu = sub_menu)
    # Todo : finish

    #Todo : edit items
    sub_menu = Menu(main_menu, tearoff=0)
    sub_menu.add_command(label="Copy" , image = r_sz_copy_icon , compound = LEFT , accelerator = "Ctrl+C" , command = copy)
    sub_menu.add_command(label="Cut" , image = r_sz_cut_icon , compound = LEFT , accelerator = "Ctrl+X" , command = cut)
    sub_menu.add_command(label="Paste" , image = r_sz_paste_icon , compound  = LEFT , accelerator = "Ctrl+V" , command = paste)
    sub_menu.add_separator()
    sub_menu.add_command(label="Find" , image = r_sz_find_icon , compound  = LEFT , accelerator = "Ctrl+F" , command = find_fun)
    sub_menu.add_command(label="Clear" , image = r_sz_clear_icon , compound  = LEFT , accelerator = "Ctrl+J" , command = clear)
    main_menu.add_cascade(label="Edit", menu=sub_menu)
    # Todo : finish

    # Todo : view
    sub_menu = Menu(main_menu, tearoff=0)
    sub_menu.add_checkbutton(label="Tool bar", onvalue = True , offvalue = False , variable = tool_bar_hide ,
                             image=r_sz_tool_bar_icon, compound=LEFT, accelerator="Ctrl+T", command=tool_bar_hide)
    sub_menu.add_checkbutton(label="Status bar", onvalue = True , offvalue = False , variable = tool_bar_hide ,
                             image=r_sz_sts_bar_icon, compound=LEFT, accelerator="Ctrl+D" , command =status_bar_hide)
    sub_menu.add_separator()
    sub_menu.add_command(label="Shortcut keys", image=r_sz_shtcut_keys_icon, compound=LEFT, accelerator="Ctrl+R" ,
                         command = sht_cut_keys_window)
    main_menu.add_cascade(label="Vew", menu=sub_menu)
    # Todo : finish

    # Todo : help items
    sub_menu = Menu(main_menu, tearoff=0)
    sub_menu.add_command(label="About Note pad" , image = r_sz_help_icon ,
                         compound = LEFT , accelerator = "Ctrl+H" , command = help)
    main_menu.add_cascade(label="Help", menu=sub_menu)
    # Todo : finish
    theme_color_choose = StringVar()
    # Todo : Theme
    sub_menu = Menu(main_menu, tearoff=0)

    # re_sz them color
    black_color = Image.open("icon\\black color.png")
    re_sz_black_color = black_color.resize((20,20),Image.ANTIALIAS)
    r_sz_black_color = ImageTk.PhotoImage(re_sz_black_color)

    light_color = Image.open("icon\\light color.png")
    re_sz_light_color = light_color.resize((20, 20), Image.ANTIALIAS)
    r_sz_light_color = ImageTk.PhotoImage(re_sz_light_color)
    # for i in color_dict:
    i = IntVar()
    Light_Default = sub_menu.add_radiobutton(label="Light Default", command=change_them, value=1, variable=i)
    Light_Plus = sub_menu.add_radiobutton(label="Light Plus", command=change_them, value=2, variable=i)
    Dark = sub_menu.add_radiobutton(label="Dark",command=change_them, value=3, variable=i)
    Red = sub_menu.add_radiobutton(label="Red",command=change_them, value=4, variable=i)
    Monokai = sub_menu.add_radiobutton(label="Monokai",command=change_them, value=5, variable=i)
    Night_Blue = sub_menu.add_radiobutton(label="Night Blue",command=change_them, value=6, variable=i)
    # color+=1
    main_menu.add_cascade(label="Theme", menu=sub_menu)
    # Todo : finish

    root.config(menu=main_menu)
    #TODO : file menu finish

    #Todo : hdr_tools
    tool_bar = Label(root , bg = "light grey")
    tool_bar.pack(fill = X , side = TOP)

    #Todo : fonts section
    fonts = font.families()
    font_str = StringVar()
    font_box = ttk.Combobox(tool_bar , width = 30 , textvar = font_str,state = "readonly")
    font_box["values"] = fonts
    font_box.current(fonts.index("Arial"))
    font_box.grid(row = 0 , column = 0 , padx = 7)
    #Todo : finish

    # Todo : font size section
    font_size_str = IntVar()
    font_size_box = ttk.Combobox(tool_bar, width=20, textvar=font_size_str, state="readonly")
    font_size_box["values"] = tuple(range(4,100,2))
    font_size_box.current(6)
    font_size_box.grid(row=0, column=1, padx=7)
    # Todo : finish

    clt_font_from_combo_box = "Arial"
    clt_font_size_from_combo_box = 16

    # Todo : set font and font size
    def set_fonts(root):
        global clt_font_from_combo_box
        clt_font_from_combo_box = font_str.get()
        txt_area.config(font=(clt_font_from_combo_box,clt_font_size_from_combo_box))
    font_box.bind("<<ComboboxSelected>>",set_fonts)

    def font_size(root):
        global clt_font_size_from_combo_box
        clt_font_size_from_combo_box = font_size_str.get()
        txt_area.config(font = (clt_font_from_combo_box,clt_font_size_from_combo_box))
    font_size_box.bind("<<ComboboxSelected>>" , font_size)
    # Todo : finish



    #Todo : tool bar buttons
    btn = ttk.Button(tool_bar , image = r_sz_bold_icon , command = bold)
    btn.grid(row = 0 , column = 2, padx = 5)

    btn1 = ttk.Button(tool_bar, image=r_sz_italic_icon , command = italic)
    btn1.grid(row=0, column=3 , padx = 5)

    btn2 = ttk.Button(tool_bar , image = r_sz_under_line_align , command = under_line)
    btn2.grid(row = 0 , column = 4 , padx = 5)

    btn3 = ttk.Button(tool_bar , image = r_sz_color_icon , command = chose_color)
    btn3.grid(row = 0 , column = 5 , padx = 5)

    btn4 = ttk.Button(tool_bar , image = r_sz_right_align , command = txt_left_align)
    btn4.grid(row = 0 , column = 6 , padx = 5)

    btn5 = ttk.Button(tool_bar , image = r_sz_center_align , command = txt_center_align)
    btn5.grid(row = 0 , column = 7 , padx = 5)

    btn6 = ttk.Button(tool_bar, image=r_sz_left_align, command = txt_right_align)
    btn6.grid(row=0, column=8, padx=5)

    btn7 = ttk.Button(tool_bar, image=r_sz_speaker , command = speaker)
    btn7.grid(row=0, column=9, padx=5)
    #Todo : finish

    #Todo : google translator section
    language = googletrans.LANGUAGES
    languageVar = list(language.values())
    language_box = ttk.Combobox(tool_bar , values = languageVar , state = "r" , font = "lucida 10")
    language_box.grid(row=0, column=10, padx=5)
    language_box.set("english")

    lan_btn_pic = Image.open("icon\\translate.png")
    re_sz_lan_btn_pic = lan_btn_pic.resize((20,20) , Image.ANTIALIAS)
    r_sz_lan_btn_pic = ImageTk.PhotoImage(re_sz_lan_btn_pic)
    lan_btn = Button(tool_bar,image = r_sz_lan_btn_pic , command = translate_now).grid(row = 0 , column =11 , padx = 5)

    language1 = googletrans.LANGUAGES
    languageVar1 = list(language.values())
    language_box1 = ttk.Combobox(tool_bar, values=languageVar1, state="r", font="lucida 10")
    language_box1.grid(row=0, column=12, padx=5)
    language_box1.set("bengali")

    #Todo :sound and rate for voice control
    # volume = ttk.Scale(tool_bar, from_=0, to=200, orient=HORIZONTAL)
    # volume.set(100)
    # volume.grid(row=0, column=9, padx=5)

    #TODO : create scroll bar
    scrl_bar = Scrollbar(root)
    scrl_bar.pack(side = RIGHT , fill = Y)
    #TODO : finish

    #TODO : create text area
    txt_area = Text(root , yscrollcommand = scrl_bar.set, font = "arial 16", undo = True)# bg= f"{bg}" , fg = f"{fg}"
    txt_area.pack(fill = BOTH, expand = True)
    scrl_bar.config(command = txt_area.yview)
    txt_area.focus_set()
    file = None
    # TODO: finish txt area

    #TODO: create sts bar
    show_status_bar = BooleanVar()
    show_status_bar.set(True)
    show_tool_bar = BooleanVar()
    show_tool_bar.set(True)

    sbar = Label(root, text = "Status Bar" , relief=SUNKEN, anchor=CENTER, padx=8, font=('lucida 9'))
    sbar.pack(side=BOTTOM, fill=BOTH)
    text_cng = False

    def show_chr_and_word(event=None):
        if txt_area.edit_modified():
            global text_cng
            text_cng = True
            words = len(txt_area.get(1.0, 'end-1c').split())
            characters = len(txt_area.get(1.0, 'end-1c').replace(" ",""))
            count = 0
            for space in str(characters):
                if space.isspace() == True:
                    count += 1
            sbar.config(text=f"Characters: {characters} words: {words} spaces: {count}")
        txt_area.edit_modified(False)
    txt_area.bind("<<Modified>>" , show_chr_and_word)
    # TODO : finish sts bar

    root.mainloop()