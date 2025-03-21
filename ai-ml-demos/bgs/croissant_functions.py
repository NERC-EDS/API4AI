import mlcroissant as mlc
import glob
import os
import requests
    
def clear_cache (directory):
        
    # Delete all files in the directory
    for file in glob.glob(os.path.join(directory, "*")):
        try:
            os.remove(file)
            print(f"Deleted: {file}")
        except IsADirectoryError:
            print(f"Skipping directory: {file}")
    
    print("CACHE CLEARED")
    
# ############################################################################


def is_image_url_valid(url):
    try:
        response = requests.get(url, stream=True)
        content_type = response.headers.get("Content-Type", "")

        # Check if the request was successful (status code 200) and it's an image
        if response.status_code == 200 and content_type.startswith("image/"):
            return True
        else:
            return False
    except requests.RequestException:
        return False
# ############################################################################


def per_recordset (ds, record_set):
    print("===============================================================")
    print("record set:", record_set.name  , "id:" , record_set.id)
    fields = record_set.fields
    for f, field in enumerate(fields):
        print("Field:", field, field.name, field.data_type, field.description)

    records: mlc.Records = ds.records(record_set=record_set.id)  # columns
    print("===============================================================")

    for r, record in enumerate(records):  # i.e. columns
        print("Record, index:",r)
        for f, field in enumerate(record_set.fields):
            print("Field:", field.id , "=" , record.get(field.id))  # field value is stored as bytes
            # see: C:\Data\Projects\EDS API4AI\python\make-croissant\venv\Lib\site-packages\mlcroissant\_src\operation_graph\operations\field.py LINE: ~113
            print("\t\tbytes converted to utf8:", record.get(field.id).decode('utf-8'))  # convert to utf8

            if ("-image-url-field-" in field.id):
                url = record.get(field.id).decode('utf-8')
                print("\t\ttest image url:", url, "VALID:", is_image_url_valid(url))

        print("---------------------------------")


def get_images_urls (ds, record_set):
    
    # Get field names:
    fields = record_set[0].fields
    records: mlc.Records = ds.records(record_set=record_set[0].id)  # columns

    # Create empty lists for image urls and names:
    ppl_urls = []; xpl_urls = []; sample_names = []

    for r, record in enumerate(records):
        for f, field in enumerate(record_set[0].fields):
            # print (field.id)
    
            if 'sample-name' in field.id:
                # print(record.get(field.id).decode('utf-8'))
                sample_names.append (record.get(field.id).decode('utf-8'))
    
            if ("ppl-image-url-" in field.id):
                ppl_url = record.get(field.id).decode('utf-8')
                if is_image_url_valid (ppl_url) == False:
                    print ('Image url NOT valid! -> ' + ppl_url)
                # print("\t\ttest image url:", ppl_url, "VALID:", is_image_url_valid (ppl_url))
                ppl_urls.append (ppl_url)
                
            if ("xpl-image-url-" in field.id):
                xpl_url = record.get(field.id).decode('utf-8')
                # print("\t\ttest image url:", xpl_url, "VALID:", is_image_url_valid (xpl_url))
                if is_image_url_valid (xpl_url) == False:
                    print ('Image url NOT valid! -> ' + xpl_url)
                xpl_urls.append (xpl_url)
                

    return ppl_urls, xpl_urls, sample_names
    
    
    
    