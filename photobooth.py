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
        self.bg_image = Image.open("background_christmas.jpg")  
        self.bg_image = self.bg_image.resize((800, 600), Image.LANCZOS)
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

        self.video_source = 0  # Sử dụng camera mặc định
        self.vid = cv2.VideoCapture(self.video_source)

        self.update()  # Cập nhật video
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def update(self):
        ret, frame = self.vid.read()
        if ret:
            # Chuyển đổi màu sắc từ BGR sang RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Chuyển đổi sang hình ảnh PIL
            img = Image.fromarray(frame)
            img = img.resize((400, 300), Image.LANCZOS)
            img_photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=img_photo)
            self.image_label.image = img_photo
        self.master.after(10, self.update)

    def capture_image(self):
        ret, frame = self.vid.read()
        if ret:
            # Lưu ảnh chụp
            cv2.imwrite("captured_image.jpg", frame)
            self.show_image("captured_image.jpg")

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.show_image(file_path)

    def show_image(self, file_path):
        img = Image.open(file_path)
        img = img.resize((400, 300), Image.LANCZOS)
        img_photo = ImageTk.PhotoImage(img)
        self.image_label.config(image=img_photo)
        self.image_label.image = img_photo

    def on_closing(self):
        self.vid.release()  # Giải phóng camera
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    photobooth = PhotoBooth(root)
    root.mainloop()
