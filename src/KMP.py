"""
code of KMP search all ocurences of pattern in text
"""
def compute_lps_array(pattern):
    """
    returns array where each position tells length of the longest subarray of chars which equals
    subarray from the start of pattern
    """
    len_suffix = 0  # length of the previous longest prefix suffix
    lps = [0] * len(pattern)  # lps[0] is always 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[len_suffix]:
            len_suffix += 1
            lps[i] = len_suffix
            i += 1
        else:
            if len_suffix != 0:
                len_suffix = lps[len_suffix - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(needle, haystack):
    """
    needle is pattern which we are searching in string text (haystack)
    and returns list of all occurrences in text as indexes of first index of matching pattern
    """
    lps_array = compute_lps_array(needle)
    index_text = 0
    index_pattern = 0
    result_arr = []
    while index_text<len(haystack):
        if needle[index_pattern] == haystack[index_text]:
            index_text += 1
            index_pattern += 1
        if index_pattern == len(needle):
            result_arr.append(index_text - index_pattern)
            index_pattern = lps_array[index_pattern - 1]
        elif index_text < len(haystack) and needle[index_pattern] != haystack[index_text]:
            if index_pattern != 0:
                index_pattern = lps_array[index_pattern - 1]
            else:
                index_text += 1
    return result_arr


