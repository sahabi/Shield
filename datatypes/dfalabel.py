'''
Created on Jun 3, 2014

@author: bkoenighofer
'''

class DfaLabel(object):
    '''
    classdocs
    '''
 
    def __init__(self, literals=None):
        '''
        Constructor
        '''

        if literals:
            self.literals_=literals
        else:
            self.literals_=[]
    
    def merge(self,otherLabel):
        otherLiterals = otherLabel.getLiterals()
        union = set(sorted(self.literals_ + otherLiterals))
        absUnionLen = len(set(map(abs, union)))
             
        if absUnionLen != len(union):
            union=[0]

        return DfaLabel(list(union))

    def removeLiteral(self, literal):
         if literal in self.literals_:
            self.literals_.remove(literal)
         return DfaLabel(list(self.literals_))

    def getLiterals(self):
        return sorted(list(self.literals_))
    
    def isValidLabel(self):
        if len(self.literals_)==0:
            return True
        literals = list(self.literals_)
        if literals[0]==0:
            return False
        return True