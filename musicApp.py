from style import style

try:
    import tkinter as tk
    from tkinter import font
except:
    import Tkinter as tk
    from Tkinter import font, messagebox

    messagebox.showwarning(
        title=style["messages"]["python2warning"]["title"],
        message=style["messages"]["python2warning"]["message"],
    )

root = tk.Tk()
root.configure(bg=style["bgColor"])
root.title(style["root"]["title"])
root.geometry(style["root"]["geometry"])
root.resizable(False, False)


class OpeningScreen:
    def draw(this):
        this.opnBtn = tk.Button(
            root,
            text=style["openScreen"]["openButton"]["text"],
            bg=style["bgColor"],
            fg=style["fgColor"],
            font=style["openScreen"]["openButton"]["font"](),
            width=style["openScreen"]["openButton"]["width"],
            pady=style["openScreen"]["openButton"]["pady"],
            command=this.opnCmd,
        )
        this.opnBtn.place(anchor="center", relx=0.5, rely=0.34)
        this.ytdBtn = tk.Button(
            root,
            text=style["openScreen"]["youtubeButton"]["text"],
            bg=style["bgColor"],
            fg=style["fgColor"],
            font=style["openScreen"]["youtubeButton"]["font"](),
            width=style["openScreen"]["youtubeButton"]["width"],
            pady=style["openScreen"]["youtubeButton"]["pady"],
            command=this.ytdCmd,
        )
        this.ytdBtn.place(anchor="center", relx=0.5, rely=0.66)

    def destroy(this):
        this.opnBtn.destroy()
        this.ytdBtn.destroy()

    def opnCmd(this):
        from tkinter import filedialog

        fs = filedialog.askopenfilenames(
            parent=root, title=style["openScreen"]["filedialog"]["title"]
        )
        if fs:
            global plyScrn, player
            this.destroy()
            player = Player(fs)
            plyScrn = PlayScreen(player)
            plyScrn.draw()

    def ytdCmd(this):
        stl = style["openScreen"]["youtubeLinkBox"]
        ylnRt = tk.Tk()
        ylnRt.configure(bg=style["bgColor"])
        ylnRt.title(stl["title"])
        ylnRt.geometry(stl["geometry"])
        tk.Label(ylnRt, text=stl["text"]).pack()


