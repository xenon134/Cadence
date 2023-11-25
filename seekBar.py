from style import style
import tkinter as tk


class SeekBar(tk.Frame):
    def __init__(this, root, maxVal, width):
        tk.Frame.__init__(this, root, height=7, width=width, bg=style["bgColor"], bd=0)
        this.root = root
        this.value = 0
        this.maxVal = maxVal
        this.canv = tk.Canvas(
            this, height=7, width=width, bg=style["bgColor"], bd=0, highlightthickness=0
        )
        this.canv.pack()
        this.canv.bind("<Motion>", this._mouseMotion)
        this.canv.bind("<B1-Motion>", this._moveBar)
        this.drawCurs(0)

    def _mouseMotion(this, event):
        x = event.x
        y = event.y
        if this._checkSelection(x, y):
            this.canv.config(cursor="hand2")
        else:
            this.canv.config(cursor="")

    def _moveBar(this, event):
        x = event.x
        y = event.y

    def drawCurs(at):
        pass


root = tk.Tk()
skbr = SeekBar(root, 211, 1000)
skbr.pack()
root.mainloop()
