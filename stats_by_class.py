try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import os


def get_stats_by_class(file: str):
    tree = ET.parse(file)
    root = tree.getroot()

    ignore_counter, fur_counter, item_counter = 0,0,0
    classes = ("ignore", "fur", "item")
    figures = ("box", "polygon", "point")
             
    for elem in root.iter('polygon'):
        if elem.attrib.get('label') == f'{classes[0]}':
            ignore_counter += 1
        elif elem.attrib.get('label') == f'{classes[1]}':
            fur_counter += 1
        elif elem.attrib.get('label') == f'{classes[2]}':
            item_counter += 1

    return f"Класс {classes[0]}: {ignore_counter} фигур  \
            \nКласс {classes[1]}: {fur_counter} фигур \
            \nКласс {classes[2]}: {item_counter} фигур "


if __name__ == '__main__':
    dir = 'files'
    for file in os.listdir(dir):
        print(f"==========STATS BY CLASSES BY {file}==========")
        print(get_stats_by_class(f'{dir}/{file}'))
