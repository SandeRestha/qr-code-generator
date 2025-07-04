from setuptools import setup

setup(
    name="qr_code_generator",
    version="1.0.0",
    py_modules=["qr_code_generator"],
    install_requires=[
        "qrcode",
        "pillow",
    ],
    entry_points={
        "gui_scripts": [
            "qr-code-generator=qr_code_generator:launch_gui",
        ]
    },
    author="Your Name",
    description="A GUI-based QR code generator using Tkinter and qrcode",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
