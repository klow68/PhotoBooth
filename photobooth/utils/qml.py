from pathlib import Path


def generate_qrc_file(root_dir: Path | str, relative: Path) -> None:
    """Generate the qrc files"""
    root_path = Path(root_dir)
    content = ""
    qrc_file = relative / ".qrc"
    for subdir in root_path.rglob("*"):
        if subdir.is_dir():
            for file in subdir.iterdir():
                if file.is_file() and file.suffix in (".png", ".ico", ".jpg", ".svg", ".ttf"):
                    content += (
                        f'    <file alias="{file.parent.name}/{file.name}">./{file.relative_to(relative)}</file>\n'  # noqa: W605
                    )
    if content != "":
        with open(qrc_file, "w") as qrc_file:
            qrc_file.write('<!DOCTYPE RCC><RCC version="1.0">\n')
            qrc_file.write("<qresource>\n")
            qrc_file.write(content)
            qrc_file.write("</qresource>\n")
            qrc_file.write("</RCC>\n")
