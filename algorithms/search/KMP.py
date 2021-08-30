def get_prefix(string: str) -> list:
    length = len(string)
    p = [0] * length
    i, j = 0, 1
    while j < length:
        if string[i] == string[j]:
            p[j] = i + 1
            i += 1
            j += 1
        elif i:
            i = p[i - 1]
        else:
            p[j] = 0
            j += 1
    return p


def kmp(text: str, search_value: str) -> list:
    """алгоритм Кнута — Морриса — Пратта"""
    search_value_len = len(search_value)
    text_len = len(text)
    if not text_len or search_value_len > text_len:
        return []
    p = get_prefix(search_value)
    entries = []
    i = j = 0
    while i < text_len and j < search_value_len:
        if text[i] == search_value[j]:
            if j == search_value_len - 1:
                entries.append(i - search_value_len + 1)
                j = 0
            else:
                j += 1
            i += 1
        elif j:
            j = p[j - 1]
        else:
            i += 1
    return entries
