try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import os


def get_total_images(xml_path: str):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    return len(root.findall('image'))


def get_labeled_images(xml_path: str):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    labeled_images = 0

    for image in root.findall('image'):
        if len(image.findall('*')) > 0:
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

    for image in root.findall('image'):
        total_figures += len(image.findall('*'))
        
    return total_figures


def get_figure_statistics(xml_path: str):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    figure_statistics = {}
    for image in root.findall('image'):
        for figure in image.findall('*'):
            figure_label = figure.tag
            if figure_label not in figure_statistics:
                figure_statistics[figure_label] = 0
            figure_statistics[figure_label] += 1

    return figure_statistics


def get_image_statistics(xml_path: str):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    image_statistics = {}
    for image in root.findall('image'):
        image_id = image.get('id')
        image_width = int(image.get('width'))
        image_height = int(image.get('height'))
        image_statistics[image_id] = {'width': image_width, 'height': image_height}

    return image_statistics


def get_max_min_image(xml_path: str):
    image_statistics = get_image_statistics(xml_path)

    max_width = max(image['width'] for image in image_statistics.values())
    max_height = max(image['height'] for image in image_statistics.values())
    min_width = min(image['width'] for image in image_statistics.values())
    min_height = min(image['height'] for image in image_statistics.values())

    max_images = sum(1 for image in image_statistics.values() if image['width'] == max_width and image['height'] == max_height)
    min_images = sum(1 for image in image_statistics.values() if image['width'] == min_width and image['height'] == min_height)

    return max_width, max_height, min_width, min_height, max_images, min_images 


if __name__ == '__main__':
    dir = 'files'
    xml_files = [file for file in os.listdir(dir) if file.endswith('.xml')]
    for xml_file in os.listdir(dir):
        xml_path = os.path.join(dir, xml_file)
        print(f"==========TOTAL STATS BY {xml_file}==========")
        print("Total Images:", get_total_images(xml_path))
        print("Labeled Images:", get_labeled_images(xml_path))
        print("Unlabeled Images:", get_unlabeled_images(xml_path))
        print("Total Figures:", get_total_figures(xml_path))
        print("Figure Statistics:", get_figure_statistics(xml_path))
        max_width, max_height, min_width, min_height, max_images, min_images = get_max_min_image(xml_path)
        print("Max Image Size:", max_width, "x", max_height)
        print("Min Image Size:", min_width, "x", min_height)
        print("Number of Max Images:", max_images)
        print("Number of Min Images:", min_images)
