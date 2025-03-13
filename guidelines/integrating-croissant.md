# Integrating CroissantML with APIs and Webpages   

## Introduction
 
[Croissant](./croissant.md) is a standardised way to describe machine learning datasets. It's built for downloading entire datasets at once, instead of repeated querying an API. By adding CroissantML to your web API, you make your datasets easier to find, understand, and download, which improves integration AI/ML workflows. 

This guide outlines recommended approaches for exposing CroissantML metadata through web APIs and webpages. It does not cover [authoring Croissant](./croissant.md) specifications only their integration into APIs and Webpages.

## Integration Principles
 
When integrating CroissantML metadata into a web APIs and webpages, it’s essential to focus on the following principles:

- **Follow Open Standards:** Ensure that the metadata is structured using open, widely-adopted standards such as JSON-LD, enabling easy integration with other systems.
- **Bulk Data Access:** CroissantML is meant for bulk data downloads, so APIs should be designed to handle large datasets efficiently rather than focusing on frequent, parameterised access.
- **Interoperability:** The metadata should be easily discoverable and usable across different geospatial and AI workflows, making it compatible with existing standards like OGC and Schema\.org. 

### Serving CroissantML Specifications

#### Dedicated CroissantML Endpoint
A dedicated CroissantML endpoint is a specific URL in your API:

e.g. `/<endpoint-path>/croissant`

That directly serves metadata describing available datasets in **CroissantML** format. This endpoint should return all relevant dataset information in the structured, machine-readable JSON-LD format. The metadata should include key details such as dataset names, descriptions, download links, and other related attributes. 

This approach offers a single, convenient access point for discovering datasets, retrieving data, and facilitating integration into AI/ML workflows, streamlining the process for users.

**Example OpenAPI specification**
``` yaml
openapi: 3.0.3
info:
  title: Geospatial API with CroissantML Support
  description: API for serving CroissantML metadata for bulk dataset access.
  version: 1.0.0
paths:
  /<endpoint-path>/croissant:
    get:
      summary: Retrieve CroissantML Metadata
      description: Returns CroissantML metadata in JSON-LD format.
      operationId: getCroissantMetadata
      tags:
        - Metadata
      responses:
        "200":
          description: CroissantML metadata in JSON-LD format
          content:
            application/ld+json:
              schema:
                type: object     # see other page for croissant details
        "404":
          description: Metadata not found
        "500":
          description: Internal server error
```

### Linking to CroissantML Specifications

If adding a new endpoint is not feasible, the CroissantML specification can be hosted elsewhere and linked to. For APIs adhering to OGC standards, links are managed through OGC _Link Objects_. These links can be added at various levels within the OGC API, with the **collection** level (probably) being the most appropriate for this case. This method ensures compatibility with geospatial standards while enabling the exposure of machine learning metadata.
 
**OGC link properties**
- **rel:** "describedBy" - Indicates that the linked document provides a description of the dataset.
- **type:** "application/ld+json" - Specifies JSON-LD as the metadata format.
- **title:** "CroissantML Metadata" - Provides a human-readable label.
- **href:** The URL where the CroissantML specification metadata can be accessed.

**Example OGC API (JSON)**

``` json
{
  "links": [
    {
      "rel": "describedBy",
      "type": "application/ld+json",
      "title": "CroissantML Metadata",
      "href": "https://<some-host>/<some-path>/croissant.json"
    }
  ]
}
```

**Example link configuration for pygeoapi**
``` yaml
resources:
      <name>:
           links:
                - type: application/ld+json
                  rel: describedby
                  title: croissant
                  href: https://<some-host>/<some-path>/croissant.json
                  hreflang: en-US
```

### Embedding CroissantML Specifications
 
To enhance the discoverability and searchability of your datasets, it’s recommended to embed Schema\.org metadata within any associated HTML webpages using JSON-LD. This allows search engines and other systems to easily index your datasets. 

When appropriate, you can embed CroissantML specifications within the HTML metadata to provide a clear connection between webpages and data available for machine learning workflows. 

**Example HTML with embedded CroissantML Specification**

``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Example Dataset</title>
    <script type="application/ld+json">
    {
  "@context": {
    "@language": "en",
    "@vocab": "https://schema.org/",
     … 
     … 
     … 
  },
  "isLiveDataset" : "true",
  "@type": "sc:Dataset",
    … 
    … 
    … 
  "distribution": [
    {
      "@type": "cr:FileObject",
      …  
      … 
      … 
    }
  ],
 "recordSet": [
    {
      "@type": "cr:RecordSet",
       … 
       … 
       … 
    }
  ]
}    </script>
</head>
<body>
    <h1>Example Dataset</h1>
    <p>This page contains metadata for an example dataset using CroissantML.</p>
</body>
</html>
```