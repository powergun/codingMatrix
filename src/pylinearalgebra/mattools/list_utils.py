def flatten(xs):
    o = []
    for x in xs:
        if isinstance(x, list):
            o.extend(x)
        else:
            o.append(x)
    return o
    