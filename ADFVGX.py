# -*- coding: utf-8 -*-


#Bon au final je suis pas sur que ca serve a quelque chose du tout... Faudrait relire le PDF

#Dechiffreur chiffre ADFVGX
#--------------------------
#
# On va lire un fichier,
# compter le nombre d'occurences de chaque paires et
# essayer de determiner a quelle lettre elles peuvent correspondre.
# On fini par essayer de traduire le message

from operator import itemgetter

#Lit un fichier adfvgx et range les paires dans un tableau pour les traduire
def get_and_parse (file_name):
    # Lecture du fichier contenant le message chiffre
    f = open(file_name, "r");
    text = f.read();
    # Separe le texte en paires de lettres
    tab = [];
    i = 1;
    mot = "";
    for lettre in text:
        mot += lettre;
        if len(mot) == 2:
            tab.append(mot);
            mot = "";
            i = 1;
        i+=1;
    return (tab);

tab = get_and_parse("gedefu.txt");
tab.sort() # On tri le tableau de maniere alphabetique

# Compte le nombre d'occurences pour chaque paires
# Rempli un tableau avec les occurences
# Et un autre tableau avec le nombre de fois ou elles apparaissent
tab_nb_occu = [];
dico_occu = {};
i = 0;
nb = 1;
ok = "";
for paire in tab:
    if i == 0:
         dico_occu.update({paire : nb});    #On ajoute l'elem au dico si c'est le premier elem
        i += 1;
        ok = paire;
    elif ok == paire: #Regarde si la cle a deja ete enregistree
        nb += 1;
    else:
        dico_occu.update({paire : nb})    #Ajoute l'elem
        nb = 1;
        i += 1;
        ok = paire;

parsed_tab = sorted(dico_occu.items(), key=itemgetter(1), reverse=True);

#Previens du nombre de chars utilisés et donc du potentiel alphabet
nblen = len(dico_occu);
if nblen == 35:
    print("Alphabet + Numeric Len : ", nblen);
elif nblen == 26:
    print("Alphabet seul Len : ", nblen);
elif nblen > 35:
    print("Alphabet + Numeric + surement d'autres caracteres(genre majuscules). Len : ", nblen);
elif nblen < 26:
    print("Message surement trop court a dechiffrer Len : ", nblen);

# Traduit un message chiffré en adfvgx selon un referenciel donne
# dico        = Dictionnaire avec les paires et la lettre leur correspondant
# text         = Le texte à traduire
def trad(dico, text):
    end_str = "";
    tmp = "";
    for paire in text:
        tmp = dico.get(paire);
        if tmp:
            end_str += tmp;
    return end_str;

# Genere un dictionnaire avec la traduction Ex -> 'AA' : 'e'
def to_dico(str_alpha, parsed_tab):
    i = 0;
    tabz = [];
    while i < len(parsed_tab):
        tabz.append(parsed_tab[i][0]);
        i += 1;
    dico = {};
    i = 0;
    for item in tabz:
        if i < len(str_alpha):
            tmp = {item : str_alpha[i]};
            dico.update(tmp);
            i += 1;
    return (dico);

# Ordre des ettres les plus utilises pris sur internet
str_alpha_fr = "EASINTRLUODCPMVGFBQHXJYZKW0123456789";
str_alpha_en = "etaoinsrhldcumfpgwybvkxjqz0123456789";

#Transforme le dictionnaire en tableau pour le lire
dico = to_dico(str_alpha_en, parsed_tab);

#On traduit le tableau de lettres chiffrees avec le tableau de lettres frequentes
str_clair = trad(dico, get_and_parse("gedefu.txt"));

print ("TEXTE TADUIT : ");
print(str_clair);



