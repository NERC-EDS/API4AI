# CONTENTS

A theoretical croissant JSON-LD file describing data about rock samples and images that is delivered via API

Only the mandatory attributes of croissant format are included

Multiple (theoretical) distributions are described:

 - csv file that is versioned and checksumed 
 - parquet file that is versioned and checksumed
 - dynamic csv download using API requests
   - this consists of 2 requests of 100k items each - the dataset size is between 150k and 200k
   
A subset of the available fields within the dataset is specified in the recordset.field array

# NOT ADDRESSED:
 - linking dataset to separate enum datasets containing the distinct dictionary values
 - better modelling of the actual images as FileObject in their own right?
