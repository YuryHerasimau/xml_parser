try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import os


dir = 'files'
xml_files = [file for file in os.listdir(dir) if file.endswith('.xml')]

for xml_file in xml_files:
    # Полный путь к исходному XML файлу
    xml_path = os.path.join(dir, xml_file)
    # Парсинг XML файла
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        # # Изменение id изображений в обратном порядке
        images = root.findall('image')
        for i in range(len(images)):
            images[i].attrib['id'] = str(len(images) - i)

        # Изменение name изображений - замена расширения на 'png' и удаление пути к файлу
        for image in images:
            name = image.attrib['name']
            name = name.split('/')[-1]              # Получение только названия файла
            name = name.split('.')[0] + '.png'      # Замена расширения на 'png'
            image.attrib['name'] = name

        # Создание нового XML файла с изменениями
        new_xml_path = os.path.join(dir, 'new_' + xml_file)
        tree.write(new_xml_path, encoding="utf-8")
    
    except Exception as ex:
        print('Exception:', ex)
    