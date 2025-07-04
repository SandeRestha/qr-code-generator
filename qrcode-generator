#!/usr/bin/env python3
import sys
import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox

# Verify Pillow is available for QR code image generation and preview
try:
    from PIL import Image, ImageTk
except ImportError:
    print("Error: The Pillow library (with ImageTk) is required for QR code image generation and preview.")
    print("Please install it by running: pip3 install pillow")
    sys.exit(1)


def generate_qr(url: str, filename: str) -> Image.Image:
    """Generate a QR code image from the provided URL, save to file, and return the PIL image."""
    qr = qrcode.QRCode(
        version=1,  # 21x21 modules
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    # Save to disk
    try:
        img.save(filename)
    except Exception as e:
        raise IOError(f"Failed to save QR code image: {e}")
    return img.convert('RGB')  # ensure compatibility with ImageTk


def launch_gui() -> None:
    """Builds and runs the Tkinter GUI for QR code generation and preview."""
    root = tk.Tk()
    root.title("QR Code Generator")
    root.resizable(False, False)

    # URL input
    tk.Label(root, text="Enter URL:").grid(row=0, column=0, padx=8, pady=8, sticky="e")
    url_var = tk.StringVar()
    tk.Entry(root, textvariable=url_var, width=40).grid(row=0, column=1, padx=8, pady=8)

    # Filename input
    tk.Label(root, text="Output Filename:").grid(row=1, column=0, padx=8, pady=8, sticky="e")
    filename_var = tk.StringVar(value="qrcode.png")
    tk.Entry(root, textvariable=filename_var, width=28).grid(row=1, column=1, padx=(8,0), pady=8, sticky="w")
    tk.Button(root, text="Browse…", command=lambda: _browse_file(filename_var)).grid(row=1, column=2, padx=8, pady=8)

    # Generate button
    generate_btn = tk.Button(
        root,
        text="Generate QR Code",
        width=20,
        command=lambda: _on_generate(root, url_var, filename_var)
    )
    generate_btn.grid(row=2, column=1, pady=(0,12))

    root.mainloop()


def _browse_file(filename_var: tk.StringVar) -> None:
    """Open a save-as dialog to pick the output PNG filename."""
    file = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")],
        initialfile=filename_var.get()
    )
    if file:
        filename_var.set(file)


def _on_generate(parent: tk.Tk, url_var: tk.StringVar, filename_var: tk.StringVar) -> None:
    """Validate inputs, generate the QR code, display status messages, and pop up a preview."""
    url = url_var.get().strip()
    if not url:
        messagebox.showerror("Input Error", "URL cannot be empty.", parent=parent)
        return

    filename = filename_var.get().strip() or "qrcode.png"
    try:
        # Generate and save QR code image
        img = generate_qr(url, filename)
        messagebox.showinfo("Success", f"QR code saved as:\n{filename}", parent=parent)

        # Display preview in a new window
        preview = tk.Toplevel(parent)
        preview.title("QR Code Preview")
        # Convert PIL image to a PhotoImage
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(preview, image=photo)
        label.image = photo  # keep a reference
        label.pack(padx=10, pady=10)
    except Exception as e:
        messagebox.showerror("Generation Error", f"Failed to generate QR code:\n{e}", parent=parent)


if __name__ == "__main__":
    launch_gui()
