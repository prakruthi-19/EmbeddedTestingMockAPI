import configparser


def getConfig(key):
    parser = configparser.ConfigParser()
    parser.read("C://Users//prakrk//PycharmProjects//EmbeddedTestingMockAPI//Config//config.ini")
    result = parser['API'][key]
    return result
