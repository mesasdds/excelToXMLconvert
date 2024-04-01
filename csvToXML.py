import pandas as pd
import xml.etree.ElementTree as ET

def csv_to_xml(csv_file, xml_file):
    df = pd.read_csv(csv_file)
    
    categories = df.columns.tolist()
    
    # Cria o elemento raiz do XML
    root = ET.Element("data")
    
    for _, row in df.iterrows():
        car_element = ET.SubElement(root, "car")
        
        for category, value in zip(categories, row):
            category_element = ET.SubElement(car_element, category)
            category_element.text = str(value)
            category_element.tail = "\n"  # Adiciona uma quebra de linha após cada elemento de categoria
        
        car_element.text = "\n"  # Adiciona uma quebra de linha ao final de cada carro
    
    tree = ET.ElementTree(root)
    tree.write(xml_file, encoding='utf-8', xml_declaration=True)

# Exemplo de uso
csv_file = "Medicaldataset.csv"
xml_file = "dados2.xml"

csv_to_xml(csv_file, xml_file)
