def add_persoana(all_persoane, persoana_id, nume, adresa):
    if find_by_id_persoana(all_persoane, persoana_id) is None:
        persoana = Persoana(persoana_id, nume, adresa)
        all_persoane.append(persoana)
    else:
        raise ValueError




class Persoana:
    def __init__(self, persoana_id, nume, adresa):
        self.__persoana_id = persoana_id
        self.__nume = nume
        self.__adresa = adresa

    def __str__(self):
        return self.__nume



##GETTER
    def get_persoana_id(self):
        return self.__persoana_id

    def get_persoana_nume(self):
        return self.__nume

    def get_persoana_adresa(self):
        return self.__adresa

##SETTER
    def set_persoana_id(self, persoana_id):
        self.__persoana_id = persoana_id

    def set_persoana_nume(self, nume):
        self.__nume = nume

    def set_persoana_adresa(self, adresa):
        self.__adresa = adresa


## OPERATIONS

    """   (+)     PENTRU NUME"""
    def __add__(self, other):
        return f"{self.__nume} {other.get_persoana_nume()}"


    """(+=)   PENTRU NUME"""
    def __iadd__(self, other):
        self.__nume += f" {other.get_persoana_nume()}"
        return self


    """(-)    PENTRU ID"""
    def __sub__(self, other):
        return self.__persoana_id - other.get_persoana_id()





def find_by_id_persoana(all_lista, id):
    if all_lista:
        for persoana in all_lista:
            if id == persoana.get_persoana_id():
                return persoana
    return None