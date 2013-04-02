import json
import logging

#from mapreduce import operation as op

from google.appengine.api import search

def build_search_index(entity):
	data = json.loads(entity.json)
	year, genus, collection_code, country = map(data.get, 
		['year', 'genus', 'collectioncode', 'country'])

	print 'data: %s %s %s %s' % (year, genus, collection_code, country)
		
	doc = search.Document(
		fields=[search.TextField(name='year', value=year),
				search.TextField(name='genus', value=genus),
        		search.TextField(name='collection_code', value=collection_code),
        		search.TextField(name='country', value=country)])

	print 'DOC: %s' % doc
	
	try:
	    search.Index(name='dwc_search').put(doc)
	except search.Error:
	    logging.exception('Put failed')
