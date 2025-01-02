'''
파일 명: Ex24-7-Tkinter-TAB.py

Tkinter 간단한 TAB 예제
'''

import tkinter as tk
from tkinter import ttk
import sv_ttk
from PIL.ImageOps import expand


class SimpleNotebookApp:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('간단한 노트북 예제')
        self.root.geometry('400x300')
        
        sv_ttk.set_theme('light')   # dark or light

        self.setup_ui()
        
    def setup_ui(self):
        
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill = 'both', expand=True)
        
        # 노트북 생성
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill='both', expand=True)

        # 첫 번째 탭
        tab1 = ttk.Frame(notebook)
        label1 = ttk.Label(tab1, text='첫 번째 탭의 내용입니다.')
        label1.pack(padx=20, pady=20)
        notebook.add(tab1, text='탭 1')

    def run(self):
        self.root.mainloop()

# 실행코드
if __name__ == "__main__":
    app = SimpleNotebookApp()
    app.run()
