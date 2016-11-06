
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '8F884D9E598A812BDA62C3E6DC277854'
    
_lr_action_items = {'RPAREN':([1,2,8,9,16,17,19,20,21,22,23,],[-10,-11,-12,17,-8,-9,-7,-5,-6,-3,-4,]),'DIVIDE':([1,2,5,6,8,9,16,17,18,19,20,21,22,23,],[-10,-11,-12,11,-12,11,-8,-9,11,-7,11,-6,11,11,]),'POWER':([1,2,5,6,8,9,16,17,18,19,20,21,22,23,],[-10,-11,-12,12,-12,12,-8,-9,12,-7,-5,-6,-3,-4,]),'INT':([0,3,7,10,11,12,13,14,15,],[1,1,1,1,1,1,1,1,1,]),'FLOAT':([0,3,7,10,11,12,13,14,15,],[2,2,2,2,2,2,2,2,2,]),'EQUALS':([5,],[10,]),'TIMES':([1,2,5,6,8,9,16,17,18,19,20,21,22,23,],[-10,-11,-12,13,-12,13,-8,-9,13,-7,13,-6,13,13,]),'PLUS':([1,2,5,6,8,9,16,17,18,19,20,21,22,23,],[-10,-11,-12,14,-12,14,-8,-9,14,-7,14,-6,-3,-4,]),'LPAREN':([0,3,7,10,11,12,13,14,15,],[3,3,3,3,3,3,3,3,3,]),'VAR':([0,3,7,10,11,12,13,14,15,],[5,8,8,8,8,8,8,8,8,]),'MINUS':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,],[7,-10,-11,7,-12,15,7,-12,15,7,7,7,7,7,7,-8,-9,15,-7,15,-6,-3,-4,]),'$end':([1,2,4,5,6,8,16,17,18,19,20,21,22,23,],[-10,-11,0,-12,-2,-12,-8,-9,-1,-7,-5,-6,-3,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,3,7,10,11,12,13,14,15,],[6,9,16,18,19,20,21,22,23,]),'statement':([0,],[4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> VAR EQUALS expression','statement',3,'p_statement_assign','CASOLUS.py',73),
  ('statement -> expression','statement',1,'p_statement_expr','CASOLUS.py',79),
  ('expression -> expression PLUS expression','expression',3,'p_expression_plus','CASOLUS.py',84),
  ('expression -> expression MINUS expression','expression',3,'p_expression_minus','CASOLUS.py',89),
  ('expression -> expression POWER expression','expression',3,'p_expression_power','CASOLUS.py',94),
  ('expression -> expression TIMES expression','expression',3,'p_expression_times','CASOLUS.py',99),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_divide','CASOLUS.py',104),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','CASOLUS.py',109),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','CASOLUS.py',115),
  ('expression -> INT','expression',1,'p_expression_int','CASOLUS.py',121),
  ('expression -> FLOAT','expression',1,'p_expression_float','CASOLUS.py',127),
  ('expression -> VAR','expression',1,'p_expression_var','CASOLUS.py',133),
]