class PlayScreen:
    def __init__(this, player):
        this.player = player
        this.draw()

    def draw(this):
        this.tnoLbl = tk.Label(
            root,
            fg=style["fgColor"],
            bg=style["bgColor"],
            font=style["playScreen"]["trackNoLabel"]["font"](),
        )
        this.updateTrackLbl()
        this.tnoLbl.place(anchor="center", relx=0.5, rely=0.2)
        imgtemp = tk.PhotoImage(file="pauseIcon.gif", format="gif")

        this.plpBtn = tk.Button(
            root, image=imgtemp, bd=0, bg=style["bgColor"], command=PlayScreen.toggle
        )
        this.plpBtn.pauImg = imgtemp
        this.plpBtn.plyImg = tk.PhotoImage(file="playIcon.gif", format="gif")
        this.plpBtn.play = True
        this.plpBtn.place(anchor="center", relx=0.5, rely=0.9)

        imgtemp = tk.PhotoImage(file="nextIcon.gif", format="gif")
        this.nxtBtn = tk.Button(
            root,
            image=imgtemp,
            bd=0,
            bg=style["bgColor"],
            state=tk.DISABLED if len(player.playlist) == 1 else tk.NORMAL,
            command=PlayScreen.next,
        )
        this.nxtBtn.image = imgtemp
        this.nxtBtn.place(anchor="center", relx=0.56, rely=0.9)

        imgtemp = tk.PhotoImage(file="previousIcon.gif", format="gif")
        this.prvBtn = tk.Button(
            root,
            image=imgtemp,
            bd=0,
            bg=style["bgColor"],
            state=tk.DISABLED,
            command=PlayScreen.previous,
        )
        this.prvBtn.image = imgtemp
        this.prvBtn.place(anchor="center", relx=0.44, rely=0.9)

        imgtemp = tk.PhotoImage(file="playlistIcon.gif", format="gif")
        this.lstBtn = tk.Button(
            root,
            image=imgtemp,
            bd=0,
            bg=style["bgColor"],
            command=PlayScreen.displayPlaylist,
        )
        this.lstBtn.image = imgtemp
        this.lstBtn.place(anchor="center", relx=0.66, rely=0.9)

        imgtemp = tk.PhotoImage(file="stopIcon.gif", format="gif")
        this.stpBtn = tk.Button(
            root, image=imgtemp, bd=0, bg=style["bgColor"], command=PlayScreen.stop
        )
        this.stpBtn.image = imgtemp
        this.stpBtn.place(anchor="center", relx=0.34, rely=0.9)

        imgtemp = tk.PhotoImage(file="volumeIcon.gif", format="gif")
        this.vlmLbl = tk.Label(root, image=imgtemp, bd=0)
        this.vlmLbl.image = imgtemp
        this.vlmLbl.place(anchor="center", relx=0.72, rely=0.9)

        from tkSliderWidget import Slider

        this.vlmBar = Slider(
            root,
            width=width * 0.204,
            height=50,
            init_lis=[1],
            bg=style["bgColor"],
            lineColor=style["playScreen"]["volumeBar"]["lineColor"],
            barColor=style["playScreen"]["volumeBar"]["barColor"],
            barRadius=style["playScreen"]["volumeBar"]["barRadius"],
            lineWidth=style["playScreen"]["volumeBar"]["lineWidth"],
            show_value=True,
        )
        this.vlmBar.place(anchor="w", relx=0.75, rely=0.9)
        this.updateVolume()

    def destroy(this):
        print("In plyScrn.destroy")
        this.tnoLbl.destroy()
        this.plpBtn.destroy()
        this.nxtBtn.destroy()
        this.prvBtn.destroy()
        this.lstBtn.destroy()
        this.stpBtn.destroy()
        this.vlmBar.destroy()
        print("Elements destroyed.")

    def toggle():
        if plyScrn.plpBtn.play:
            player.pause()
            plyScrn.plpBtn.play = False
            plyScrn.plpBtn.configure(image=plyScrn.plpBtn.plyImg)
        else:
            player.play()
            plyScrn.plpBtn.play = True
            plyScrn.plpBtn.configure(image=plyScrn.plpBtn.pauImg)

    def next():
        player.next()
        if not player.nowplaying < len(player.playlist) - 1:
            plyScrn.nxtBtn.configure(state=tk.DISABLED)
        plyScrn.prvBtn.configure(state=tk.NORMAL)
        plyScrn.updateTrackLbl()

    def previous():
        player.previous()
        if not player.nowplaying > 0:
            plyScrn.prvBtn.configure(state=tk.DISABLED)
        plyScrn.nxtBtn.configure(state=tk.NORMAL)
        plyScrn.updateTrackLbl()

    def stop():
        global opnScrn
        player.stop()
        plyScrn.destroy()
        opnScrn = OpeningScreen()
        opnScrn.draw()

    def displayPlaylist():
        from tkinter import messagebox

        messagebox.showerror(
            title="Not Implemented Yet!",
            message="This feature will be available in a future version",
        )

    def updateTrackLbl(this):
        try:
            import eyed3

            f = eyed3.load(player.playlist[player.nowplaying]).tag
            if not f.title:
                raise Exception()
            track = f.title
            if f.artist:
                track += "\n" + f.artist
            if f.album:
                track += "\n" + f.album
        except Exception:
            from tkinter import messagebox

            messagebox.showwarning(
                title=style["messages"]["eyed3warning"]["title"],
                message=style["messages"]["eyed3warning"]["message"],
            )
            from os.path import split

            track = split(player.playlist[player.nowplaying])[1]
            track = track.replace(".mp3", "")
        this.tnoLbl.configure(
            text=f"Playing track {player.nowplaying+1} of {len(player.playlist)}:\n{track}"
        )

    def updateVolume(this):
        player.volume(this.vlmBar.getValues()[0])
        this.vlmBar.after(10, PlayScreen.updateVolume, this)


class Player:
    def __init__(this, playlist):
        this.playlist = list(playlist)
        try:
            from pygame import mixer
        except:
            from tkinter import messagebox

            messagebox.showerror(
                title=style["messages"]["pygameError"]["title"],
                message=style["messages"]["pygameError"]["message"],
            )
            root.destroy()
        mixer.init()
        this.nowplaying = -1
        this.music = mixer.music
        this.next()

    def play(this):
        this.music.unpause()

    def pause(this):
        this.music.pause()

    def previous(this):
        this.nowplaying -= 1
        this.reload()

    def next(this):
        this.nowplaying += 1
        this.reload()

    def stop(this):
        this.music.stop()

    def volume(this, set2):
        this.music.set_volume(set2)

    def reload(this):
        try:
            this.music.stop()
            this.music.unload()
        except AttributeError:
            global pygameWarned
            if not pygameWarned:
                from tkinter import messagebox

                messagebox.showwarning(
                    title=style["messages"]["pygameWarning"]["title"],
                    message=style["messages"]["pygameWarning"]["message"],
                )
                pygameWarned = True
        this.music.load(this.playlist[this.nowplaying])
        this.music.play()

    def seek(this, time):
        pass


def showPreferences():
    from tkinter import messagebox

    messagebox.showerror(
        title="Not Implemented Yet!",
        message="This feature will be available in a future version",
    )


imgtemp = tk.PhotoImage(file="preferencesIcon.gif", format="gif")
prfBtn = tk.Button(
    root, image=imgtemp, bd=0, bg=style["bgColor"], command=showPreferences
)
prfBtn.image = imgtemp
width, height = [int(i) for i in style["root"]["geometry"].split("x")]
prfBtn.place(anchor="ne", x=width - 10, y=10)

pygameWarned = False
eyed3warned = False

opnScrn = OpeningScreen()
plyScrn = None
player = None
opnScrn.draw()
root.mainloop()
