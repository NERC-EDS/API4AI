# NOC ML Time-series data example

The "example_timeseries_predictor.ipynb" notebook here loads a croissant file and trains a simple machine learning model using the darts library to forecast unseen bottom pressure recorder data, from the British Oceanographic Data Centre (BODC). This is purely intended to be a proof of concept, to demonstrate that data can be obtained via a croissant file, and then used to train a machine learning model.

## Contents
- `example_timeseries_predictor.ipynb` - Jupyter notebook containing the outline for obtaining the data and training a simple machine learning model on the data. The code should just run out of the box without the need for user intervention. Users without a GPU may find that the model training step takes some time.
- `requirements.txt` - The packages needed to run the notebook (I used a virtual environment: conda will probably work fine).
- `shelfbpr_bodc.json` - The croissant file containing metadata and the means to obtain the data used here.

## Notebook usage
Use the `requirements.txt` file to install the packages needed if necessary. The notebook should just run out the box. You may wish to play around with the number of epochs if you have a GPU and the time.

## Data
The description of the data set below is taken from the [BODC website](https://www.bodc.ac.uk/resources/inventories/edmed/report/155/).

> The data set comprises time series measurements from offshore pressure gauges mounted on the sea floor. The data holdings are approximately 250 observation months from 100 sites. The data have mainly been collected in the continental shelf seas around the British Isles. Data records contain date/time, total pressure and, occasionally, temperature. The sampling interval is typically 15 minutes or hourly, over deployment periods ranging from 1 to 6 months. Data were collected mainly by the Proudman Oceanographic Laboratory (POL), now the National Oceanography Centre (NOC) at Liverpool, and are managed by the British Oceanographic Data Centre (BODC).

There are multiple variables in the files provided: for this use case we only cared about [PPSCZZ01](https://vocab.nerc.ac.uk/collection/P01/current/PPSCZZ01/) data to keep the input data to the model consistent.

# NOC ML image data example:

The "crab_ml_example.ipynb" notebook shows an example workflow for working with image data. It uses a pre-trained model, a [modified version of the phytoClassUCSC classifier](https://huggingface.co/NOCAIR/phyto_class_ucsc_updated). This is just a test project, and has not been validated for bias issues.

## Exposing plankton data via CRAB
The [Centralised Repository for Annotations and BLOBs](https://crab.noc.ac.uk/) is a new project aiming to provide the capability for rapid prototyping of machine learning models utilising image data. It is still in development at time of writing, so the notebook may break, as it relies on a connection to this service.

## Notebook demonstrating ML workflow with Croissant
The [notebook](./crab_ml_example.ipynb) shared here is simply a demonstration of how Croissant files can be used to programmatically access NOC's image data via CRAB. The classifier is not optimised for the dataset, and is based on an old version of [phytoClassUCSC](https://huggingface.co/patcdaniel/phytoClassUCSC) that has been modified to run on modern TensorFlow versions.

