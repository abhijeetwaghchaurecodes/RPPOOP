import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

def open_image(image_path):
    """Open an image file in a new window"""
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    window = tk.Toplevel(root)
    window.title("Image Viewer")
    label = tk.Label(window, image=photo)
    label.image = photo  # keep a reference to the photo to prevent garbage collection
    label.pack(side="top", fill="both", expand=True)
    button = tk.Button(window, text="Back", command=window.destroy)
    button.pack(side="bottom", pady=10)

# Create the first label with a blue background and rounded edges
font = ("Arial", 24)
label1 = tk.Label(root, text="Click here to open Image 1", bg="blue", font=font, bd=10, relief="ridge", padx=50, anchor="center")
label1.pack(side="left", padx=10, pady=10)
label1.bind("<Button-1>", lambda event: open_image("image1.jpg"))

# Create the second label with a red background and rounded edges
label2 = tk.Label(root, text="Click here to open Image 2", bg="red", font=font, bd=10, relief="ridge", padx=50, anchor="center")
label2.pack(side="left", padx=10, pady=10)
label2.bind("<Button-1>", lambda event: open_image("image2.jpg"))

# Center the window
"""root.update_idletasks()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
size = tuple(int(_) for _ in root.geometry().split('+')[0].split('x'))
x = w / 2 - size[0] / 2
y = h / 2 - size[1] / 2
root.geometry("%dx%d+%d+%d" % (size + (x, y)))"""

root.mainloop()
