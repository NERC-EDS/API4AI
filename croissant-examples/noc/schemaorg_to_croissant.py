"""Tool for converting a Schema.org JSON-LD file to a croissant compliant JSON."""

import json
from datetime import datetime

import click
import mlcroissant as mlc
from mlcroissant import Person

Json = dict[str, any]

# List of fields that can be "directly" converted using mlcroissant
CONVERTABLE_FIELDS = [
    "name",
    "description",
    "url",
    "keywords",
    "creator",
    "citation",
    "license",
    "distribution",
]

# These fields are added by mlcrossiant, so these must be removed from the original data
REMOVE_FIELDS = ["@context", "@type", "@id"]


def try_get(jsonld: Json, field: str):
    """Tries to get a field from the given jsonld if it is exists. Returns None if it does not"""
    return jsonld[field] if field in jsonld else None


def create_croissant_metadata(jsonld: Json):
    """Converts the jsonld input to croissant compliant json."""
    distributions = []
    record_sets = []

    if "distribution" in jsonld:
        for distribution in jsonld["distribution"]:
            name = f"{distribution['@type']}_{distribution['encodingFormat']}"
            print(name)
            distributions.append(
                mlc.FileObject(
                    id=name,
                    name=name,
                    content_url=distribution["contentUrl"],
                    encoding_format="Binary",
                    sha256="main",
                )
            )

            # Not 100% sure how this works, but the examples show a mapping
            # between the distrubtions and record sets, and it needs to be here
            # for croissant completion
            record_sets.append(
                # RecordSets contains records in the dataset.
                mlc.RecordSet(
                    id=f"{name}1",
                    # Each record has one or many fields...
                    fields=[
                        # Fields can be extracted from the FileObjects/FileSets.
                        mlc.Field(
                            id=f"{name}/context",
                            name="context",
                            description="",
                            data_types=mlc.DataType.TEXT,
                            source=mlc.Source(
                                file_set=name,
                                # Extract the field from the column of a FileObject/FileSet:
                                extract=mlc.Extract(column="context"),
                            ),
                        ),
                    ],
                )
            )

    keywords = try_get(jsonld, "keywords")
    if keywords:
        keywords = keywords.split(",")

    creators = try_get(jsonld, "creator")
    if creators:
        creators = [
            Person(name=creator["name"], url=creator["@id"]) for creator in creators
        ]

    return mlc.Metadata(
        name=try_get(jsonld, "name"),
        description=try_get(jsonld, "description"),
        url=try_get(jsonld, "url"),
        keywords=keywords,
        creators=creators,
        cite_as=try_get(jsonld, "citation"),
        license=try_get(jsonld, "license"),
        distribution=distributions,
        record_sets=record_sets
    )


@click.command()
@click.option("--file", help="The Schema.org JSON-LD to convert to croissant")
@click.option("--output", default="output.json", help="The ouput filename.")
def convert(file: str, output: str):
    """Converts the given JSON LD file into a croissant compliant JSON."""

    with open(file, "r", encoding="UTF-8") as f:
        data = f.read()
        data: dict[str, any] = json.loads(data)

    # mlcroissant will automatically add certain fields, so to avoid duplication these are removed first
    for key in REMOVE_FIELDS:
        if key in data:
            del data[key]

    # Non-Standard croissant fields are extracted so they can be added afterwards
    cannot_directly_convert = {}
    delete_keys = []
    for key, var in data.items():
        if key not in CONVERTABLE_FIELDS:
            cannot_directly_convert[key] = var
            delete_keys.append(key)

    for key in delete_keys:
        del data[key]

    # Create cro
    croissant_metadata = create_croissant_metadata(data)
    croissant = croissant_metadata.to_json()

    # Add the non-metadata fields back into the croissant json
    croissant.update(cannot_directly_convert)

    # Currently uploading the croissant to the validator causes a "datetime object is not JSON serialisable" error if
    # this field is present, so it must be removed. The "json.dumps" still works with this present though interestingly.
    del croissant["datePublished"]

    croissant = json.dumps(croissant, indent=2)

    with open(output, "w") as f:
        print(croissant)
        f.write(f"{croissant}\n")


if __name__ == "__main__":
    convert()
