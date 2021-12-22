import re

def is_ID(id:str):
    return True if re.match("[a-zA-Z_][a-zA-Z_0-9]*", id) else False

def analyseur_lexical(fichier:str):
    print(is_ID("aaa"))
    print(is_ID("1aa"))
    # Lecture du fichier avec séparation des ; et \n
    code = ""
    with open(fichier,'r') as f:
        for ligne in f:
            for lettre in ligne:
                if lettre== ";":
                    code += " ; "
                elif lettre == ",":
                    code += " , "
                elif lettre=="\n":
                    code+= " "
                else:
                    code += lettre

    # Suppression des commentaires
    code = re.sub("\(\*(.*?)\*\)", "", code)

    # Séparation des mots et réassemblement des différentes instructions
    code=code.split(" ")
    code=[value for value in code if value != '']
    instructions = []
    instruction_courante = []
    for mot in code:
        if mot == ";":
            instruction_courante.append(mot)
            instructions.append(instruction_courante)
            instruction_courante = []
        elif mot == "begin" or mot == "end" or mot == "repeat":
            if instruction_courante != []:
                instructions.append(instruction_courante)
            instructions.append([mot])
            instruction_courante = []
        else:
            instruction_courante.append(mot)
    instructions.append(instruction_courante)
    code=[instruction for instruction in instructions if instruction != []]
    print(instructions)

    # Analyse du lexique

    # Program
    instruction = instructions[0]
    assert instruction[0] == "program", "SyntaxError: Missing program declaration in header"
    assert re.match("[a-zA-Z_][a-zA-Z_0-9]*", (instruction[1]), "SyntaxError: Missing program name in header"
    assert instruction[2] == ";", "SyntaxError: Missing semicolon in header declaration"

    #Bloc

    fin_des_consts = False
    fin_des_vars = False

    for instruction in instructions:
        # Déclaration CONSTS
        if instruction[0] == "const":
            assert not fin_des_consts, "SyntaxError: Cant declare const after var"
            assert re.match("[a-zA-Z_][a-zA-Z_0-9]*", instruction[1]), f"SyntaxError: \"{instruction[1]}\" is not a legal const name"
            assert instruction[2] == "=" , f"SyntaxError: Expected \= in const declaration"
            assert re.match("[+-]?[0-9]+", instruction[3]), f"ValueError: \"{instruction[3]}\" Expected integer in const affectation"
            assert instruction[4] == ";", f"SyntaxError: Expected semicolon"
        # Déclaration VARS
        elif instruction[0] == "var":
            assert not fin_des_vars, "SyntaxError: Cant declare var after an INSTS"
            fin_des_consts = True
            assert instruction[1] != ";", "SyntaxError: excepted variable name"
            i = 1
            nom_variable_attendu = True # A la prochaine instruction
            while instruction[i] != ";":
                if nom_variable_attendu:
                    assert re.match("[a-zA-Z_][a-zA-Z_0-9]*", instruction[i]), f"SyntaxError: \"{instruction[i]}\" is not a legal variable name"
                    nom_variable_attendu = False
                else: # , attendu
                    assert instruction[i] == ",", f"SyntaxError: \"{instruction[i]}\" expected comma between 2 variable"
                    nom_variable_attendu = True
                i+=1
            assert nom_variable_attendu == False, f"SyntaxError: \"{instruction[i-1]}\" expected variable after a comma"
        # INSTS
        assert ['begin'] in instructions, "SyntaxError: BEGIN expected"
        # Affec
        if instruction == ['begin']:
            fin_des_vars = True

        # Verification que le BLOC finisse bien par end
        assert instructions[-2] == ['end'], "SyntaxError: expected \"end\" at the end of BLOCK "
        # . Verification que le programme finisse par un point
        assert instructions[-1] == ["."], "SyntaxError: expected \'.\' at the end of the program"
analyseur_lexical("code.code")