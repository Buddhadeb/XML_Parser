import xml.etree.ElementTree as ET


def read_and_store_single_xml(file_content):
    ns = {
        "ns": "urn:iso:std:iso:20022:tech:xsd:pain.012.001.01"
    }  # Namespace definition
    tree = ET.ElementTree(ET.fromstring(file_content))
    root = tree.getroot()

    def find_text(element, path):
        found = element.find(path, ns)
        return found.text if found is not None else "N/A"

    data = {
        "MsgId": find_text(root, ".//ns:MsgId"),
        "CreDtTm": find_text(root, ".//ns:CreDtTm"),
        "InstgAgt_Nm": find_text(root, ".//ns:InstgAgt/ns:FinInstnId/ns:Nm"),
        "InstgAgt_MmbId": find_text(
            root, ".//ns:InstgAgt/ns:FinInstnId/ns:ClrSysMmbId/ns:MmbId"
        ),
        "InstdAgt_Nm": find_text(root, ".//ns:InstdAgt/ns:FinInstnId/ns:Nm"),
        "InstdAgt_MmbId": find_text(
            root, ".//ns:InstdAgt/ns:FinInstnId/ns:ClrSysMmbId/ns:MmbId"
        ),
        "OrgnlMsgInf_MsgNmId": find_text(root, ".//ns:OrgnlMsgInf/ns:MsgNmId"),
        "OrgnlMsgInf_CreDtTm": find_text(root, ".//ns:OrgnlMsgInf/ns:CreDtTm"),
        "AccptncRslt_Accptd": find_text(root, ".//ns:AccptncRslt/ns:Accptd"),
        "RjctRsn_Prtry": find_text(root, ".//ns:RjctRsn/ns:Prtry"),
        "OrgnlMndt_OrgnlMndtId": find_text(root, ".//ns:OrgnlMndt/ns:OrgnlMndtId"),
    }

    return data
