def solution(data, ext, val_ext, sort_by):
    ext_dict = {
        'code' : 0,
        'date' : 1,
        'maximum' : 2,
        'remain' : 3
    }
    
    filtered_data = filter(lambda x: x[ext_dict[ext]] < val_ext, data)
    sorted_data = sorted(filtered_data, key=lambda x: x[ext_dict[sort_by]])
    
    return sorted_data