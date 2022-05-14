from tkinter import *
import pandas as pd
from random import randint
import messagebox

df = pd.read_csv("data.csv")
new_df = (df.to_dict(orient="records"))


# ______________________ button commands ______________
def yes_pressed():
    try:
        df.iloc[random_number, 2] = int(df.iloc[random_number, 2]) + 2
        df.to_csv("data.csv", index=False)
        new_word_generating()
    except ValueError:
        messagebox.showinfo(title="Lack of words", message="Please, add more words")
    except TypeError:
        messagebox.showinfo(title="Lack of words", message="Please, add more words")
    except NameError:
        messagebox.showinfo(title="Lack of words", message="Please, add more words")


def maybe_pressed():
    try:
        df.iloc[random_number, 2] = int(df.iloc[random_number, 2]) + 1
        df.to_csv("data.csv", index=False)
        new_word_generating()
    except ValueError:
        messagebox.showinfo(title="Lack of words", message="Please, add more words")
    except TypeError:
        messagebox.showinfo(title="Lack of words", message="Please, add more words")
    except NameError:
        messagebox.showinfo(title="Lack of words", message="Please, add more words")


# _______________________Word Generating_______________
def new_word_generating():
    try:
        print("new word is generated")
        global random_number
        random_number = random_num()
        print("random is", random_number)
        new_word = new_df[random_number]

        canvas.itemconfig(language_name_txt, text="German")
        canvas.itemconfig(new_word_txt, text=new_word["German"])

        window.after(3000, flipping_the_card, new_word["English"])

    except ValueError:
        messagebox.showinfo(title="Lack of words", message="Please, add more words")
    except TypeError:
        messagebox.showinfo(title="Lack of words", message="Please, add more words")
    except NameError:
        messagebox.showinfo(title="Lack of words", message="Please, add more words")


def flipping_the_card(translation):
    canvas.itemconfig(language_name_txt, text="English")
    canvas.itemconfig(new_word_txt, text=translation)


# _____________Valid random number generation________________
def random_num():
    try:
        ran_num = randint(0, 99)
        if int(df.iloc[ran_num, 2]) > 1:
            return random_num()
        else:
            return ran_num
    except RecursionError:
        messagebox.showinfo(title="Lack of words", message="Please, add more words")


# _______________________UI _________________
bg_color = "#B1DDC6"
# Create object
window = Tk()

window.title("Flash cards")
window.geometry("900x800")
window.config(bg=bg_color)

# uploading the images
card_back_img = PhotoImage(file="card_back.png")
card_front_img = PhotoImage(file="card_front.png")
yes_button_img = PhotoImage(file="yes.png")
no_button_img = PhotoImage(file="no.png")
maybe_button_img = PhotoImage(file="maybe.png")

# creating canvas and uploading images
canvas = Canvas(width=880, height=650, highlightthickness=0, bg=bg_color)

canvas.create_image(450, 300, image=card_back_img)
canvas.create_image(450, 300, image=card_front_img)
canvas.pack()

yes_button = Button(image=yes_button_img, bg=bg_color, highlightthickness=0, command=yes_pressed)
yes_button.place(x=600, y=620)

no_button = Button(image=no_button_img, bg=bg_color, highlightthickness=0, command=new_word_generating)
no_button.place(x=150, y=620)

maybe_button = Button(image=maybe_button_img, bg=bg_color, highlightthickness=0, command=maybe_pressed)
maybe_button.place(x=350, y=620)

# asking the user
language_name_txt = canvas.create_text(450, 150, text="Are you", font=("Ariel", 40, "italic"))
new_word_txt = canvas.create_text(450, 300, text="ready?", font=("Ariel", 60, "italic"))


window.mainloop()
