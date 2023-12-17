import os
from tkinter import filedialog, messagebox


def select_path():
    path = filedialog.askdirectory()
    return path

def create_complex_folder_structure():
    selected_path = select_path()

    if selected_path:
        main_folder = os.path.join(selected_path, "website")
        os.makedirs(main_folder)

        assets_folder = os.path.join(main_folder, "assets")
        os.makedirs(assets_folder)

        css_folder = os.path.join(assets_folder, "css")
        os.makedirs(css_folder)

        img_folder = os.path.join(assets_folder, "img")
        os.makedirs(img_folder)

        js_folder = os.path.join(assets_folder, "js")
        os.makedirs(js_folder)

        dev_folder = os.path.join(assets_folder, "dev")
        os.makedirs(dev_folder)

        html_file_path = os.path.join(main_folder, "index.html")
        with open(html_file_path, 'w') as html_file:
            html_file.write("html")

        css_file_path = os.path.join(css_folder, "style.css")
        with open(css_file_path, 'w') as css_file:
            css_file.write("body")