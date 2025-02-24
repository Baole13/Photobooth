import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2

class PhotoBooth:
    def __init__(self, master):
        self.master = master
        self.master.title("Photobooth Giáng Sinh")
        self.master.geometry("800x600")
        
        # Hình nền Giáng sinh
        self.bg_image = Image.open("background_christmas.jpg")  # Thay đổi đường dẫn đến hình nền của bạn
        self.bg_image = self.bg_image.resize((800, 600), Image.LANCZOS)  # ✅ Đúng
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        self.canvas = tk.Canvas(master, width=800, height=600)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_photo)
        
        self.btn_capture = tk.Button(master, text="Chụp Ảnh", command=self.capture_image)
        self.btn_capture.pack(pady=20)
        
        self.btn_upload = tk.Button(master, text="Tải Ảnh Lên", command=self.upload_image)
        self.btn_upload.pack(pady=20)

        self.image_label = tk.Label(master)
        self.image_label.pack()

    def capture_image(self):
        # Mở camera và chụp ảnh
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite("captured_image.jpg", frame)
            self.show_image("captured_image.jpg")
        cap.release()

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.show_image(file_path)

    def show_image(self, file_path):
        img = Image.open(file_path)
        img = img.resize((400, 300), Image.LANCZOS)  # Sử dụng LANCZOS thay vì ANTIALIAS
        img_photo = ImageTk.PhotoImage(img)
        self.image_label.config(image=img_photo)
        self.image_label.image = img_photo

if __name__ == "__main__":
    root = tk.Tk()
    photobooth = PhotoBooth(root)
    root.mainloop()
