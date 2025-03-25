import mlcroissant as mlc
import json


file_object_name = "thin-section-sample"
file_object_id = file_object_name + "-id"

distribution = [
    mlc.FileObject(
        id=file_object_id,
        name=file_object_name,
        content_url="https://resources.bgs.ac.uk/petrologyThinSectionsHighResDemo/images-001.csv",
        encoding_format="text/csv",
        sha256="7fcd1af874338938234cafbd799592c82bab446b9de6765b6d4bba433e6b8d44",
    )
]

field_column_name_and_type = {
    "sample-id":mlc.DataType.TEXT,
    "parent-id":mlc.DataType.TEXT,
    "sample-name":mlc.DataType.TEXT,
    "ppl-image-url": mlc.DataType.TEXT,
    "xpl-image-url": mlc.DataType.TEXT
}

columns = []

for column_name, type in field_column_name_and_type.items():
    field_id = column_name + "-field-id"
    field_name = column_name + "-field"
    field_description = "field for column: " + column_name
    print("making column id:", field_id, field_name, field_description)
    columns.append(mlc.Field(id=field_id,
                             name=field_name,
                             description=field_description,
                             data_types=type,
                             source=mlc.Source(file_object=file_object_id, extract=mlc.Extract(column=column_name))))

record_sets = [
    # RecordSets contains records in the dataset.
    mlc.RecordSet(
        fields=columns,
        id=file_object_name + "-rs-id",
        name=file_object_name + "-rs",
    )
]

ctx = mlc.Context(
    is_live_dataset=True
)

# Metadata contains information about the dataset.
metadata = mlc.Metadata(
    ctx=ctx,
    name="bgs-sample-thin-sections-api4ai",
    # Descriptions can contain plain text or markdown.
    description=(
        "A small subset of thin-section images, for API4AI demonstration purposes, of rock samples held at BGS with pairs of plain and cross polarised images."
    ),
    cite_as=(
        "unsure"
    ),
    url="https://www.bgs.ac.uk/technologies/databases/bgs-rock-collections/",
    license="https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/",  # FOR EXAMPLE
    distribution=distribution,
    record_sets=record_sets,
    # date_published="2025-03-31T12:00:00.000000",
    version="0.0.1",
)

JSONLD = metadata.to_json()  # this returns the JSON-LD file.

pretty_json = json.dumps(JSONLD, indent=4)

print(pretty_json)
