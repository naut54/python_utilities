from tkinter import *
from tkinter import ttk
import socket
import threading

class chat_app:
    def __init__(self) -> None:
        self.clients = []
        self.usernames = []
        self.window()
        
        thread_server = threading.Thread(target = self.server)
        thread_server.setDaemon(True)
        thread_server.start()
        
        def window(self):
            root.title("Server")
            root.resizable(0, 0)
            root.geometry(f"{int(root.winfo_screenwidth()/3)}x{int(root.winfo_screenheight()/2)}")
            self.active()
            self.chat()
            
            def active(self):
                conn_F = Frame(root, width = 50)
                conn_F.pack(expand = True, side = LEFT, fill = BOTH)
                Label(conn_F,text="ACTIVO AHORA:",font=("arial",12,"bold"),bg="greenyellow",anchor=CENTER).pack(fill=BOTH)
                self.treeActive = ttk.Treeview(conn_F, columns=("port","ip","username"),show="headings")
                self.treeActive.pack(expand=True,fill=BOTH)
                
                self.treeActive.column("port",width=40)
                self.treeActive.column("ip",width=60)
                self.treeActive.column("username",width=100)

                self.treeActive.heading("port", text = "PUERTO")
                self.treeActive.heading("ip", text = "IP")
                self.treeActive.heading("username", text = "USUARIO")