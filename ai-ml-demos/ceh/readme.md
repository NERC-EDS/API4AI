# UKCEH Croissant Examples:

## Making Data in the EIDC accessible via Croissant
[The Environmental Information Data Centre (EIDC)](https://eidc.ac.uk/) is part of the Natural Environment Research Council's (NERC) Environmental Data Service and is hosted by the UK Centre for Ecology & Hydrology (UKCEH), managing nationally-important datasets concerned with the terrestrial and freshwater sciences. 

A Croissant API has been developed for each dataset in the EIDC, for example: [Croissant API: Bare sand, wind speed, aspect and slope at four English and Welsh coastal sand dunes, 2014-2016](https://catalogue.ceh.ac.uk/documents/972599af-0cc3-4e0e-a4dc-2fab7a6dfc85?format=croissant). 

Currently some manual editing is required to incorporate information about the recordSet for the data. A selection of these manually adjusted croissant files are available here:
- [Adjusted croissant file: Bare sand, wind speed, aspect and slope at four English and Welsh coastal sand dunes, 2014-2016](/croissant-examples/ukceh/croissantSpikeZip.json)
- [Adjusted croissant file: Daily and sub-daily hydrometeorological and soil data (2013-2023) [COSMOS-UK]](/croissant-examples/ukceh/croissantSpikeCOSMOS.json)
- [Adjusted croissant file: Climate hydrology and ecology research support system meteorology dataset for Great Britain (1961-2019) [CHESS-met]](/croissant-examples/ukceh/croissantSpikeChess.json)

## Notebooks demonstrating ML workflow with Croissant
To following notebook demonstrates loading data from a croissant file and putting it through an ML pipeline: [UKCEH ML-Croissant Pipeline ](/ai-ml-demos/ceh/ml_workflow_ukceh.ipynb). The purpose of the notebook is to highlight the ease of access to the data and underlying metadata, then the ease of implementing the data directly in an ML pipeline. The focus is not on the science or the particular statistical model.
