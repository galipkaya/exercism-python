def annotate(minefield):
    # Function body starts here
    result = []
    len_i = len(minefield)
    if len_i == 0:
        return []

    len_j = len(minefield[0])

    # check errors
    for i in range(len_i):
        if len(minefield[i]) != len_j:
            raise ValueError("different len")
        for ch in minefield[i]:
            if ch not in [" ", "*"]:
                raise ValueError("invalid char")

    for i in range(len_i):
        line = minefield[i]
        new_line = [0]*len(line)
        result.append(new_line)
        for j in range(len_j):
            if minefield[i][j] == "*":
                result[i][j] = "*"
                continue
            if i>0 and minefield[i-1][j] == "*":
                result[i][j] += 1
            if i<len_i-1 and minefield[i+1][j] == "*":
                result[i][j] += 1
            if j>0 and minefield[i][j-1] == "*":
                result[i][j] += 1
            if j<len_j-1 and minefield[i][j+1] == "*":
                result[i][j] += 1
            if j<len_j-1 and i<len_i-1 and minefield[i+1][j+1] == "*":
                result[i][j] += 1
            if j>0 and i>0 and minefield[i-1][j-1] == "*":
                result[i][j] += 1
            if j<len_j-1 and i>0 and minefield[i-1][j+1] == "*":
                result[i][j] += 1
            if j>0 and i<len_i-1 and minefield[i+1][j-1] == "*":
                result[i][j] += 1

    new_result = []
    for line in result:
        string = ""
        for ch in line:
            if ch == 0:
                string += " "
            else:
                string += str(ch)
        new_result.append(string)

    return new_result






