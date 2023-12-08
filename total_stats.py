try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import os


def get_total_images(xml_path: str):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    return len(root.findall("image"))


def get_labeled_images(xml_path: str):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    labeled_images = 0

    for image in root.findall("image"):
        if len(image.findall("*")) > 0:
            labeled_images += 1

    return labeled_images


def get_unlabeled_images(xml_path: str):
    total_images = get_total_images(xml_path)
    labeled_images = get_labeled_images(xml_path)
    return total_images - labeled_images


def get_total_figures(xml_path: str):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    total_figures = 0

    for image in root.findall("image"):
        total_figures += len(image.findall("*"))

    return total_figures


def get_figure_statistics(xml_path: str):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    figure_statistics = {}
    for image in root.findall("image"):
        for figure in image.findall("*"):
            figure_label = figure.tag
            if figure_label not in figure_statistics:
                figure_statistics[figure_label] = 0
            figure_statistics[figure_label] += 1

    return figure_statistics


def get_image_statistics(xml_path: str):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    image_sizes = []
    for image in root.findall("image"):
        name = image.get("name")
        width = int(image.get("width"))
        height = int(image.get("height"))
        area = width * height
        image_sizes.append((name, width, height, area))
        max_size = max(image_sizes, key=lambda x: x[3])
        min_size = min(image_sizes, key=lambda x: x[3])

    return max_size, min_size


if __name__ == "__main__":
    dir = "files"
    xml_files = [file for file in os.listdir(dir) if file.endswith(".xml")]
    for xml_file in os.listdir(dir):
        xml_path = os.path.join(dir, xml_file)
        print(f"==========TOTAL STATS BY {xml_file}==========")
        print("Total Images:", get_total_images(xml_path))
        print("Labeled Images:", get_labeled_images(xml_path))
        print("Unlabeled Images:", get_unlabeled_images(xml_path))
        print("Total Figures:", get_total_figures(xml_path))
        print("Figure Statistics:", get_figure_statistics(xml_path))
        max_size, min_size = get_image_statistics(xml_path)
        print(
            "Max Image Name:", max_size[0],
            "\nMax Image Size:", max_size[1], "x", max_size[2],
        )
        print(
            "Min Image Name:", min_size[0],
            "\nMin Image Size:", min_size[1], "x", min_size[2],
        )
