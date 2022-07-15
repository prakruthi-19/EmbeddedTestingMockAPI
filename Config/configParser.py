import configparser


def getConfig(key):
    parser = configparser.ConfigParser()
    parser.read("C://HU Training//Embedded Systems//EmbeddedTestingMockAPI//Config//config.ini")
    result = parser['API'][key]
    return result
