import tkinter as tk

def Kirby_Victory():
    win = tk.Tk()
    win.title("CONGRATULATIONS")
    win.geometry("500x500")
    win.configure(bg = "#FFB7C5")


    title = tk.Label(win, text = "AWESOME!, AMAZING!, GREAT!, COOL!", font =("Arial", 23, "bold"), bg = "#FFB7C5")

    title.pack(pady=20)




    route = os.path.dirname(__file___)
    imagen = os.path.join(ruta, "Kirby Feliz.jpeg")


    img = tk.PhotoImage(file=foto_path)

    panel = tk.Label(win, image=img, bg="#FFB7C5")
    panel.image = img
    panel.pack()


except:

tk.Label(win, text = "POYO", command= win.destroy, width= )
