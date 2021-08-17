def commands(number):
    handshakes = ["wink", "double blink", "close your eyes", "jump"]
    number_string = f"{number%32:b}".zfill(5)
    reverse_commands = len(number_string) == 5 and number_string[0] == '1'
    number_string = number_string[1:][::-1]

    result = []
    for i, command in enumerate(number_string):
        if command == '1':
            result.append(handshakes[i])
    if reverse_commands:
        result.reverse()
    return result
