from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title("Budgeting application")
    app_ui = UI(window)
    app_ui.start()
    window.mainloop()


if __name__ == '__main__':
    main()
