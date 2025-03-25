import mlcroissant as mlc


def per_recordset(record_set):
    print("===============================================================")
    print("record set:", record_set.name, "id:", record_set.id)
    fields = record_set.fields
    for f, field in enumerate(fields):
        print("Field:", field, field.name, field.data_type, field.description)

    records: mlc.Records = ds.records(record_set=record_set.id)  # columns
    print("===============================================================")

    for r, record in enumerate(records):  # i.e. columns
        print("Record, index:", r)
        for f, field in enumerate(record_set.fields):
            print("Field:", field.id, "=", record.get(field.id))  # field value is stored as bytes
            # see: C:\Data\Projects\EDS API4AI\python\make-croissant\venv\Lib\site-packages\mlcroissant\_src\operation_graph\operations\field.py LINE: ~113
            print("\t\tbytes converted to utf8:", record.get(field.id).decode('utf-8'))  # convert to utf8
        print("---------------------------------")


f = "https://resources.bgs.ac.uk/petrologyThinSectionsHighResDemo/croissant.json"
ds = mlc.Dataset(f)
metadata = ds.metadata.to_json()
print(f"{metadata['name']}: {metadata['description']}")

record_sets = ds.metadata.record_sets

for s, set in enumerate(record_sets):
    per_recordset(set)
