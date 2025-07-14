from itertools import chain
import sys
import re
import json
import math

# str = sys.stdin.read()
file = open("04_logs_data.json", "r", encoding="utf-8")

data = json.loads(file.read())

file.close()

def rel_dcg(results):
    return sum([ result[ 'relevance' ] / i for i, result in enumerate(results) ])

def revenue(results):
    return sum([ result[ 'cost' ] / math.sqrt(i) for i, result in enumerate(results) ])


new_docs = {}

for doc in data[ 'new_documents' ]:
    query = doc[ 'query' ]

    if not (query in new_docs):
        new_docs[ query ] = []

    new_docs[ query ].append(doc)

for query in new_docs:
    new_docs[ query ].sort(key=lambda x: (x[ 'relevance' ], x[ 'cost' ]), reverse=True)

for query in data[ 'serpset' ]:
    results = query[ 'results' ]

    quality = rel_dcg(results)
    cost = revenue(results)

    docs = new_docs[ query[ 'query' ] ]



