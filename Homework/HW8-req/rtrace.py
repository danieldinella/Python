#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 16:38:23 2020

@author: Prof. Sterbini (edited by iacopo)
"""

class TraceRecursion:
    def __init__(self,f):
        self.f = f
        self.traceP = False
        self.countP = False
        self.indent = 0
        self.numcalls = 0

    def trace(self,*args,**kargs):
        self.traceP = True
        self.countP = True
        self.indent = 0
        self.numcalls = 0
        print('------------------- Starting recursion -------------------')
        answer = self.__call__(*args,**kargs)
        print('-------------------- Ending recursion --------------------')
        print('Num calls:', self.numcalls)
        self.countP = False
        self.traceP = False
        return answer

    def __call__(self,*args,**kargs):
        '''Conta e traccia (se richiesto) le chiamate alla funzione'''
        if self.traceP:
            indent     = '|--'*self.indent
            callstring = self.f.__name__
            if args : callstring += str(args)
            if kargs: callstring += str(kargs)
            print (indent+" entering", callstring , sep='\t')
            self.indent += 1
        if self.countP:
            self.numcalls += 1
        answer = self.f(*args,**kargs)
        if self.traceP:
            self.indent -= 1
            print(indent+' exiting ', callstring,"returns", answer, sep='\t')
        return answer