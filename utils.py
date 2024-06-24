import base64
from xml_parser.stage_2 import stage_2_parse_xml
from xml_parser.stage_1 import read_and_store_single_xml


def parse_contents(contents, filename, process):
    content_type, content_string = contents.split(",")
    decoded = base64.b64decode(content_string)
    try:
        if "xml" in filename:
            if process == "Stage 1":
                data = read_and_store_single_xml(decoded)
            else:
                data = stage_2_parse_xml(decoded)
            return data
    except Exception as e:
        return str(e)
