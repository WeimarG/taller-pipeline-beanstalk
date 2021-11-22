def load_file(file_name: str) -> dict:
    heroes = {}
    file = open(file_name, "r")
    file.readline()

    line = file.readline()
    while len(line) > 0:
        datos = line.split(";")
        llave = datos[0]
        record = {}
        record['name'] = datos[1]
        record['gender'] = datos[2]
        record['eye_color'] = datos[3]
        record['race'] = datos[4]
        record['hair_color'] = datos[5]
        record['height'] = datos[6]
        record['publisher'] = datos[7]
        record['skin_color'] = datos[8]
        record['alignment'] = datos[9]
        record['weight'] = datos[10].replace('\n', '')
        heroes[llave] = record
        line = file.readline()

    file.close()
    return heroes
