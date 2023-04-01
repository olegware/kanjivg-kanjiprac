import os
import xml.etree.ElementTree as ET

kanji_folder = "C:/Users/Path/to/your/kanji/svg/files"  # add actual path to your kanji folder with svg files
output_file = "kanjivg_merged.xml"

kanji_files = [f for f in os.listdir(kanji_folder) if f.endswith(".svg")]

root = ET.Element("kanjivg")
root.set("xmlns", "http://kanjivg.tagaini.net")

for filename in kanji_files:
    file_path = os.path.join(kanji_folder, filename)
    tree = ET.parse(file_path)
    kanji_element = tree.getroot()
    root.append(kanji_element)

merged_tree = ET.ElementTree(root)
merged_tree.write(output_file, encoding="utf-8", xml_declaration=True)
