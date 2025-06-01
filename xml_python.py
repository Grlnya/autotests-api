import xml.etree.ElementTree as ET

xml_data = """
<person>
    <id>1</id>
    <first_name>John</first_name>
    <last_name>Doe</last_name>
    <email>jhon.doe@example.com</email>
    <adress>
        <street>Main Street 1</street>
        <city>New York</city>
        <zip>10001</zip>
    </adress>
</person>
"""

root = ET.fromstring(xml_data)

print(root.find('id').text)