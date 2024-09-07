import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    import csv
    from tempfile import TemporaryFile
    with TemporaryFile(mode='w+', encoding='utf-8') as fout:
        csv_writer = csv.writer(fout)
        csv_writer.writerow(['File', 'Image ID', 'Confidence', 'Xmin', 'Xmax', 'Ymin', 'Ymax'])

        for result in results:
            # get the file name and path
            index = os.path.basename(result.path)
            # get the image ID according to the filename
            index_split = index.split('_')
            index = index_split[0] + '_' + index_split[1] # file name without extension
            
            csv_writer.writerow