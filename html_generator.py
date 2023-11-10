import os

def create_complex_folder_structure():
    main_folder = "website"

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
        html_file.write("<html><head><link rel='stylesheet' type='text/css' href='assets/css/style.css'></head><body><h1>Hello, World!</h1></body></html>")

    css_file_path = os.path.join(css_folder, "style.css")
    with open(css_file_path, 'w') as css_file:
        css_file.write("body { background-color: white; }")

    print(f"Folder structure created in {os.getcwd()}/{main_folder}")

create_complex_folder_structure()