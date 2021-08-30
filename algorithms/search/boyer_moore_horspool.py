def set_up(m: int, search_value: str) -> dict:
    offset_dict = {}
    symbol_set = set()
    for i in range(m - 2, -1, -1):
        if search_value[i] not in symbol_set:
            offset_dict[search_value[i]] = m - i - 1
            symbol_set.add(search_value[i])

    if search_value[m - 1] not in symbol_set:
        offset_dict[search_value[m - 1]] = m

    offset_dict['*'] = m
    return offset_dict


def bmh(text: str, search_value: str) -> int:
    n = len(text)
    m = len(search_value)
    offset_dict = set_up(m, search_value)

    if n >= m:
        i = m - 1
        while i < n:
            k = 0
            for j in range(m - 1, -1, -1):
                if text[i - k] != search_value[j]:
                    if j == m - 1:
                        off = offset_dict[text[i]] if offset_dict.get(text[i], False) else offset_dict['*']
                    else:
                        off = offset_dict[search_value[j]]
                    i += off
                    break
                k += 1
            else:
                return i - k + 1
        else:
            return -1
    else:
        return -1
