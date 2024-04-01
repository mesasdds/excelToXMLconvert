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
            car_element.set(category, str(value))
            car_element.text = "\n"
    
    tree = ET.ElementTree(root)
    tree.write(xml_file, encoding='utf-8')


column_number = 1    
excel_file = "Pasta.xlsx"
xml_file = "dados.xml"

excel_to_xml(excel_file ,xml_file)