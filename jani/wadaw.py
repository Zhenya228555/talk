from customtkinter import*
from PIL  import Image
from socket import *
import threading

windows = CTk()
windows.geometry("400x600")


client = socket(AF_INET , SOCK_STREAM)

client.connect(("0.tcp.eu.ngrok.io", 14202))

def send_message():
    while True:
        client_message = input()
        client.send(f"женя {client_message.encode()}")


threading.Thread(target=send_message).start()
def jpojpopo():
    while True:
        try:
            message = client.recv(1024).decode().strip()
            print(message)
            message_dox.configure(state="normal")
            message_dox.insert(END,  message + "\n")
            message_dox.configure(state="disable")
        except:
            pass
threading.Thread(target=jpojpopo).start()
#-----FREIM1-----
fr1 = CTkFrame(windows, height=500,width=550)
fr1.pack_propagate(False)
fr1.pack(pady = 10)

message_dox= CTkTextbox(fr1, height=400,width=350)
message_dox.configure(state="disabled")
message_dox.pack()


#-----FREIM2----
fr2 = CTkFrame(windows, height=100,width=350)
fr2.pack_propagate(False)
fr2.pack(pady = 10)

entry =CTkEntry(fr2,placeholder_text="Напешіть повидомленя...",
                height= 60,width= 230)
entry.pack(pady = 20, side = "left",padx=10)

img_load = Image.open("foto/wwww.png")
ready_image = CTkImage(light_image= img_load, size=(20,20))

def click_sent():
    a=entry.get()
    entry.delete(0,END)
    client.send(a.encode())
    message_dox.configure(state="normal")
    message_dox.insert(END,  a + "\n")
    message_dox.configure(state="disable")



btn_send = CTkButton(fr2, text="SEND", image = ready_image, compound="right", width=20, height= 60,command=click_sent)
btn_send.pack(pady = 20)
windows.mainloop()