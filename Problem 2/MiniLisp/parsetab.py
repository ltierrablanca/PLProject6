
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'C9A024CB30CB4E73621C1C0BD8B585C1'
    
_lr_action_items = {'FALSE':([0,2,4,5,6,7,8,13,14,15,16,17,18,20,21,22,25,26,],[5,-21,-17,-20,-14,-16,-15,-19,5,-4,5,5,-10,-11,-9,-12,-13,-5,]),'NIL':([0,2,4,5,6,7,8,13,14,15,16,17,18,20,21,22,25,26,],[2,-21,-17,-20,-14,-16,-15,-19,2,-4,2,2,-10,-11,-9,-12,-13,-5,]),'QUOTE':([0,2,4,5,6,7,8,13,14,15,16,17,18,20,21,22,25,26,],[9,-21,-17,-20,-14,-16,-15,-19,9,-4,9,9,-10,-11,-9,-12,-13,-5,]),'SIMB':([0,1,2,4,5,6,7,8,13,14,15,16,17,18,20,21,22,25,26,],[6,14,-21,-17,-20,-14,-16,-15,-19,6,-4,6,6,-10,-11,-9,-12,-13,-5,]),'NUM':([0,2,4,5,6,7,8,13,14,15,16,17,18,20,21,22,25,26,],[7,-21,-17,-20,-14,-16,-15,-19,7,-4,7,7,-10,-11,-9,-12,-13,-5,]),'LPAREN':([0,2,4,5,6,7,8,9,13,14,15,16,17,18,20,21,22,25,26,],[1,-21,-17,-20,-14,-16,-15,16,-19,1,-4,1,1,-10,-11,-9,-12,-13,-5,]),'TEXT':([0,2,4,5,6,7,8,13,14,15,16,17,18,20,21,22,25,26,],[4,-21,-17,-20,-14,-16,-15,-19,4,-4,4,4,-10,-11,-9,-12,-13,-5,]),'RPAREN':([2,4,5,6,7,8,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[-21,-17,-20,-14,-16,-15,-19,-8,-4,-8,-8,-10,25,-11,-9,-7,26,-6,-13,-5,]),'TRUE':([0,2,4,5,6,7,8,13,14,15,16,17,18,20,21,22,25,26,],[13,-21,-17,-20,-14,-16,-15,-19,13,-4,13,13,-10,-11,-9,-12,-13,-5,]),'$end':([0,2,3,4,5,6,7,8,10,11,12,13,15,25,26,],[-18,-21,-2,-17,-20,-14,-16,-15,0,-1,-3,-19,-4,-13,-5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'quoted_list':([0,14,16,17,],[3,18,18,18,]),'items':([14,16,17,],[19,23,24,]),'list':([9,],[15,]),'item':([14,16,17,],[17,17,17,]),'bool':([0,14,16,17,],[8,8,8,8,]),'exp':([0,],[10,]),'atom':([0,14,16,17,],[11,21,21,21,]),'call':([0,14,16,17,],[12,20,20,20,]),'empty':([14,16,17,],[22,22,22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> exp","S'",1,None,None,None),
  ('exp -> atom','exp',1,'p_exp_atom','yacc.py',131),
  ('exp -> quoted_list','exp',1,'p_exp_qlist','yacc.py',135),
  ('exp -> call','exp',1,'p_exp_call','yacc.py',139),
  ('quoted_list -> QUOTE list','quoted_list',2,'p_quoted_list','yacc.py',143),
  ('list -> LPAREN items RPAREN','list',3,'p_list','yacc.py',149),
  ('items -> item items','items',2,'p_items','yacc.py',153),
  ('items -> empty','items',1,'p_items_empty','yacc.py',157),
  ('empty -> <empty>','empty',0,'p_empty','yacc.py',161),
  ('item -> atom','item',1,'p_item_atom','yacc.py',165),
  ('item -> quoted_list','item',1,'p_item_list','yacc.py',173),
  ('item -> call','item',1,'p_item_call','yacc.py',177),
  ('item -> empty','item',1,'p_item_empty','yacc.py',181),
  ('call -> LPAREN SIMB items RPAREN','call',4,'p_call','yacc.py',185),
  ('atom -> SIMB','atom',1,'p_atom_simbol','yacc.py',203),
  ('atom -> bool','atom',1,'p_atom_bool','yacc.py',207),
  ('atom -> NUM','atom',1,'p_atom_num','yacc.py',211),
  ('atom -> TEXT','atom',1,'p_atom_word','yacc.py',215),
  ('atom -> <empty>','atom',0,'p_atom_empty','yacc.py',219),
  ('bool -> TRUE','bool',1,'p_true','yacc.py',223),
  ('bool -> FALSE','bool',1,'p_false','yacc.py',227),
  ('atom -> NIL','atom',1,'p_nil','yacc.py',231),
]
