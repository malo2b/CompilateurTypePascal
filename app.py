from pCodeFonctions import *

pcode = ["INT 2",
        "LDA 0" ,
        "INN" ,
        "LDA 1" ,
        "LDA 0" ,
        "LDV" ,
        "LDA 1" ,
        "LDV" ,
        "ADD" ,
        "STO" ,
        "LDA 0" ,
        "LDV" ,
        "LDI 0" ,
        "EQL" ,
        "BZE 1" ,
        "LDA 1" ,
        "LDV" ,
        "PRN" ,
        "HLT"]

def interpreteur_pcode(pcode):
    pc = 0 # Compteur d'instruction
    sp = 0 # Pointeur de somet de pile
    mem = [None]*10 # Pile


    while pcode[pc] != "HLT":
        print(mem)
        if type(pcode[pc]) == str:
            pcode[pc] = pcode[pc].split(" ")
        print(pcode[pc])

        if pcode[pc][0] == "ADD":
            ADD(mem)
        elif pcode[pc][0] == "SUB":
            SUB(mem)
        elif pcode[pc][0] == "MUL":
            MUL(mem)
        elif pcode[pc][0] == "DIV":
            DIV(mem)
        elif pcode[pc][0] == "EQL":
            EQL(mem)
        elif pcode[pc][0] == "NEQ":
            NEQ(mem)
        elif pcode[pc][0] == "GTR":
            GTR(mem)
        elif pcode[pc][0] == "LSS":
            LSS(mem)
        elif pcode[pc][0] == "GEQ":
            GEQ(mem)
        elif pcode[pc][0] == "LEQ":
            LEQ(mem)
        elif pcode[pc][0] == "PRN":
            PRN(mem)
        elif pcode[pc][0] == "INN":
            INN(mem)
        elif pcode[pc][0] == "INT":
            INT(mem, pcode[pc][1], sp)
            sp += int(pcode[pc][1])
        elif pcode[pc][0] == "LDI":
            LDI(mem, int(pcode[pc][1]))
        elif pcode[pc][0] == "LDA":
            LDA(mem, int(pcode[pc][1]))
        elif pcode[pc][0] == "LDV":
            LDV(mem)
        elif pcode[pc][0] == "STO":
            STO(mem)
        elif pcode[pc][0] == "BRN":
            pc = int(pcode[pc][1])
        elif pcode[pc][0] == "BZE":
            if mem[-1] == 0:
                pc = int(pcode[pc][1])-1 # -1 car réincrémenté a la fin du corp de la boucle
                del(mem[-1])
        elif pcode[pc] == "HLT":
            HLT()

        pc += 1

interpreteur_pcode(pcode)