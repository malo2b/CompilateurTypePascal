def analyseur_lexical(fichier:str):
    # Lecture du fichier avec séparation des ; et \n
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

    # Séparation des mots et réssemblement des différentes instructions
    code=code.split(" ")
    code=[value for value in code if value != '']
    instructions = []
    instruction_courante = []
    for mot in code:
        if mot == ";":
            instruction_courante.append(mot)
            instructions.append(instruction_courante)
            instruction_courante = []
        elif mot == "begin" or mot == "end":
            if instruction_courante != []:
                instructions.append(instruction_courante)
            instructions.append([mot])
            instruction_courante = []
        else:
            instruction_courante.append(mot)
    code=[instruction for instruction in instructions if instruction != []]
    print(instructions)

    # Analyse du lexique

    for instruction in instructions:
        # Déclaration variable
        pass







analyseur_lexical("code.code")

TOKENS =["ID_TOKEN", "NUM_TOKEN", "PLUS_TOKEN", "MOINS_TOKEN", "MUL_TOKEN",
        "DIV_TOKEN", "EGAL_TOKEN" , "DIFF_TOKEN", "INF_TOKEN", "SUP_TOKEN",
        "INF_TOKEN", "SUP_EGAL_TOKEN", "PAR_OUV_TOKEN",
        "PAR_FER_TOKEN", "VIRG_TOKEN", "PT_VIRG_TOKEN", "POINT_TOKEN",
        "AFFEC_TOKEN" , "BEGIN_TOKEN", "END_TOKEN",  "IF_TOKEN" ,"WHILE_TOKEN",
        "THEN_TOKEN", "DO_TOKEN", "WRITE_TOKEN", "READ_TOKEN", "CONST_TOKEN",
        "VAR_TOKEN", "PROGRAM_TOKEN", "TOKEN_INCONNU"]

