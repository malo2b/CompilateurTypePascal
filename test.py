a=[['procedure', 'BLOCK', ';'], ['begin', 'if', 'TOKEN', '=', 'CONST_TOKEN', 'then', 'CONSTS', ';'], ['if', 'TOKEN', '=', 'VAR_TOKEN', 'then', 'VARS', ';'], ['INSTS', 'end']]

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

