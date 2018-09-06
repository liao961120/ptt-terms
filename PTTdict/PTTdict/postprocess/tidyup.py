import re

class Cleanbracket(object):
    def process_item(self, item, spider):
        ''' Clean field "bracket" '''
        
        if 'bracket' not in item:
            item['bracket'] = None
        
        # Remove brackets around strings

        lst = list()
        for i in item['bracket']:
            no_bracket = re.sub(r'」', '', re.sub(r'「', '', i))
            lst.append(no_bracket)
        
        # Remove LONG strings
        rm_long_string(lst)

        # Extract Unique value
        lst = list(set(lst))
        
        # Deal with empty
        if len(lst) == 0:
            lst = None
        
        item['bracket'] = lst
        
        return item
        
        
class Cleanbold(object):
    def process_item(seld, item, spider):
        ''' Clean field "bold" '''
        
        if 'bold' not in item:
            item['bold'] = None
        
        # Remove inner parenthesis in strings 
        lst = list()
        for i in item['bold']:
            rm_paren = re.sub(r'（.+）', '', i)                
            lst.append(rm_paren)

        # Remove LONG strings
        rm_long_string(lst)
            
        # Extract Unique value
        lst = list(set(lst))
        
        # Deal with empty
        if len(lst) == 0:
            lst = None
            
        item['bold'] = lst
        
        return item
        
        
# Helper Functions

def rm_long_string(lst):
    for i in lst:
        if len(i) >= 10:
            lst.remove(i)
