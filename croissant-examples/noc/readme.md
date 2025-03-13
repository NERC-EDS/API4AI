# NOC Croissant Examples

## PDL To Croissant

The PDL (Published Data Library) is BODC's published data catalogue. For each dataset, Schema.org JSON-LD is already produced. This script takes the metadata in that JSON-LD and converts into a Croissant file.

Currently the distribution links in the Schema.org are not typically machine actionable, so manual editing of the Croissant file was needed to then feed this into notebooks/AI tools/etc.

To use:
- `pip install mlcroissant click`
- `python schemaorg_to_croissant.py --file schema_org.json --output croissant.json`

## GEBCO Croissant File

`gebco_2024.json` is a Croissant file produced from our PDL using the above script. The distribution/recordsets were then manually edited to point to a zip file containing a series of GeoTIFF images. A sample notebook for loading this dataset is provided, `gebco_croissant_demo.ipynb`.

# Example ML Workflow

`pdl_croissant_ai_demo.ipynb` takes the above Croissant file and runs it through a machine learning algorithm, performing k-mean clustering on the GEBCO GeoTiffs. While these results are, themselves, meaningless due to the nature of the data it provides a clear demonstration of what the process would look like.
