import tkinter as tk

# //＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
class Console(tk.Tk):
    def __init__(self,udp_client,title="Server Console",geometry="350x200"):
        super().__init__()
        self.udp_client = udp_client
        self.title(title)
        self.geometry(geometry)

        # self.button_terminate = tk.Button(text="Terminate")
        # self.button_terminate.pack()

        # ネットワーク
        self.frame_network = tk.Frame()
        self.frame_network.pack(pady=10)

        # ネットワーク
        # ネットワーク > Port(インバウンド)
        self.frame_network_port_inbound = tk.Frame(self.frame_network)
        self.frame_network_port_inbound.pack()
        self.label_network_port_inbound = tk.Label(self.frame_network_port_inbound,text="Port (inbound): ")
        self.label_network_port_inbound.pack(side=tk.LEFT)

        self.entry_var_port_inbound = tk.StringVar()
        self.entry_var_port_inbound.trace_add('write',self.on_value_changed_port_inbound)

        self.entry_port_inbound = tk.Entry(self.frame_network_port_inbound,width=10,textvariable=self.entry_var_port_inbound)
        self.entry_port_inbound.pack(side=tk.LEFT)
        self.entry_port_inbound.insert(0, f'{self.udp_client.port_inbound}')

        # ネットワーク > ホスト(アウトバウンド)
        self.frame_network_ip = tk.Frame(self.frame_network)
        self.frame_network_ip.pack()
        self.label_network_ip = tk.Label(self.frame_network_ip,text="IP Address: ")
        self.label_network_ip.pack(side=tk.LEFT)

        self.entry_var_host = tk.StringVar()
        self.entry_var_host.trace_add('write',self.on_value_changed_host)

        self.entry_ip = tk.Entry(self.frame_network_ip,width=15,textvariable=self.entry_var_host)
        self.entry_ip.pack(side=tk.LEFT)
        self.entry_ip.insert(0, f"{udp_client.host}")

        # ネットワーク > Port(アウトバウンド)
        self.frame_network_port_outbound = tk.Frame(self.frame_network)
        self.frame_network_port_outbound.pack()
        self.label_network_port_outbound = tk.Label(self.frame_network_port_outbound,text="Port (outbound): ")

        self.label_network_port_outbound.pack(side=tk.LEFT)
        self.entry_var_port_outbound = tk.StringVar()

        self.entry_var_port_outbound.trace_add('write',self.on_value_changed_port_outbound)
        self.entry_port_outbound = tk.Entry(self.frame_network_port_outbound,width=10,textvariable=self.entry_var_port_outbound)
        self.entry_port_outbound.pack(side=tk.LEFT)
        self.entry_port_outbound.insert(0, f'{self.udp_client.port_outbound}')

        # ブラー
        self.frame_blur = tk.Frame()
        self.frame_blur.pack(pady=10)
        # self.use_blur_var = tk.BooleanVar()
        # self.use_blur_var.trace_add('write',self.on_checkbutton_changed)
        # self.button_use_blur = tk.Checkbutton(self.frame_blur,text = "ブラーを使用",variable=self.use_blur_var)
        # self.button_use_blur.pack()
        self.frame_blur_theta = tk.Frame(self.frame_blur)
        self.frame_blur_theta.pack()
        self.label_theta = tk.Label(self.frame_blur_theta,text="Blur Strength (rad): ")
        self.label_theta.pack(side=tk.LEFT)
        self.entry_var_theta = tk.StringVar()
        self.entry_var_theta.trace_add('write',self.on_value_changed_theta)
        self.entry_theta = tk.Entry(self.frame_blur_theta,textvariable=self.entry_var_theta)
        self.entry_theta.pack(side=tk.LEFT)
        self.entry_theta.insert(0,f'{udp_client.theta}')

        self.protocol("WM_DELETE_WINDOW", self.on_closing)


    def on_value_changed_host(self,*args):
        self.udp_client.host = self.entry_var_host.get()


    def on_value_changed_port_inbound(self,*args):
        self.udp_client.port_inbound = int(self.entry_var_port_inbound.get())

    
    def on_value_changed_port_outbound(self,*args):
        self.udp_client.port_outbound = int(self.entry_var_port_outbound.get())


    def on_checkbutton_changed(self,*args):
        self.udp_client.use_blur = self.use_blur_var.get()

    def on_value_changed_theta(self,*args):
        self.udp_client.theta = float(self.entry_var_theta.get())


    def on_closing(self):
        self.udp_client.stop()
        self.destroy()

    
    def set_image(self,image):
        self.image = image

