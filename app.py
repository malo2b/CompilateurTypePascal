from pCodeFonctions import interpreteur_pcode

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

interpreteur_pcode(pcode)