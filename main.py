import tkinter as tk
from tkinter import ttk  #untuk progress bar
from samp_client.client import SampClient
import time
#fungsi untuk mendapatkan info server SA-MP
def get_server_info(ip, port):
    try:
        with SampClient(address=ip, port=port) as client:
            info = client.get_server_info()
            return info
    except Exception as e:
        print(f"Error: {e}")
        return None

#fungsi untuk menampilkan info server di GUI
def display_server_info():
    ip = entry_ip.get()  #ambil IP dari input GUI
    port = int(entry_port.get())  #ambil port dari input GUI
    info = get_server_info(ip, port)  #panggil fungsi get_server_info
    progress_bar.start()
    root.after(100, fetch_server_info, ip, port)
   
def fetch_server_info(ip, port):       
    progress_bar.stop()
    info = get_server_info(ip, port)
    if info:
            #jika berhasil, tampilkan informasi server
        label_info.config(text=f"Server: {info.hostname}\nPlayers: {info.players}/{info.max_players}\nGamemode: {info.gamemode}")
    else:
            #jika gagal, tampilkan pesan error
        label_info.config(text="Unable to fetch server info")

#membuat window GUI
root = tk.Tk()
root.title("SA-MP Server Manager")

#input dan tombol di GUI
label_ip = tk.Label(root, text="Server IP:")
label_ip.pack()
entry_ip = tk.Entry(root)
entry_ip.pack()

label_port = tk.Label(root, text="Server Port:")
label_port.pack()
entry_port = tk.Entry(root)
entry_port.pack()

button_get_info = tk.Button(root, text="Get Server Info", command=display_server_info)
button_get_info.pack()

progress_bar = ttk.Progressbar(root, mode='indeterminate')
progress_bar.pack(pady=10)

label_info = tk.Label(root, text="")
label_info.pack()

root.mainloop()
