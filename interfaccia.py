import openai
from tkinter import *
from ctypes import windll, byref, create_unicode_buffer, create_string_buffer

system_message = """Sei un assistente per uno studente italiano che frequenta le scuole medie superiori. 
Lo studente ha problemi nel leggere e scrivere per periodi prolungati perché è affetto da Disturbo Specifico 
dell’Apprendimento. 
Lo studente vorebbe che tenessi conto del suo Disturbo Specifico dell’Apprendimento. Lo studente vorrebbe che lo 
correggessi quando 
sbaglia a fare lo spelling di parole. Lo studente vorebbe che lo aiutassi a creare un testo senza errori ortografici.
Se identifichi degli errori, correggili e aggiungi la versione corretta nella risposta."""
openai.api_key = "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"

FR_PRIVATE  = 0x10
FR_NOT_ENUM = 0x20

def loadfont(fontpath, private=True, enumerable=False):
    if isinstance(fontpath, bytes):
        pathbuf = create_string_buffer(fontpath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExA
    elif isinstance(fontpath, str):
        pathbuf = create_unicode_buffer(fontpath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExW
    else:
        raise TypeError('fontpath must be of type str or unicode')

    flags = (FR_PRIVATE if private else 0) | (FR_NOT_ENUM if not enumerable else 0)
    numFontsAdded = AddFontResourceEx(byref(pathbuf), flags, 0)
    return bool(numFontsAdded)

loadfont("OpenDyslexic-Regular.otf")

root = Tk()
root.title("Chatbot")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "OpenDyslexic-Regular"
FONT_BOLD = "Helvetica 13 bold"

def ask_gpt(messages):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.2,
        max_tokens=200
    )
    return completion.choices[0].message["content"]

messages = [{"role": "system", "content": system_message}]

def send():
    global messages
    send = "Utente -> " + e.get()
    txt.insert(END, "\n" + send)

    user = e.get().lower()
    messages.append({"role": "user", "content": user})

    response = ask_gpt(messages)
    messages.append({"role": "assistant", "content": response})
    txt.insert(END, "\nAssistente -> " + response)

    print(messages)

    e.delete(0, END)


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
    row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
              command=send).grid(row=2, column=1)

root.mainloop()
