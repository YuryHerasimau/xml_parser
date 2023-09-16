try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import os


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


if __name__ == '__main__':
    dir = 'files'
    xml_files = [file for file in os.listdir(dir) if file.endswith('.xml')]
    for xml_file in xml_files:
        xml_path = os.path.join(dir, xml_file)
        print(f"Figure Statistics by {xml_file}:\n", get_figure_statistics(xml_path))