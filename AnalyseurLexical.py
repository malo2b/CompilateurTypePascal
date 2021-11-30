def analyseur_lexical(fichier:str):
    code = ""
    with open(fichier,'r') as f:
        for ligne in f:
            for lettre in ligne:
                if lettre== ";":
                    code += " ; "
                elif lettre=="\n":
                    code+= " "
                else:
                    code += lettre

    code=code.split(" ")
    code=[value for value in code if value != '']
    #print(code)
    instructions = []
    instruction_courante = []
    for mot in code:
        if mot == ";":
            instruction_courante.append(";")
            instructions.append(instruction_courante)
            instruction_courante = []
        else:
            instruction_courante.append(mot)
    instructions.append(instruction_courante)
    print(instructions)

analyseur_lexical("code.code")

TOKENS =["ID_TOKEN", "NUM_TOKEN", "PLUS_TOKEN", "MOINS_TOKEN", "MUL_TOKEN",
        "DIV_TOKEN", "EGAL_TOKEN" , "DIFF_TOKEN", "INF_TOKEN", "SUP_TOKEN",
        "INF_TOKEN", "SUP_EGAL_TOKEN", "PAR_OUV_TOKEN",
        "PAR_FER_TOKEN", "VIRG_TOKEN", "PT_VIRG_TOKEN", "POINT_TOKEN",
        "AFFEC_TOKEN" , "BEGIN_TOKEN", "END_TOKEN",  "IF_TOKEN" ,"WHILE_TOKEN",
        "THEN_TOKEN", "DO_TOKEN", "WRITE_TOKEN", "READ_TOKEN", "CONST_TOKEN",
        "VAR_TOKEN", "PROGRAM_TOKEN", "TOKEN_INCONNU"]

