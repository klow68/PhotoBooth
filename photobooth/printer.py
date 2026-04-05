from pathlib import Path

import cups


def print_image(image_path: Path, printer_name: str) -> None:
    """print the given image"""
    conn = cups.Connection()
    printers = conn.getPrinters()
    print(type(printer_name), type(image_path))
    if printer_name not in printers:
        print(printers)
        raise ValueError(f"Printer {printer_name} not found")
    # conn.printFile(printer_name, image_path, "Print Job", {})
    conn.printFile(
        printer_name,
        str(image_path),
        "Print Job",
        {
            "media": "Custom.100x150mm",  # or a standard size like "A6"
            # "fit-to-page": "True",        # or "scaling": "100"
            "scaling": "100",
            "orientation-requested": "3",  # 3=landscape, 4=portrait
        },
    )


# def main_printer():
#     TODO add config for printer
#     print_image("./photos.jpg","HL-L3240CDW_series")
