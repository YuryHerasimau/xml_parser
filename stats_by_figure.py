try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import os


def get_stats_by_figure(file: str):
    tree = ET.parse(file)
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
    for file in os.listdir(dir):
        print(f"==========FIGURE STATS BY {file}==========")
        print("Figure Statistics:", get_stats_by_figure(f'{dir}/{file}'))