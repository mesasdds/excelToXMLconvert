import pandas as pd
import xml.etree.ElementTree as ET

def excel_to_xml(excel_file, xml_file):
    df = pd.read_excel(excel_file)
    
    categories = df.columns.tolist()
    
    # Cria o elemento raiz do XML
    root = ET.Element("data")
    
    for _, row in df.iterrows():
        car_element = ET.SubElement(root, "car")
        
        for category, value in zip(categories, row):
            category_element = ET.SubElement(car_element, category)
            category_element.tail = "\n"  # Adiciona uma quebra de linha após cada elemento de categoria
            category_element.text = str(value)
        

    
    tree = ET.ElementTree(root)
    tree.write(xml_file, encoding='utf-8', xml_declaration=True)

# Exemplo de uso
excel_file = "Pasta.xlsx"
xml_file = "dados3.xml"

excel_to_xml(excel_file, xml_file)
