def response(hey_bob):
    msg = hey_bob.replace(" ", "")
    if not msg or msg.isspace():
        return "Fine. Be that way!"
    elif is_question(msg) and is_yelling(msg):
        return "Calm down, I know what I'm doing!"
    elif is_yelling(msg):
        return "Whoa, chill out!"
    elif is_question(msg):
        return "Sure."

    return "Whatever."


def is_question(msg):
    return msg[-1] == '?'


def is_yelling(msg):
    result = [ch.isupper() for ch in msg if ch.isalpha()]
    return all(result) and result
