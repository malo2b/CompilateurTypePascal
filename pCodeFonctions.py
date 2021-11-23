
def ADD(pile:list):
    """Additionne le sous-somet et le sommet de la pile, laisse le resultat au sommer

    Args:
        pile (list): Pile
    """
    res = pile[-1] + pile[-2]
    pile.pop(-1)
    pile[len(pile)-1] = res

def SUB(pile:list):
    """Soustrait le sous-somet et le sommet de la pile, laisse le resultat au sommer

    Args:
        pile (list): Pile
    """
    res = pile[-1] - pile[-2]
    pile.pop(-1)
    pile[len(pile)-1] = res

def MUL(pile:list):
    """Multiplie le sous-somet et le sommet de la pile, laisse le resultat au sommer

    Args:
        pile (list): Pile
    """
    res = pile[-1] * pile[-2]
    pile.pop(-1)
    pile[len(pile)-1] = res

def DIV(pile:list):
    """Divise le sous-somet et le sommet de la pile, laisse le resultat au sommer

    Args:
        pile (list): Pile
    """
    res = pile[-1] / pile[-2]
    pile.pop(-1)
    pile[len(pile)-1] = res

def EQL(pile:list):
    """Remplace le sous-sommet par 1 si sous-sommet == sommet, 0 sinon

    Args:
        pile (list): Pile
    """
    if pile[-1] == pile[-2]:
        pile[-2] = 1
        del(pile[-1])
    else:
        pile[-2] = 0
        del(pile[-1])

def NEQ(pile:list):
    """Laisse 1 au sommet si sous-sommet != sommet, 0 sinon

    Args:
        pile (list): Pile
    """
    if pile[-1] != pile[-2]:
        pile[-2] = 1
        pile.pop(-1)
    else:
        pile[-2] = 0
        pile.pop(-1)

def GTR(pile:list):
    """Laisse 1 au sommet si sous-sommet > sommet, 0 sinon

    Args:
        pile (list): Pile
    """
    if pile[-2] > pile[-1]:
        pile[-2] = 1
        pile.pop(-1)
    else:
        pile[-2] = 0
        pile.pop(-1)

def LSS(pile:list):
    """Laisse 1 au sommet si sous-sommet < sommet, 0 sinon

    Args:
        pile (list): Pile
    """
    if pile[-2] < pile[-1]:
        pile[-2] = 1
        pile.pop(-1)
    else:
        pile[-2] = 0
        pile.pop(-1)

def GEQ(pile:list):
    """Laisse 1 au sommet si sous-sommet >= sommet, 0 sinon

    Args:
        pile (list): Pile
    """
    if pile[-2] >= pile[-1]:
        pile[-2] = 1
        pile.pop(-1)
    else:
        pile[-2] = 0
        pile.pop(-1)

def LEQ(pile:list):
    """Laisse 1 au sommet si sous-sommet <= sommet, 0 sinon

    Args:
        pile (list): Pile
    """
    if pile[-2] <= pile[-1]:
        pile[-2] = 1
        pile.pop(-1)
    else:
        pile[-2] = 0
        pile.pop(-1)

def PRN(pile:list):
    """Imrpime le sommet, depile

    Args:
        pile (list): Pile
    """
    print(pile[-1])
    pile.pop(-1)

def INN(pile:list):
    """Lit un entier, le stocke a l'adresse trouvée au sommet de la pile, dépile

    Args:
        pile (list): Pile
    """
    while True:
        try:
            value = int(input("Saisir un entier : "))
            break
        except ValueError:
            print("Veuillez saisir une valeur correcte")
    pile[pile[-1]] = value
    pile.pop(-1)

def INT(pile:list, inc:int, sp:int):
    """Incrémente de la constante c le pointeur de la pile (la constante c peut être négative)
    """
    i = sp
    if int(inc) > 0:
        while i <  sp + int(inc):
            pile[i] = 0
            i+=1;
    # elif inc < 0:
    #     while i > inc:
    #         pile[]

def LDI(pile:list, v):
    """Empile la valeur v

    Args:
        pile (list): Pile
        v : valeur a empiler
    """
    pile.append(v)

def LDA(pile:list, a: int):
    """Empile l'adresse a

    Args:
        pile (list): Pile
        a (int): Adresse à empiler
    """
    pile.append(a)

def LDV(pile:list):
    """Remplace le sommet par la valeur trouvée à l'adresse indiquée par le sommet (déréférence)

    Args:
        pile (list): Pile
    """
    pile[-1] = pile[pile[-1]]

def STO(pile:list):
    """Stocke la valeur au sommet à l'adresse indiquée par le sous-sommet, dépile 2 fois

    Args:
        pile (list): Pile
    """
    pile[pile[-2]] = pile[-1]
    pile.pop(-1)
    pile.pop(-1)

def BRN(i:int):
    """Branchement inconditionnel à l'instruction i

    Args:
        i (int): indice de l'instruction
    """
    return i

def BZE(pile:list, i):
    """Branchement à l'instruction i si le sommet = 0, dépile

    Args:
        i ([type]): [description]
        pile (list): Pile
    """

def HLT():
    """Halte
    """
    print("Fin")