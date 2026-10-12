# Shared helper for mind maps that reuse the leaves of another one (IMSO, IMAS).


def merge_leaves(base_L, examples, new):
    """Keep each base leaf that has examples here (leaf id "<sub>-<letter>" = position in
    base_L[sub]), with those examples, then append the competition's own leaves."""
    L = {}
    for sub, leaves in base_L.items():
        L[sub] = []
        for j, (title, sign, key, _) in enumerate(leaves):
            ex = examples.get(f"{sub}-{chr(97 + j)}")
            if ex:
                L[sub].append((title, sign, key, ex))
        L[sub].extend(new.get(sub, []))
    for sub in new.keys() - base_L.keys():
        L[sub] = list(new[sub])
    return L
