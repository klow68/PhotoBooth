# PhotoBooth
Photobooth written in PySide6 QML

# WARNING: Work in progress
This is the very first stage of the photobooth project

# Install
To be able to install pycups, you need to install on:
## Debian
sudo apt-get install libcups2-dev
## Fedora
sudo dnf install cups-devel

In the repo, create the folders photos/photos_overlay
Add the necessary assets you can found them in the settings.toml
run `uv run invoke generate-qrc`
and then start the project with `uv run pb`


# Good to know
- You can print in pdf if you install on your OS cups-pdf.

- You can found your printer options with:
`lpoptions -p <printer_name> -l`
