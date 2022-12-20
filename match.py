import tkinter as tk


class App:
    def __init__(self, players):
        self.players = players
        # 创建窗口，标签
        self.root = tk.Tk()
        self.root.title("第一届\"大力神\"杯")
        self.root.geometry("400x300")
        self.root.geometry("+{}+{}".format(int(self.root.winfo_screenwidth()/2 - self.root.winfo_width()/2)-200,
                              int(self.root.winfo_screenheight()/2 - self.root.winfo_height()/2)-150))
        self.create_widgets()

    def create_widgets(self):
        # 创建淘汰赛对阵表标签
        tk.Label(self.root, text="淘汰赛对阵表").pack()

        # 创建选手列表框
        self.listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE)
        for player in self.players:
            self.listbox.insert(tk.END, player)
        self.listbox.pack()

        # 创建单选按钮
        self.selected = tk.IntVar()
        tk.Radiobutton(self.root, text="Player 1", value=1, variable=self.selected).pack()
        tk.Radiobutton(self.root, text="Player 2", value=2, variable=self.selected).pack()

        # 创建比赛按钮
        tk.Button(self.root, text="比赛开始", command=self.play_match).pack()

    def play_match(self):
        # 获取选中的选手
        selected = self.listbox.curselection()
        if len(selected) != 2:
            tk.messagebox.showerror("错误", "请选择仅两名选手进行比赛！")
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
        
        # # 移除输的选手
        # loser = self.listbox.get(selected[1])
        # self.listbox.delete(selected[1])
        # winner = self.listbox.get(selected[0])
        # self.listbox.itemconfigure(selected[0], {'fg': 'green'})

        # 如果只剩下一名选手，则比赛结束
        if self.listbox.size() == 1:
            tk.messagebox.showinfo("恭喜", f"{winner} 是冠军!")
            self.root.destroy()

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
    # 创建比赛选手列表
    players = ["小红", "小绿", "小黄", "小蓝"]

    # 创建并启动应用程序
    app = App(players)
    app.root.mainloop()
