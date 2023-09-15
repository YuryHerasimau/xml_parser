try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import os


def get_total_stats(file: str):
    try:
        tree = ET.parse(file)
        root = tree.getroot()

        marked_counter, unmarked_counter, number_of_figures = 0,0,0
        figures = ("box", "polygon", "point")

        for elem in root.findall('image'):
            # Все "соседние" узлы, которые являются первым нижестоящим элементом их родителя
            if (elem.find(f'.//{figures[0]}') is not None
            or elem.find(f'.//{figures[1]}') is not None
            or elem.find(f'.//{figures[2]}') is not None):
                marked_counter += 1
            else:
                unmarked_counter += 1

        for elem in tree.iter():
            if elem.tag in figures:
                number_of_figures += 1

        width_list, height_list = [],[]
        
        for elem in root.findall('image'):
            width_list.append(int(elem.attrib['width'].strip()))
            height_list.append(int(elem.attrib['height'].strip()))

        return f"Всего изображений: {marked_counter + unmarked_counter} \
                \nВсего изображений размечено: {marked_counter} \
                \nВсего изображений неразмечено: {unmarked_counter} \
                \nВсего фигур: {number_of_figures} \
                \nСамое большое изображение: width={max(width_list)}, height={max(height_list)} \
                \nСамое маленькое изображение: width={min(width_list)}, height={min(height_list)}"
    
    except Exception as ex:
        print('Exception :', ex)


if __name__ == '__main__':
    dir = 'files'
    for file in os.listdir(dir):
        print(f"==========TOTAL STATS BY {file}==========")
        print(get_total_stats(f'{dir}/{file}'))
