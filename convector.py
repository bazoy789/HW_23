from typing import Optional, Iterable

from funtion import filter_query, unique_query, limit_query, map_query, sort_query


CMD_TO_FUNCTIONS = {
    'filter': filter_query,
    'unique': unique_query,
    'limit': limit_query,
    'map': map_query,
    'sort': sort_query,
}


def read_file(file_name: str):
    with open(file_name) as f:
        for line in f:
            yield line


def configur(cmd: str, value: str, file_name: str, data: Optional[Iterable[str]]):
    if data is None:
        prepr_date = read_file(file_name)
    else:
        prepr_date = data

    return list(CMD_TO_FUNCTIONS[cmd](value=value, data=prepr_date))
