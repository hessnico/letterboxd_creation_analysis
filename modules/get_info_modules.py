def get_info(json_format, row_name, what_i_want):
    info = []
    for i in range(len(json_format[row_name])):
        info.append(json_format[row_name][i][what_i_want])
    info_str = ", "
    return info_str.join(info)

def find_movie(json_format, year):
    if 'results' in json_format:
        for j in range(0, len(json_format['results'])):
            if 'release_date' in json_format['results'][j]:
                if str(year) == str(json_format['results'][j]['release_date'][0:4]) or str(year+1) == str(json_format['results'][j]['release_date'][0:4]) or str(year-1) == str(json_format['results'][j]['release_date'][0:4]):
                    return json_format['results'][j]
    return None