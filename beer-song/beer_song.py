def recite(start, take=1):
    lyrics = [
        ["No more bottles of beer on the wall, no more bottles of beer.",
         "Go to the store and buy some more, 99 bottles of beer on the wall."],
        ["1 bottle of beer on the wall, 1 bottle of beer.",
         "Take it down and pass it around, no more bottles of beer on the wall."],
        ["2 bottles of beer on the wall, 2 bottles of beer.",
         "Take one down and pass it around, 1 bottle of beer on the wall."]
    ]
    result = []
    for i in range(start, start-take, -1):
        if i > 2:
            result.append(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            result.append(f"Take one down and pass it around, {i-1} bottles of beer on the wall.")
        else:
            result.extend(lyrics[i])

        result.append("")

    result.pop()
    return result
