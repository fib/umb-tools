# convert scraper output to table row format

from dataclasses import dataclass, asdict
import json
import pprint

@dataclass
class Class:
    s: str  # subject
    n: str  # number
    t: str  # title
    c: int  # credits


data = None

with open("./../src/course_catalog.json") as f:
    data = json.loads(f.read())

new_data = []

for subject in data.keys(): 
    for course in data[subject]:
        new_data.append(
            asdict(
                Class(
                    subject,
                    course["n"],
                    course["t"],
                    course["c"],
                )
            )
        )

pprint.pp(new_data)

with open("../src/course_table_rows.json", "w") as f:
    json.dump(new_data, f)