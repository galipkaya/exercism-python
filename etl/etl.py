def transform(legacy_data):
    result = {}
    for k, v in legacy_data.items():
        for i in v:
            result[i.lower()] = k
    return result
