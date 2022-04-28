import itertools

def powerset(iterable, allow_empty):
    if allow_empty:
        start = 0
    else:
        start = 1

    s = list(iterable)

    return list(itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(start, len(s)+1)))

def get_pairings(a, b):
    if len(b) == 0:
        return [[]]

    if isinstance(a, set):
        a = list(a)
    if isinstance(b, set):
        b = list(b)
    if len(a) == 0:
        return [[]]
    
    first_a = a[0]

    new_pairings = []

    successive_pairings = get_pairings(a[1:], b)

    for successive_pairing in successive_pairings:
        for bi in b:
            new_pairing = list(successive_pairing)
            new_pairing.append((first_a, bi))

            new_pairings.append(new_pairing)
    
    return new_pairings