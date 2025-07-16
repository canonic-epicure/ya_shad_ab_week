import sys
import json
import math

# file = open("04_logs_data.json", "r", encoding="utf-8")
# str = file.read()

str = sys.stdin.read()

data = json.loads(str)

# file.close()

def rel_dcg(results):
    return sum([ result[ 'relevance' ] / (i + 1) for i, result in enumerate(results) ])

def revenue(results):
    return sum([ result[ 'cost' ] / math.sqrt(i + 1) for i, result in enumerate(results) ])


def get_extra_quality_after_insert(results, r):
    quality = 0

    for i in range(r, len(results) - 1):
        quality += (results[ i ][ 'relevance' ] - results[ i + 1 ][ 'relevance' ]) / (i + 2)

    return quality


new_docs = {}

for doc in data[ 'new_documents' ]:
    query = doc[ 'query' ]

    if not (query in new_docs):
        new_docs[ query ] = []

    new_docs[ query ].append(doc)

for query in new_docs:
    new_docs[ query ].sort(key=lambda x: (x[ 'cost' ], x[ 'relevance' ]), reverse=True)


total_cost = 0

for query in data[ 'serpset' ]:
    results = query[ 'results' ]

    quality = rel_dcg(results)
    cost = revenue(results)

    docs = new_docs[ query[ 'query' ] ]

    size_res = len(results)
    initial_quality = rel_dcg(results)

    # print(f'query={ query[ 'query' ] }, initial_quality={ initial_quality }, initial cost={ revenue(results) }')

    docs_to_insert = new_docs[ query[ 'query' ] ]
    docs_to_insert_size = len(docs_to_insert)

    if docs_to_insert_size == 0:
        continue

    d = 0
    r = 0

    extra_quality = 0

    while d < docs_to_insert_size and r < size_res:
        result = results[ r ]
        doc = docs_to_insert[ d ]

        if doc[ 'cost' ] >= result[ 'cost' ]:
            quality_delta = (result[ 'relevance' ] - doc[ 'relevance' ]) / (r + 1)
            extra_quality_after_insert = get_extra_quality_after_insert(results, r)

            if quality_delta <= 0 or quality_delta < extra_quality_after_insert + extra_quality:
                extra_quality += extra_quality_after_insert - quality_delta
                results[ r:r ] = [ doc ]
                results.pop(-1)

                d += 1
                r += 1
            else:
                r += 1
        else:
            r += 1

    # print(f'query={ query[ 'query' ] }, final_quality={ rel_dcg(results) }, final cost={ revenue(results) }')

    total_cost += revenue(results)


print(round(total_cost, 2))


# print(data[ 'serpset' ])