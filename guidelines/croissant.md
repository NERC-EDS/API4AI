# CroissantML 

## Introduction  

The [Croissant](https://docs.mlcommons.org/croissant/docs/croissant-spec.html)  metadata format has gathered significant support within the machine learning (ML) community since its introduction.  Croissant is designed to standardise the description of machine learning (ML) datasets, enhancing their discoverability, usability, and interoperability across various platforms and tools. Developed collaboratively by industry and academia under the MLCommons initiative, Croissant builds upon the [Schema.org](https://schema.org/) vocabulary to provide a comprehensive framework for dataset documentation.

> [Schema.org](https://schema.org/) is a standardised vocabulary for describing structured data on the web. In Croissant, it is used to define dataset metadata, ensuring interoperability with web-based dataset search engines like Google Dataset Search.

Croissant metadata is encoded in [JSON-LD](https://json-ld.org/).

> [JSON-LD](https://json-ld.org/) (JavaScript Object Notation for Linked Data) is a lightweight format for representing linked data using JSON. It is used in Croissant to encode metadata in a structured, machine-readable way, allowing datasets to be easily discovered and integrated across platforms.

**Where can you find Croissant datasets:**
 
- [OpenML](https://openml.org/search?type=data&status=active)
- [Hugging Face](https://huggingface.co/datasets)
- [Kaggle](https://www.kaggle.com/datasets)
- [Dataset Search (google)](https://datasetsearch.research.google.com/)

### Responsible AI (RAI)

Croissant supports **Responsible AI (RAI)** by providing a machine-readable framework for documenting ML datasets, making solutions like Data Cards easier to publish, share, and reuse.  Designed to be modular and extensible, Croissant includes an RAI vocabulary covering data lifecycle, labeling, AI safety, fairness, compliance, and inclusion. The community is encouraged to extend it for specific data types and domains, ensuring broader applicability across various AI fields.

### Discoverability 

Croissant enhances dataset discoverability by providing a machine-readable metadata schema based on [JSON-LD](https://json-ld.org/) and  [schema.org](https://schema.org/). This allows datasets to be indexed by search engines, making them easier to find, share, and integrate into ML workflows. By standardising metadata descriptions, Croissant ensures datasets are more accessible and reusable across different platforms.

> Embedding Croissant JSON-LD  within HTML can significantly enhance discoverability by providing structured data that search engines can easily parse and understand.

### Portability 

Croissant improves dataset portability by defining a structured, format-agnostic way to describe datasets, enabling seamless use across different tools and environments. It supports multiple file formats, storage locations, and ML frameworks, ensuring datasets can be easily transferred and used in diverse computing setups.

### Reproducibility

Croissant promotes reproducibility by documenting dataset provenance, transformations, and dependencies in a structured manner. By capturing how data was generated, processed, and formatted, it ensures that experiments and ML models can be reliably recreated, reducing inconsistencies and improving transparency in AI research.

## Core Concepts

Below is a summary of the core concepts that constitute a Croissant specification file. For simplicity, more advanced concepts have been excluded and complex relationships between these  concepts can be created. The best places to learn more about Croissant specification is:
- [Croissant Format Specification](https://docs.mlcommons.org/croissant/docs/croissant-spec.html)
- [CroissantML on GitHub](https://github.com/mlcommons/croissant)
- [CroissantML example datasets on GitHub](https://github.com/mlcommons/croissant/tree/main/datasets)

### Dataset
A **dataset** is a structured collection of data that can be used for machine learning, analysis, or research. It consists of multiple records organised in a meaningful way, often accompanied by metadata that describes its structure, sources, and intended use.

### Croissant Dataset
A **Croissant dataset** is a **dataset** described using the Croissant ML specification, which provides a standardised, machine-readable format for defining dataset metadata, structure, and relationships. This enables better discoverability, sharing, and integration with ML frameworks.

### Distribution
A **distribution** refers to the way a **dataset** can be accessed or retrieved. It includes information on file formats, URLs, and encoding methods, allowing users to download or stream data in a structured manner.

### FileObject
A **FileObject** is a reference to an individual file within a **dataset**. It provides metadata about the file, such as its format, size, and location, enabling structured access and integration into ML workflows.

### FileSet
A **FileSet** is a collection of multiple **FileObjects** within a **dataset**. It groups related files together, allowing for more efficient dataset organisation and handling, especially for datasets containing multiple data sources or modalities (e.g., images, text, and annotations).

### RecordSet
A RecordSet represents a structured set of records (rows) within a **dataset**. It defines how individual instances of data are stored and organised, specifying attributes such as field names, data types, and relationships between records.

### Field
A **Field** in a **RecordSet** represents a single attribute or column within the structured data. Each **Field** defines the name, data type, format, etc. Additionally, a **Field** can reference a **DataSource**, specifying where its data originates and how it should be extracted or transformed.

### DataSource
A **DataSource** specifies where a **Field** within a **RecordSet** gets its data, including how it should be extracted, transformed, or formatted. Typically it will be a structured file (e.g., CSV, JSON).

### Live versus Static Datasets
Each **FileObject** in a Croissant file can provide a checksum using either the `md5` or `sha256` property, which is a hash of the file's content. For versioned (static) datasets, recording these checksums is recommended to ensure the integrity of downloaded files. **Live datasets**, which evolve continuously, should have the `isLiveDataset` property set to `True`. Checksums should not be specified for **FileObject**s that are expected to change over time.

### Example Croissant

Below is a simple example of a Croissant specification the BGS magnetogram images, it has a **distribution** made up of a single **FileObject** with a content URL for API call that returns a CSV file. There is a corresponding **RecordSet** that defines Field that match those in the source **FileObject** i.e. the CSV file.

``` json
{
  "@context": {
    "@language": "en",
    "@vocab": "https://schema.org/",
    "citeAs": "cr:citeAs",
    "column": "cr:column",
    "conformsTo": "dct:conformsTo",
    "cr": "http://mlcommons.org/croissant/",
	  "rai": "http://mlcommons.org/croissant/RAI/",
    "data": {
      "@id": "cr:data",
      "@type": "@json"
    },
    "dataType": {
      "@id": "cr:dataType",
      "@type": "@vocab"
    },
    "dct": "http://purl.org/dc/terms/",
    "examples": {
      "@id": "cr:examples",
      "@type": "@json"
    },
    "extract": "cr:extract",
    "field": "cr:field",
    "fileProperty": "cr:fileProperty",
    "fileObject": "cr:fileObject",
    "fileSet": "cr:fileSet",
    "format": "cr:format",
    "includes": "cr:includes",
    "isLiveDataset": "cr:isLiveDataset",
    "jsonPath": "cr:jsonPath",
    "key": "cr:key",
    "md5": "cr:md5",
    "parentField": "cr:parentField",
    "path": "cr:path",
    "recordSet": "cr:recordSet",
    "references": "cr:references",
    "regex": "cr:regex",
    "repeated": "cr:repeated",
    "replace": "cr:replace",
    "sc": "https://schema.org/",
    "separator": "cr:separator",
    "source": "cr:source",
    "subField": "cr:subField",
    "transform": "cr:transform"
  },
  "isLiveDataset" : "true",
  "@type": "sc:Dataset",
  "citeAs": "British Geological Survey. (2013). UK Magnetic Observatory Magnetograms. British Geological Survey. (Dataset). https://doi.org/10.5285/4eeec93c-12e6-4244-9b99-52c61350f9aa",
  "version": "1.2.3",
  "name": "bgs-historical-magnetograms-images",
  "description": "Scanned images of about 250 000 historical magnetograms on photographic paper — original recordings of the variations in the strength and direction of the Earth’s magnetic field",
  "conformsTo": "http://mlcommons.org/croissant/1.0",
  "license": "https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/",
  "url": "https://www.bgs.ac.uk/information-hub/scanned-records/magnetograms/",
  "creator" : [
             {"@type": "Organization",
             "name": "British Geological Survey"}],
  "datePublished" : "2013-01-01",
  "distribution": [
    {
      "@type": "cr:FileObject",
      "@id": "api-image-csv-1",
      "name": "api-image-csv-1",
      "contentUrl": "https://ogcapi.bgs.ac.uk/collections/magnetograms/magnetograms/items?f=csv&limit=100000&properties=component_code,start_date_year,end_date_year,observatory_code,front_filename,rear_filename",
      "encodingFormat": "text/csv"
	     
      
    }
  ],
 "recordSet": [
    {
      "@type": "cr:RecordSet",
      "@id": "thin-section-images",
      "name": "thin-section-images",
	    "key": { "@id": "gsr/gsr_id" },
      "description": "Index of thin section images with descriptive labels and urls to the image file",
      "field": [
		{
			"@type": "cr:Field",
			"@id": "bgs-magnetograms/observatory_code",
			"name": "bgs-magnetograms/observatory_code",
			"description": "A three digit IAGA code used to identify the observatory that the magnetogram was recorded at.",
			"dataType": "sc:Text",
			"source": {
			  "fileObject": {
				"@id": "api-image-csv-1"
			  },
			  "extract": {
				"column": "observatory_code"
			  }
			}
		  },
		  {
			"@type": "cr:Field",
			"@id": "bgs-magnetograms/component_code",
			"name": "bgs-magnetograms/component_code",
			"description": "The code(s) of the magnetic components that were recorded.",
			"dataType": "sc:Text",
			"source": {
			  "fileObject": {
				"@id": "api-image-csv-1"
			  },
			  "extract": {
				"column": "component_code"
			  }
			}
		  },
		  {
			"@type": "cr:Field",
			"@id": "bgs-magnetograms/front_filename",
			"name": "bgs-magnetograms/front_filename",
			"description": "The filename of the front scan of the magnetogram",
			"dataType": "sc:Text",
			"source": {
			  "fileObject": {
				"@id": "api-image-csv-1"
			  },
			  "extract": {
				"column": "front_filename"
			  }
			}
		  },
		  {
			"@type": "cr:Field",
			"@id": "bgs-magnetograms/rear_filename",
			"name": "bgs-magnetograms/rear_filename",
			"description": "The filename of the rear scan of the magnetogram",
			"dataType": "sc:Text",
			"source": {
			  "fileObject": {
				"@id": "api-image-csv-1"
			  },
			  "extract": {
				"column": "rear_filename"
			  }
			}
		  },
		  {
			"@type": "cr:Field",
			"@id": "bgs-magnetograms/start_date_year",
			"name": "bgs-magnetograms/start_date_year",
			"description": "The start date of this magnetogram,  in format YYYY .",
			"dataType": "sc:Integer",
			"source": {
			  "fileObject": {
				"@id": "api-image-csv-1"
			  },
			  "extract": {
				"column": "start_date_year"
			  }
			}
		  },
		  {
			"@type": "cr:Field",
			"@id": "bgs-magnetograms/end_date_year",
			"name": "bgs-magnetograms/end_date_year",
			"description": "The end date of this magnetogram,  in format YYYY.",
			"dataType": "sc:Integer",
			"source": {
			  "fileObject": {
				"@id": "api-image-csv-1"
			  },
			  "extract": {
				"column": "end_date_year"
			  }
			}
		  }
		]
    }
  ]
}

```

## Creating a Croissant Specification


There are a few options for creating a Croissant specification:

### By Hand
You can manually create a Croissant specification by writing the necessary metadata in [JSON-LD](https://json-ld.org/) format. This method gives you full control over the details but can be time-consuming.

### Python Library: mlcroissant
The [mlcroissant library](https://github.com/mlcommons/croissant/tree/main/python) simplifies the process of creating and managing compliant Croissant specifications. It provides tools and functions to generate the required metadata programmatically, making it easier to integrate into your workflows.

**Example Python code:**

``` python
import mlcroissant as mlc
import json

print("mlcroissant")

distribution = [ 
    mlc.FileObject(
        id="api-image-csv-1",
        name="api-image-csv-1", 
        content_url="https://ogcapi.bgs.ac.uk/collections/magnetograms/magnetograms/items?f=csv&limit=100000&properties=component_code,start_date_year,end_date_year,observatory_code,front_filename,rear_filename",
        encoding_format="text/csv",
        md5="TBD",
    )
] 

fieldColNameAndType = {
    "observatory_code":mlc.DataType.TEXT,
    "component_code":mlc.DataType.TEXT,
    "front_filename":mlc.DataType.TEXT,
    "rear_filename": mlc.DataType.TEXT ,
    "start_date_year":mlc.DataType.INTEGER,
    "end_date_year":mlc.DataType.INTEGER
}

fields = []

# Fields are often repetitive 
for col, type in fieldColNameAndType.items():
    fields.append(mlc.Field(id=col + "-id", name=col, description=col + " column", data_types=type, source=mlc.Source(file_object="api-image-csv-1", extract=mlc.Extract(column=col)),))

record_sets = [
    # RecordSets contains records in the dataset.
    mlc.RecordSet(
        fields=fields,
        id="magnetogram-images",
        name="magnetogram-images",
    )
]

ctx = mlc.Context(
    is_live_dataset=True
)

# Metadata contains information about the dataset.
metadata = mlc.Metadata(
    ctx=ctx,
    name="bgs-historical-magnetograms-images", 
    description=(
        "Scanned images of about 250 000 historical magnetograms on photographic paper — original recordings of the variations in the strength and direction of the Earth’s magnetic field"
    ),
    cite_as=(
        "British Geological Survey. (2013). UK Magnetic Observatory Magnetograms. British Geological Survey. (Dataset). https://doi.org/10.5285/4eeec93c-12e6-4244-9b99-52c61350f9aa"
    ),

    url="https://www.bgs.ac.uk/information-hub/scanned-records/magnetograms/",
    license="https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/",  # FOR EXAMPLE
    distribution=distribution,
    record_sets=record_sets, 
    version="1.2.3",

)

JSONLD = metadata.to_json()   

pretty_json = json.dumps(JSONLD, indent=4)

print(pretty_json)
```


### Croissant Editor on Hugging Face
The [visual editor](https://huggingface.co/spaces/MLCommons/croissant-editor) available on Hugging Face allows you to create and edit Croissant specifications through an intuitive interface. This option is user-friendly and ideal for those who prefer a graphical approach. However, it may have limited customisation options compared to manual creation. It is also dependent on huggingface developers to maintain the tool in line with updates to the croissant specification (at the time of writing the editor appeared to be built to a previous version of the specification rather than the latest version).
 
## Consuming a Croissant Specification

### Collaborative Platforms
 
Croissant specifications can be consumed on various online platforms, making it easier to integrate and utilise machine learning datasets. 
- On [Google Colab](https://colab.research.google.com/), you can use the **mlcroissant** Python library to read and manage Croissant specifications within an interactive environment, perfect for experimentation and collaboration. 
- [Hugging Face](https://huggingface.co/docs/hub/spaces) supports Croissant specifications, allowing you to explore and utilise datasets through their intuitive interface and strong community support. 
- [OpenML](https://openml.org/search?type=flow&sort=runs) provides a collaborative platform where you can share and explore machine learning datasets annotated with Croissant specifications.
- [Kaggle](https://www.kaggle.com/code) also supports Croissant specifications, offering a vast repository of datasets and integration with Jupyter notebooks, making it a valuable resource for data scientists and researchers. 

### mlcroissant Python Library

Using the [mlcroissant library](https://github.com/mlcommons/croissant/tree/main/python) to consume Croissant specifications and referenced data offers a versatile approach for both conventional Python development environments and integrated Python notebooks. 

The library provides robust functions to read, manage, and utilise Croissant specifications, making it easier to incorporate structured metadata into your machine learning workflows. 

When integrated into Python notebooks, such as [Jupyter](https://jupyter.org/) or [Google Colab](https://colab.research.google.com/), mlcroissant allows for interactive data exploration and manipulation, enhancing collaboration and experimentation.

**Example Python code:**
``` python
# A very simple example that shows how to:
# a) read a Croissant specification.
# b) access information on the first RecordSet.
# c) iterate over Records in the RecordSet.
# d) access Field infomation within Records.
ds = mlc.Dataset("TODO/put/filepath/here.json")  # <------- CHANGE THIS

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
        print("\t\t value", record.get(field.id))

    if r >= 3:  # just the first 3 rows (records) to illustrate data
        print("break")
        break
```

## API4AI Findings 

### Automation & Integration

Programmatically generating Croissant specifications (i.e. using the mlcroissant library) offers significant benefits in terms of **automation and integration**. 

By using libraries (such as mlcroissant), you can automate the creation, verification and consumption of Croissant specifications, ensuring that they are always up-to-date. 

> For example, an API serving data referenced in a Croissant specification, can dynamically generate and serve Croissant specifications at runtime based on available metadata. This approach eliminates the need for manual editing or updating when the data changes, reducing the risk of errors and saving valuable time.  

### Bulk versus Dynamic Dataset Access

Croissant is primarily designed for describing static datasets that are available for bulk download, rather than those delivered dynamically via parameterised API queries. Croissant's intention is to provides metadata about entire datasets (structure, source, and formats), ensuring datasets can be easily discovered, shared, and loaded into ML pipelines.

- Croissant supports datasets stored in local files, cloud storage (GCS, S3), HTTP endpoints, and repositories (Kaggle, Hugging Face, OpenML), making it ideal for datasets that can be downloaded in full. 
- Many typical ML workflows require access to entire datasets upfront, rather than fetching data dynamically through API queries.

#### Workaround for lack of parameterised API support

Our intention was to provide dynamic dataset access to datasets via a **pygeoapi** instance, which provides a rapid no-code way of exposing a database table as a web API that is also compliant with OGC API family of standards. Our initial plan would have meant individual **OGC Records** would be delivered via the _items_ endpoint: _`{apiroot}/collections/{collectionId}/items/{itemId}/`_. However, this approach was difficult to support in Croissant for a long and dynamic list of {itemId} as each url would have to be listed. As a workaround, we used [CQL](https://docs.pygeoapi.io/en/latest/cql.html) to define a single endpoint/query (per **FileObject**) that would represent all the items in the dataset.

Retrieving the entire dataset this way posed challenges related to size and processing time. Executing a query for the full dataset could lead to timeouts, as generating and transmitting a large response payload would be computationally expensive. To address this, we subset the data in the query, either by limiting the quantity or filtering based on specific attributes.

For example, when using _paging_ to subset a dataset into multiple **FileObjects**, we were able to combine multiple **FileObjects** into a single **FileSet**. However, it was not immediately clear how to define an appropriate **RecordSet** that would allow access to the columns in the CSV data from all of the FileObjects that made up the **FileSet**, even though each CSV file had the same structure.


#### Workaround for lack of pygeoapi customisation

_In this case, the issue lies with pygeoapi, not Croissant......_

As mentioned above, the initial idea was to have an OGC API hosted by a **pygeoapi** instance. This API would serve a Croissant specification from a dedicated endpoint, leveraging pygeoapi’s JSON-LD support, while also providing access to the data referenced in the Croissant specification.

However, due to limitations in the customisation options available within **pygeoapi**, adding an additional endpoint was not feasible (at least not without subverting existing plugin support). As a workaround, an additional **OGC link** (which is supported by pygeoapi’s configuration) was added which would link to a Croissant specification hosted elsewhere. This Croissant specification, in turn, referenced data served by **pygeoapi** via a CQL endpoint/query.

While not ideal, this approach at least demonstrates how Croissant can be used alongside OGC APIs. If these APIs were designed to  support Croissant specification endpoints (as they do for **openapi** specification endpoints which deliver very similar information), they could serve as self-contained sources for both ML metadata and data delivery.  

### RecordSets and Data Sources 

- A **FileObject** represents a single, individual file. It contains the file's location (e.g., URL, local path) and metadata, such as its format and size.
- A **FileSet** is a collection of multiple files that logically belong together (e.g., a ZIP file or another type of archive).
- A **RecordSet** references either a FileSet or a FileObject as its data source. The **RecordSet** defines how the data within these files should be interpreted and structured.

From our experience, when a **FileObject** serves as the data **source** for a **RecordSet**, it is possible to further decompose the file into **Fields** derived from it's internal structure:
  - JSON files can be decomposed using _JSONPath_.
  - CSV files can be decomposed using _column_ names.

However, it does not appear to be possible to do the same when a **RecordSet** has a **FileSet** (containing JSON or CSV files) as the data **source**.

Instead, when decomposing a **FileSet**, properties related to the files themselves (rather than their internal structure) are accessible as **Fields**, for example the **filename** of each file in the **FileSet**.

**Our inference:**
- The most granular information a **Field** refers to, when a **FileSet** is the **source**, is the files themselves.
-	The most granular information a **Field** refers to, when a **FileObject** is the **source**, is: 
    - JSONPath for JSON files
    -	Column names for CSV files
    - Or, the file itself (singular).


 It remains unclear whether this difference in behaviour between **FileSets** and **FileObjects** is an intentional design choice, a limitation of the CroissantML library, or a misunderstanding of the intended use of **FileSets** and **FileObjects**.

### Support & Complexity 

Croissant is still a very new standard, but it has already gained widespread support from major platforms and organisations.

However, due to its newness, there is still limited technical information, documentation, and mature tooling available, making it challenging to learn its full capabilities, especially when working with more complex aspects of the specification, such as data transformations, advanced referencing, joins, etc. 

As Croissant evolves, better tooling, more real-world case studies, and expanded community contributions will be essential to unlocking its full potential and making it easier to implement at scale. Croissant's success will depend on continued community engagement, tool support, and real-world adoption in ML research and industry.  
 
### Authentication and Python Library: mlcroissant 

The **mlcroissant** library currently supports data retrieval (contentUrls) only from unauthenticated endpoints, or endpoints that use **basic authentication**. 

Basic authentication for data retrieval (contentUrls) is supported, this support is via environment variables: 

```
"CROISSANT_BASIC_AUTH_USERNAME" = USERNAME
"CROISSANT_BASIC_AUTH_PASSWORD" = PASSWORD
```

- Croissant specifications hosted on endpoints requiring any form of authentication are not supported. 
- Additionally, data retrieval is limited to **basic authentication**, meaning endpoints requiring more advanced authentication methods are not accessible.

While the library allows loading metadata and datasets from various sources, including HTTP, cloud storage, and local files, its support for accessing protected resources remains limited. If not resolved this limitation could impact adoption for datasets hosted on private servers, restricted cloud storage, or enterprise data platforms. Hopefully, future updates would improve support for authentication.
 
### Alternatives to Croissant

#### GeoCroissant (proposed)
The proposed [GeoCroissant](https://www.youtube.com/watch?v=DPA14-6Vssg) specification extends the Croissant dataset description format to better suit geospatial machine learning. Croissant lacks crucial geospatial features, GeoCroissant will address these gaps by incorporating spatial references, supporting complex data structures (like NetCDF4), ensuring interoperability with existing geospatial data formats, and managing geographical biases and restricted data access. 

#### Schema\.org/Dataset
[Schema.org](https://schema.org/)  provides a metadata vocabulary widely used for describing [datasets](https://schema.org/Dataset) on the web. It enables datasets to be indexed and discovered by search engines like Google Dataset Search. While it supports structured metadata in JSON-LD, it is not ML-specific and lacks features for tracking dataset transformations, relationships, and lineage, which are crucial for ML workflows. Croissant re-uses schema.org elements where it can, and extends it where necessary.

#### Data Cards (Google Research)
[Data Cards](https://sites.research.google/datacardsplaybook/) are structured, human-readable dataset documentation templates designed to enhance transparency and responsible AI practices. They provide insights into dataset properties, provenance,motivations & intentions, and intended use cases. However, they are not machine-readable and do not support automated metadata extraction or dataset discoverability through search engines.

#### Datasheets for Datasets (Microsoft Research)
[Datasheets for Datasets](https://www.microsoft.com/en-us/research/publication/datasheets-for-datasets/) adopt a questionnaire-style approach to document dataset characteristics. It covers dataset creation, potential biases, and ethical considerations. While valuable for AI governance, they lack machine-readable representations and are not optimised for automated dataset discovery or ML workflow integration.

#### Frictionless Data (Open Knowledge Foundation)
[Frictionless Data](https://okfnlabs.org/projects/frictionless-data/) / [frictionlessdata.io](https://frictionlessdata.io/introduction/#frictionless-standards) provides a JSON-based metadata format called [Data Package](https://datapackage.org/), which standardises dataset structure, schema validation, and provenance tracking. It is designed for general-purpose datasets, making it useful in open data and research but lacks deep ML-specific capabilities, such as defining dataset joins, transformations, and model reproducibility.

#### DCAT (Data Catalog Vocabulary - W3C)
[DCAT](https://www.w3.org/TR/vocab-dcat-3/) is a W3C standard for describing datasets & services in linked data formats like RDF and JSON-LD. It is widely used in government and open data portals for structured dataset cataloging. However, it is not optimized for ML-specific metadata, making it less suitable for tracking model training datasets, transformations, or ML workflows. [Alignments exist](https://www.w3.org/TR/vocab-dcat-3/#dcat-sdo) between DCAT and schema.org.

#### ML Metadata (MLMD - TensorFlow)
[ML Metadata (MLMD)](https://www.tensorflow.org/tfx/guide/mlmd) is a metadata tracking system developed for ML pipelines. It captures dataset lineage, transformations, and model versioning, ensuring reproducibility in machine learning experiments. While useful for understanding and analysing all the interconnected parts of your ML pipeline, it is not designed for dataset publishing or discoverability, making it less useful for dataset sharing across different ML ecosystems.

#### Training Data Markup Language for AI
The [TrainingDML-AI](https://www.ogc.org/publications/standard/trainingdml-ai), developed by the OGC, is a standard to address the need for a consistent way to represent and exchange geospatial training data. It is particularly focused on machine learning models that process Earth Observation data. By providing a structured framework, TrainingDML-AI enables different AI systems to understand and use the same training data and improve interoperability. 

### Extensions to Croissant

#### GeoCroissant (proposed)
The proposed [GeoCroissant](https://www.youtube.com/watch?v=DPA14-6Vssg) specification extends the Croissant dataset description format to better suit geospatial machine learning. Croissant lacks crucial geospatial features, GeoCroissant will address these gaps by incorporating spatial references, supporting complex data structures (like NetCDF4), ensuring interoperability with existing geospatial data formats, and managing geographical biases and restricted data access. 


--- 

Links: 

- [Croissant Format Specification](https://docs.mlcommons.org/croissant/docs/croissant-spec.html)
- [Croissant ML Commons](https://mlcommons.org/working-groups/data/croissant/)
- [CroissantML on GitHub](https://github.com/mlcommons/croissant)
- [CroissantML example datasets on GitHub](https://github.com/mlcommons/croissant/tree/main/datasets)
- [mlcroissant library on GitHub](https://github.com/mlcommons/croissant/tree/main/python)
- [visual editor on huggingface](https://huggingface.co/spaces/MLCommons/croissant-editor)
- [Croissant: a metadata format for ML-ready datasets](https://research.google/blog/croissant-a-metadata-format-for-ml-ready-datasets/)
- [JSON-LD](https://json-ld.org/)
- [Schema.org](https://schema.org/)
- [CQL](https://docs.pygeoapi.io/en/latest/cql.html) 
- [Schema.org/datasets](https://schema.org/Dataset) 
- [Google Data Cards](https://sites.research.google/datacardsplaybook/) 
- [Datasheets for Datasets](https://www.microsoft.com/en-us/research/publication/datasheets-for-datasets/) ([2021 paper](https://arxiv.org/pdf/1803.09010))
- [Frictionless Data](https://okfnlabs.org/projects/frictionless-data/) / [frictionlessdata.io](https://frictionlessdata.io/introduction/#frictionless-standards) / [Data Package](https://datapackage.org/)
- [DCAT](https://www.w3.org/TR/vocab-dcat-3/)
- [ML Metadata (MLMD)](https://www.tensorflow.org/tfx/guide/mlmd) 
- [TrainingDML-AI](https://www.ogc.org/publications/standard/trainingdml-ai)
- [GeoCroissant](https://www.youtube.com/watch?v=DPA14-6Vssg)