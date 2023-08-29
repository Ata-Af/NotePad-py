import tkinter as tk
import pickle

def mainWindow():
    mainpage = tk.Tk()
    mainpage.geometry('350x440')
    mainpage.title('Note Pad')
    mainpage.config(bg='#ABD5C9')
    mainpage.resizable(0, 0)

    noteDic = {

    }

    def newNotepage():
        newNotePage = tk.Toplevel()
        newNotePage.geometry('350x430')
        newNotePage.title(' New note ')
        newNotePage.config(bg='#ABD5C9')
        newNotePage.resizable(0, 0)

        def savenote():
            global counter
            try:
                a = newNote_textbox.get("1.0", 'end-1c')
                counter = int(len(list(noteDic.keys())))
                listBox.insert(counter+1,newNoteName_Entry.get())
                noteDic.update({newNoteName_Entry.get():a})

                file = open('NoteBackup.txt', 'wb')
                file.close()
                file = open('NoteBackup.txt', 'ab')
                pickle.dump(noteDic, file)
                file.close()

            except ValueError:
                print('Error')

        newNoteName = tk.Label(newNotePage, text='New note name : ', bg='#ABD5C9', font='Calibri 11')
        newNoteName.place(x=13, y=10)

        newNoteName_Entry = tk.Entry(newNotePage, bd=2, width=20)
        newNoteName_Entry.place(x=210, y=13)

        newNote_textbox = tk.Text(newNotePage, bd=3, width=45, height=20, font='Calibri, 10')
        newNote_textbox.place(x=13, y=50)

        newNoteSave_Button = tk.Button(newNotePage, image=newNoteSaveButton_Image, bg='#ABD5C9', bd=0, activebackground='#ABD5C9', command=savenote)
        newNoteSave_Button.place(x=11, y=388)

    def noteShowpage():
        noteShowpage = tk.Toplevel()
        noteShowpage.geometry('350x338')
        noteShowpage.title(' Notes ')
        noteShowpage.config(bg='#ABD5C9')
        noteShowpage.resizable(0, 0)

        showNote_text = tk.Text(noteShowpage, width=40, height=16, bd=3, font='Calibri 12')
        showNote_text.place(x=11, y=10)

        file = open('NoteBackup.txt', 'rb')
        new = pickle.load(file)

        selected = listBox.get(tk.ANCHOR)

        showNote_text.delete('1.0', tk.END)
        showNote_text.insert(tk.END, new[selected])

    def deleteNote ():
        try:

            file = open('NoteBackup.txt', 'rb')
            new = pickle.load(file)
            file.close()
            selected = listBox.get(tk.ANCHOR)

            new.pop(selected)

            file = open('NoteBackup.txt', 'wb')
            pickle.dump(new, file)
            file.close()

            listBox.delete(tk.ANCHOR)

        except ValueError:
            print('Error')


    listBox = tk.Listbox(mainpage, bg='#ABD5C9', width=40, height=18, bd=4, activestyle='dotbox')
    listBox.config(font=('Calibri', 12))
    listBox.place(x=10, y=10)

    newNoteB_image = tk.PhotoImage(file='NewNoteButton.png')
    addButton = tk.Button(mainpage, bg='#ABD5C9', bd=0, activebackground='#ABD5C9', image=newNoteB_image, command=newNotepage)
    addButton.place(x=10, y=390)

    deleteNoteB_image = tk.PhotoImage(file='DeleteNoteButton.png')
    deleteButton = tk.Button(mainpage, bg='#ABD5C9', bd=0, activebackground='#ABD5C9', image=deleteNoteB_image, command= deleteNote)
    deleteButton.place(x=60, y=390)

    readNoteButton_image = tk.PhotoImage(file='ReadNoteButton.png')
    readNoteButton = tk.Button(mainpage, bg='#ABD5C9', bd=0, activebackground='#ABD5C9', image=readNoteButton_image, command=noteShowpage)
    readNoteButton.place(x=120, y=390)

    newNoteSaveButton_Image = tk.PhotoImage(file='NewNoteSaveButton.png')

    mainpage.mainloop()

def protecting():
    def openApp():
        try:
            if passEntry.get() == 'Ata0010':
                passWindow.destroy()
                mainWindow()

            else:
                passLabel.config(text='You entered wrong password, try again :')
        except ValueError:
            print(None)

    passWindow = tk.Tk()
    passWindow.geometry('300x120')
    passWindow.config(bg='#ABD5C9')
    passWindow.title(' ')
    passWindow.resizable(0, 0)

    passLabel = tk.Label(passWindow, text='Enter Password to continue : ', bg='#ABD5C9')
    passLabel.config(font=('Calibri', 12))
    passLabel.place(x=20, y=20)

    passEntry = tk.Entry(passWindow, width=30, bd=3, bg='lightgrey')
    passEntry.place(x=21, y=70)

    loudButton = tk.PhotoImage(file='Enterbutton.png')
    passButton = tk.Button(passWindow, image=loudButton, bg='#ABD5C9', bd='0', activebackground='#ABD5C9',
                           command=openApp)
    passButton.place(x=230, y=60)

    passWindow.mainloop()

# protecting()
mainWindow()

