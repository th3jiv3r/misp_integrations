import requests
import json
import time
from datetime import datetime
from pymisp import ExpandedPyMISP

misp = ExpandedPyMISP(url='Your MISP', key='API KEY', ssl='True')

response = requests.get("http://api.cybercure.ai/feed/get_url",
                       headers={"Accept": "application/json"},
                       params={"output": "json"})

var = json.loads(response.text)
now = datetime.now()
ts = time.time()
attr = []
for feed in var["data"]["urls"]:
    attribute = {
        "comment": "Known Malicious",
        "category": "External analysis",
        "timestamp": ts,
        "to_ids": False,
        "value": feed,
        "disable_correlation": False,
        "object_relation": "",
        "type": "url"
    }
    attr.append(attribute)
    EventDict = {
        "Event": {
            "info": "Cyber Cure Known Bad",
            "publish timestamp": ts,
            "analysis": 2,
            "Tag": {
                "colour": "#ff0000",
                "exportable": True,
                "name": "Malicious URLs"
            },
            "Attribute": attr,
            "threat_level_id": "1",
            "extends_uuid": "",
            "published": False,
            "date": now.strftime("%Y-%m-%d"),
            "Orgc": {
                "uuid": "Your UUID",
                "name": "Cyber Curet"
            },

        }
        }
misp.add_event(EventDict)
