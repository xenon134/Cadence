from tkinter import font

style = {
    "bgColor": "#121212",
    "fgColor": "white",
    "root": {"title": "Music App", "geometry": "1200x400"},  # size of window
    "openScreen": {  # opening screen
        "openButton": {
            "text": "Open File(s)",
            "font": lambda: font.Font(family="tahoma", size=23),
            "width": 40,
            "pady": 13,
        },
        "youtubeButton": {
            "text": "Load from YouTube",
            "font": lambda: font.Font(family="tahoma", size=23),
            "width": 40,
            "pady": 13,
        },
        "youtubeLinkBox": {
            "title": "YouTube Link",
            "geometry": "400x200",
            "text": "Enter YouTube link:",
        },
        "filedialog": {"title": "Open ..."},
    },
    "messages": {
        "pygameError": {
            "title": "",
            "message": """This environment does not meet the minimum requirements to run this program.

Minumum System Requirements:
    Python 3
    Tkinter 8.6
    Pygame 1.9

Recommended System Requirements:
    Python 3
    tkinter 8.6
    pygame 2.0
    eyed3 0.9.6
    CPU: Core i3 2.4 GHz
    GPU: AMD Rodeon HD 7870""",
        },
        "pygameWarning": {
            "title": "Version Warning!!",
            "message": f'You are using pygame version {__import__("pygame").version.ver}; however, you should consider upgrading to at least version 2',
        },
        "python2warning": {
            "title": "Version Warning!!",
            "message": f'You are using python version {__import__("sys").version}; however, you should consider upgrading to at least python 3',
        },
        "eyed3warning": {
            "title": "Import Warning",
            "message": "You may not have eyed3 installed. You should consider installing eyed3 0.9.6 for all features to work correctly.",
        },
    },
    "playScreen": {
        "trackNoLabel": {
            "font": lambda: font.Font(family="times new roman", size=20),
        },
        "volumeBar": {
            "lineColor": "white",
            "barColor": "#add8e6",
            "barRadius": 5,
            "lineWidth": 2,
        },
    },
}
