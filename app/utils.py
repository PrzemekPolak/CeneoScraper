#funkcja do usuwania znaków formatujących
def remove_whitespaces(string):
    try:
        return string.replace("\n", ", ").replace("\r", ", ")
    except AttributeError:
        pass

