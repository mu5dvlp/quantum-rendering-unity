import tkinter as tk
import threading
import socket

import server
import gui

# //＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# UDPクライアントの作成
udp_client = server.UDPClient()

# UDPクライアントを別スレッドで実行
udp_thread = threading.Thread(target=udp_client.start)
udp_thread.daemon = True
udp_thread.start()

# GUIアプリの起動
app = gui.Console(udp_client)
app.mainloop()

# アプリ終了時にUDPクライアントも停止
udp_client.stop()
