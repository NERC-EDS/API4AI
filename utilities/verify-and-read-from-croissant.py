import mlcroissant as mlc

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Create a session with increased timeout and retries
session = requests.Session()
retry = Retry(connect=5, backoff_factor=1)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

# Increase default timeout (in seconds)
session.timeout = 60  # Increase to 60 seconds

# -------------------------------------------------------------

ds = mlc.Dataset("TODO/put/filepath/here.json")  # <---------------- CHANGE THIS

metadata = ds.metadata.to_json()
print(f"{metadata['name']}: {metadata['description']}")

record_sets = ds.metadata.record_sets
record_set = record_sets[0]  # gets first record set, you might have more than 1 though
print("record set:", record_set.name, "id:", record_set.id)


fields = record_set.fields
for f, field in enumerate(fields):
    print(field, field.name, field.data_type, field.description)  # print the fields within the record set

records: mlc.Records = ds.records(record_set=record_set.id)  # columns

for r, record in enumerate(records):  # i.e. rows
    print("---------------------------------------------------\n", "record ", r)
    for f, field in enumerate(record_set.fields):  # i.e. columns
        print(field.id)
        print("\t as bytes", record.get(field.id))
        print("\t\t value", record.get(field.id))

    if r >= 3:  # just the first 3 rows to illustrate data
        print("break")
        break
