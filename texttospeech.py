#import to required modules
from tkinter import*
from gtts import gTTS #to speech conversion
import pygame as pg
from pygame import mixer





class text_to_speech(object):
  file_name=input('Kaydedilecek dosyanın ismini giriniz:')
  
  def __init__(self):
    self.label=Label(root, text ='Enter sentence', font ='arial 15 bold', bg ='white smoke').place(x=20,y=60)

    self.Msg = StringVar()

    self.entry_field = Entry(root,textvariable =self.Msg,bd='5')
    self.entry_field.place(x=20,y=100,width = 500)

    #define buttons
    self.play_button=Button(root, text = "PLAY" , font = 'arial 15 bold',activebackground='#00ff00', command =self.speak, width =4).place(x=25, y=140)
    self.exit_button=Button(root,text = 'EXIT',font = 'arial 15 bold' , command =self.Exit, bg = 'OrangeRed1').place(x=100,y=140) 
    self.reset_button=Button(root, text = 'RESET', font='arial 15 bold', command =self.Reset).place(x=175 , y =140)
    self.text_button=Button(root,text='TEXT',font='arial 15 bold',command=self.text,width=10).place(x=270,y=140)


  def speak(self):
    #initialize tts, create mp3 and play
    self.message=self.entry_field.get()
    self.tts = gTTS(text=self.message,lang='tr')
    self.tts.save(self.file_name + '.mp3')

    pg.mixer.init()
    pg.mixer.music.load(self.file_name + '.mp3')
    pg.mixer.music.play()

  def Exit(self):
    root.destroy()

  def Reset(self):
    self.Msg.set("")


  def text(self):
    #initializing window
    window=Tk()
    window.geometry('700x500')
    window.resizable(0,0)
    window.title('Text')
    window.config(bg='white')

    #adding a scrollbar
    self.scrollbar=Scrollbar(window)
    self.scrollbar.pack(side=RIGHT,fill=Y)
    
    
    self.window=window
    self.label=Label(window,text='Enter text',font ='arial 15 bold').place(x=20,y=60)
    self.text=Text(window,width=70,height=20,yscrollcommand=self.scrollbar.set,bd='5')
    self.text.pack()
    self.scrollbar.config(command=self.text.yview)
    self.text.place(x=20,y=100)
  
    self.string=StringVar()
    self.entry_field2=Entry(window,textvariable=self.string)
  
    #define buttons
    self.play=Button(window, text = "PLAY" , font = 'arial 15 bold',activebackground='#00ff00', command =self.text_speak, width =4).place(x=25, y=430)
    self.exit=Button(window,text = 'EXIT',font = 'arial 15 bold' , command =self.exit, bg = 'OrangeRed1').place(x=100,y=430)
    self.reset=Button(window, text = 'RESET', font='arial 15 bold', command =self.reset).place(x=175 , y =430)

  def text_speak(self):
    self.message=self.text.get("1.0","end")
    self.tts=gTTS(text=self.message,lang='tr')
    self.file_name=self.entry_field2.get()
    self.tts.save(self.file_name + '.mp3')

    pg.mixer.init()
    pg.mixer.music.load(self.file_name + '.mp3')
    pg.mixer.music.play()

  def exit(self):
    self.window.destroy()
  def reset(self):
    self.text.delete('1.0','end')


#initializing window
root=Tk()
root.geometry('700x500')
root.resizable(0,0)
root.config(bg='white')
root.title("Text to Speech")
uyg=text_to_speech()
mainloop()






  

  

 







    
#scale yap,play kısmı çalışmıyor




