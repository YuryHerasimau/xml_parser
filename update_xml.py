try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import os


dir = "files"
xml_files = [file for file in os.listdir(dir) if file.endswith(".xml")]

for xml_file in xml_files:
    # Полный путь к исходному XML файлу
    xml_path = os.path.join(dir, xml_file)
    # Парсинг XML файла
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        for image in root.findall("image"):
            # Изменение id изображений в обратном порядке
            image_id = image.get("id")
            image.set("id", image_id[::-1])
            # Изменение name изображений - замена расширения на 'png' и удаление пути к файлу
            image_name = image.get("name")
            # Получение только названия файла
            image_name = image_name.split("/")[-1]
            # Замена расширения на 'png'
            image_name = image_name.split(".")[0] + ".png"
            image.set("name", image_name)

        # Создание нового XML файла с изменениями
        new_xml_path = os.path.join(dir, "new_" + xml_file)
        tree.write(new_xml_path, encoding="utf-8")

    except Exception as ex:
        print("Exception:", ex)
