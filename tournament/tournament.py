import functools


class Info:
    def __init__(self, name, match_played, win, draw, loss, point):
        self.name = name
        self.match_played = match_played
        self.win = win
        self.draw = draw
        self.loss = loss
        self.point = point


def compare(item1, item2):
    if item1.point < item2.point:
        return -1
    elif item1.point > item2.point:
        return 1
    else:
        if item1.name > item2.name:
            return -1
        elif item1.name < item2.name:
            return 1
        else:
            return 0


def get_info(table, name):
    for info in table:
        if info.name == name:
            return info

    table.append(Info(name, 0, 0, 0, 0, 0))
    return get_info(table, name)


def tally(rows):
    table = []
    for row in rows:
        team1, team2, status = row.split(";")
        if status == "win":
            win_info = get_info(table, team1)
            win_info.match_played += 1
            win_info.win += 1
            win_info.point += 3
            loss_info = get_info(table, team2)
            loss_info.match_played += 1
            loss_info.loss += 1
        elif status == "loss":
            win_info = get_info(table, team2)
            win_info.match_played += 1
            win_info.win += 1
            win_info.point += 3
            loss_info = get_info(table, team1)
            loss_info.match_played += 1
            loss_info.loss += 1
        else:
            draw1_info = get_info(table, team1)
            draw1_info.match_played += 1
            draw1_info.draw += 1
            draw1_info.point += 1
            draw2_info = get_info(table, team2)
            draw2_info.match_played += 1
            draw2_info.draw += 1
            draw2_info.point += 1

    table = sorted(table, key=functools.cmp_to_key(compare), reverse=True)
    result = ["Team                           | MP |  W |  D |  L |  P"]
    for row in table:
        name = row.name.ljust(31)
        result.append(f"{name}|  {row.match_played} |  {row.win} |  {row.draw} |  {row.loss} |  {row.point}")
    return result
