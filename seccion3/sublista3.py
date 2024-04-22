def haveSublist(arr) -> bool:
    for i in arr:
        if type(i) == list:
            return True
    return False
