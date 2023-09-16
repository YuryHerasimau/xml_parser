try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import os


def get_stats_by_class(xml_path: str):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    class_statistics = {}
    for image in root.findall('image'):
        for figure in image.findall('*'):
            figure_label = figure.get('label')
            if figure_label not in class_statistics:
                class_statistics[figure_label] = 0
            class_statistics[figure_label] += 1

    return class_statistics


if __name__ == '__main__':
    dir = 'files'
    xml_files = [file for file in os.listdir(dir) if file.endswith('.xml')]
    for xml_file in xml_files:
        xml_path = os.path.join(dir, xml_file)
        print(f"Class Statistics by {xml_file}:\n", get_stats_by_class(xml_path))
