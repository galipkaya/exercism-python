def handle_error_by_throwing_exception():
    raise Exception("Error")


def handle_error_by_returning_none(input_data):
    if input_data == '1':
        return 1
    return None


def handle_error_by_returning_tuple(input_data):
    if input_data == '1':
        return True, 1
    return False, None


def filelike_objects_are_closed_on_exception(filelike_object):
    try:
        filelike_object.open()
        filelike_object.do_something()
    finally:
        filelike_object.close()
