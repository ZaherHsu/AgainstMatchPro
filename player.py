import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("第一届\"大力神\"杯")
        self.root.geometry("400x300")
        # 创建比赛选手列表
        self.Text = tk.Text(self.root)
        self.Text.pack()
        self.Text.config(height=20)

        # 创建按钮，点击时调用 open_new_window 函数
        self.button = tk.Button(self.root, text="进入比赛", command=self.open_new_window)
        self.button.pack()

    def open_new_window(self):
        # 获取文本输入框中的文本
        text = self.Text.get("0.5", "end")
        self.players = list(filter(None, text.split('\n')))
        
        # 创建一个新窗口
        self.new_window = tk.Toplevel(self.root)
        # 在新窗口中添加标签
        self.new_window.title("第一届\"大力神\"杯")
        self.new_window.geometry("400x400")
        self.new_window.geometry("+{}+{}".format(int(self.new_window.winfo_screenwidth()/2 - self.new_window.winfo_width()/2)-200,
                              int(self.new_window.winfo_screenheight()/2 - self.new_window.winfo_height()/2)-150))
        self.create_widgets()
        # 关闭当前窗口
        # self.root.destroy()

    def create_widgets(self):
        # 创建淘汰赛对阵表标签
        tk.Label(self.new_window, text="淘汰赛对阵表").pack()

        # 创建选手列表框
        self.listbox = tk.Listbox(self.new_window, selectmode=tk.MULTIPLE)
        for player in self.players:
            self.listbox.insert(tk.END, player)
        self.listbox.pack()

        # 创建显示选手输赢文本框
        self.result_text = tk.Text(self.new_window, height=2, width=10)
        self.result_text.pack()

        # 创建单选按钮
        self.selected = tk.IntVar()
        tk.Radiobutton(self.new_window, text="Player 1", value=1, variable=self.selected).pack()
        tk.Radiobutton(self.new_window, text="Player 2", value=2, variable=self.selected).pack()

        # 创建比赛按钮
        tk.Button(self.new_window, text="比赛开始", command=self.play_match).pack()

    def play_match(self):
        # 获取选中的选手
        selected = self.listbox.curselection()
        if len(selected) != 2:
            info_window = tk.messagebox.showerror("错误", "请选择仅两名选手进行比赛！")
            self.new_window.after(1000, info_window.destroy)
            return

        # 获取获胜的选手
        winner = int(self.selected.get())
        if winner == 1:
            winner = self.listbox.get(selected[0])
            loser = self.listbox.get(selected[1])
            
            # 将输的选手从选手列表中删除
            self.listbox.delete(selected[1])
            self.listbox.itemconfigure(selected[0], {'fg': 'green'})
        else:
            winner = self.listbox.get(selected[1])
            loser = self.listbox.get(selected[0])
            # 将输的选手从选手列表中删除
            self.listbox.delete(selected[0])
            self.listbox.itemconfigure(selected[0], {'fg': 'green'})
        
        # 更新文本框内容
        self.result_text.insert(tk.END, "{} wins!\n".format(winner))

        # # 移除输的选手
        # loser = self.listbox.get(selected[1])
        # self.listbox.delete(selected[1])
        # winner = self.listbox.get(selected[0])
        # self.listbox.itemconfigure(selected[0], {'fg': 'green'})

        # 如果只剩下一名选手，则比赛结束
        if self.listbox.size() == 1:
            tk.messagebox.showinfo("恭喜", f"{winner} 是冠军!")
            self.new_window.destroy()

    def add_player(self):
        # 从文本框中获取新选手的名字
        new_player = self.entry.get()
        if not new_player:
            tk.messagebox.showerror("错误", "请输入一名选手姓名")
            return
        self.entry.delete(0, tk.END)

        # 将新选手添加到选手列表中
        self.listbox.insert(tk.END, new_player)

    def reset(self):
        # 重置选手列表和文本框
        self.listbox.delete(0, tk.END)
        for player in self.players:
            self.listbox.insert(tk.END, player)
        self.entry.delete(0, tk.END)


if __name__ == '__main__':
   # 创建并启动应用程序
    app = App()
    app.root.mainloop()