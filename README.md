# input-file-capturer

This is a google cloud function to automatically capture customer excel files uploaded from portal.
Once a new file is submitted to portal, a new blob on GCS is created, and the event will triger a GCF that validate the data and upload the same to GBQ.
