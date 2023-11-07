import tkinter as tk
import tkinter.filedialog as fd
import qrcode

def generate_qr_code():
    text = input_text.get()
    if not text:
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")

    result_label.config(text=f"QR Code created at: {img.filename}")

def save_qr_code():
    file_path = fd.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if file_path:
        img = qrcode.make(input_text.get())
        img.save(file_path)
        result_label.config(text=f"QR Code saved at: {file_path}")

root = tk.Tk()
root.title("QR Code Generator")

input_text = tk.Entry(root)
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
save_button = tk.Button(root, text="Save QR Code", command=save_qr_code)
result_label = tk.Label(root, text="")

input_text.pack()
generate_button.pack()
save_button.pack()
result_label.pack()

root.mainloop()

