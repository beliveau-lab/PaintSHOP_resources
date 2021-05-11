
import sys
import pickle
import requests

# configure script 
DOI_DICT = {
    '10.1073/pnas.1213818110': 'oligopaints',
    '10.1073/pnas.1714530115': 'oligominer',
    '10.1101/2020.07.05.188797': 'ps_rxiv',
    '10.1038/s41592-019-0404-0': 'kishi_2019',
    '10.1038/s41586-019-1035-4': 'mateo_2019',
    '10.1073/pnas.1912459116': 'xia_2019',
    '10.1126/science.aaa6090': 'MERFISH',
    '10.1093/bioinformatics/btr011': 'jellyfish',
    '10.1021/acssynbio.9b00523': 'NUPACK',
}
URL = 'http://api.crossref.org/works/%(doi)s/transform/application/x-bibtex'

# load cache file
CACHE_FILE = 'bib_cache.pickle'
try:
    BIB_CACHE = pickle.load(open(CACHE_FILE, 'rb'))
except FileNotFoundError:
    BIB_CACHE = {}

def main():
    
    # create bibliography file
    bib_text = ''.join(get_bib(doi) for doi in DOI_DICT)
    with open('../bibliography.bib', 'w') as outfile:
        outfile.write(bib_text)
    
    # success
    print('DONE!')


def get_bib(doi):
        
    if doi in BIB_CACHE:

        # get cached result
        bib_text = BIB_CACHE[doi]
    
    else:
    
        # get bibtext citation for this doi
        request_url = URL % {'doi': doi}
        response = requests.get(request_url)
        if response.status_code != 200:
            sys.exit('Error: DOI {} was not found. Response: {} {}'.format(doi, response.status_code, response.reason))
        bib_list = response.content.decode('utf-8').split(',')
        bib_list[0] = '@article{' + DOI_DICT[doi]
        bib_text = ','.join(bib_list) + '\n'

        # add this result to the cache and update the cache file
        BIB_CACHE[doi] = bib_text
        pickle.dump(BIB_CACHE, open(CACHE_FILE, 'wb'))
        
    # success  
    return(bib_text)


if __name__ == '__main__':
    main()
