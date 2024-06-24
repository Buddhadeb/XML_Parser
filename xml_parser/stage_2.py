import xml.etree.ElementTree as ET


# Define a function to parse a single XML file and extract data
def stage_2_parse_xml(file_content):
    ns = {
        "ns": "urn:iso:std:iso:20022:tech:xsd:pain.009.001.01"
    }  # Namespace definition
    tree = ET.ElementTree(ET.fromstring(file_content))
    root = tree.getroot()

    def find_text(element, path):
        found = element.find(path, ns)
        return found.text if found is not None else "N/A"

    def find_attrib(element, path, attrib):
        found = element.find(path, ns)
        return (
            found.attrib.get(attrib)
            if found is not None and attrib in found.attrib
            else "N/A"
        )

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
        "MndtId": find_text(root, ".//ns:MndtId"),
        "MndtReqId": find_text(root, ".//ns:MndtReqId"),
        "SvcLvl_Prtry": find_text(root, ".//ns:Tp/ns:SvcLvl/ns:Prtry"),
        "LclInstrm_Prtry": find_text(root, ".//ns:Tp/ns:LclInstrm/ns:Prtry"),
        "SeqTp": find_text(root, ".//ns:Ocrncs/ns:SeqTp"),
        "Frqcy": find_text(root, ".//ns:Ocrncs/ns:Frqcy"),
        "FrDt": find_text(root, ".//ns:Ocrncs/ns:Drtn/ns:FrDt"),
        "FrstColltnDt": find_text(root, ".//ns:Ocrncs/ns:FrstColltnDt"),
        "FnlColltnDt": find_text(root, ".//ns:Ocrncs/ns:FnlColltnDt"),
        "MaxAmt": find_text(root, ".//ns:MaxAmt"),
        "MaxAmt_Ccy": find_attrib(root, ".//ns:MaxAmt", "Ccy"),
        "Cdtr_Nm": find_text(root, ".//ns:Cdtr/ns:Nm"),
        "CdtrAcct_Id": find_text(root, ".//ns:CdtrAcct/ns:Id/ns:Othr/ns:Id"),
        "CdtrAgt_Nm": find_text(root, ".//ns:CdtrAgt/ns:FinInstnId/ns:Nm"),
        "CdtrAgt_MmbId": find_text(
            root, ".//ns:CdtrAgt/ns:FinInstnId/ns:ClrSysMmbId/ns:MmbId"
        ),
        "Dbtr_Nm": find_text(root, ".//ns:Dbtr/ns:Nm"),
        "Dbtr_Id": find_text(root, ".//ns:Dbtr/ns:Id/ns:PrvtId/ns:Othr/ns:Id"),
        "DbtrAcct_Id": find_text(root, ".//ns:DbtrAcct/ns:Id/ns:Othr/ns:Id"),
        "DbtrAcct_Tp": find_text(root, ".//ns:DbtrAcct/ns:Tp/ns:Prtry"),
        "DbtrAgt_Nm": find_text(root, ".//ns:DbtrAgt/ns:FinInstnId/ns:Nm"),
        "DbtrAgt_MmbId": find_text(
            root, ".//ns:DbtrAgt/ns:FinInstnId/ns:ClrSysMmbId/ns:MmbId"
        ),
    }

    return data
