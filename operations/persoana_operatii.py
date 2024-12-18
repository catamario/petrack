def get_nume(all_persoane):
    nume_list = []
    for persoana in all_persoane:
        nume_list.append(persoana.get_persoana_nume())
    return nume_list




def cautare_persoana(all_list, nume):
    if all_list:
        for persoana in all_list:
            if nume == persoana.get_persoana_nume():
                return persoana.get_persoana_nume()

    return None




def modifica_persoana(all_lista, id):

    if all_lista:
        for persoana in all_lista:
            if id == persoana.get_persoana_id():
                persoana.set_persoana_id(int(input("ID:")))
                persoana.set_persoana_nume(input("NUME:"))
                persoana.set_persoana_adresa(input("ADRESA:"))
                print(f' ID: {persoana.get_persoana_id()}, \n NUME: {persoana.get_persoana_nume()}, \n ADRESA: {persoana.get_persoana_adresa()}')
                break




def delete_persoana(all_persoane, nume):
    for persoana in all_persoane:
        if persoana.get_persoana_nume() == nume:
            all_persoane.remove(persoana)  # Șterge elementul din listă
            return True  # Indica faptul ca persoana a fost ștearsa
    return False  # Indica faptul ca persoana nu a fost gasita

