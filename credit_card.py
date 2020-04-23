#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 15:12:37 2019

@author: dasharath
"""

class CreditCard:
    """"Creating consumer credit card"""
    def __init__(self, person, bank, acnt, limit):
        self._person = person
        self._bank = bank 
        self._account = acnt
        self._limit = limit
        self._balance = 0.
    
    def get_costumer(self):
       return self._person
    def get_account(self):
        return self._bank
    def account_number(self):
        return self._account
    def get_limit(self):
        return self._limit
    def get_balance(self):
        return self._balance
    
    """If a person purchase something amount need to be added to the existing 
       balance and updated balance can not cross the credit limit"""
    def charge(self, amount):
        if amount + self._balance > self.limit:
            raise ValueError("Credit limit reached") 
        else:
            self._balance  += amount  # update the new balance
    
    """After each payment made by the customer the balance need to be reduced
      by tge payment amount"""
    def make_payment(self, payment):
        self._balance -= payment

class PredatoryCreditCard(CreditCard):
    """An extension to the credit card that compounds interest and fees"""
    def __init__(self, person, bank, acnt, limit, apr):
        super().__init__(self, person, bank, acnt, limit) # calling super class
        self._apr = apr
        
    def charge(self, price):
        """Charge given price to the card assuming sufficient credit limit"""
        success = super().charge(price)
        if not success:
            self._balance += 5   # assess penalty
        return success
    def process_month(self):
        """Assess monthly interest on outstanding balance"""
        if self._balance > 0.:
            apr_factor = pow(1 + self._apr, 1/12)
            self._balance *= apr_factor
        
           
            
            
        
       
        