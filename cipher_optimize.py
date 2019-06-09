# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:42:58 2019

Cipher breaking

Script to run "frequency.py" and optimize for most english words generated.

"""
import cipher_analysis as cy

path = r'C:\Users\Pizzagirl\Documents\programming\python\cypher\book_944.txt'


""" look at: patterns(n), frequency,  dup_list  """
    
#most frequent letter patterns
common_1 = [ 'e', 't', 'a', 'o', 'i', 'n', 's', 'h','r', 'd', 'l', 'u']

common_3 = ['the', 'and', 'tha', 'ent', 'ion', 'tio', 'for', 'nde', 'has', 'nce', 'edt', 'tis', 'oft', 'sth', 'men']

common_2 = ['th', 'er', 'on', 'an', 're', 'he', 'in', 'ed', 'nd', 'ha', 'at', 'en', 'es', 'of', 'or', 'nt', 'ea', 'ti', 'to', 'it', 'st', 'io', 'le', 'is', 'ou', 'ar', 'as', 'de', 'rt', 've'] 
#spaces: ohm, mu, 8, 0

common_4 = ['that', 'with', 'have', 'this', 'will', 'your', 'from', 'they', 'know', 'want', 'been', 'good', 'much', 'some', 'time'] 

#get stats and cipher characters in a list
#cipher = list of characters, others are panda data frames.
#single_list = most frequent single chars, dup_list = duplicates, pattn = frequent patterns (2-4) 
cipher, single_list, dup_list, patt2, patt3, patt4 = cy.all_stats(path)

#step 1: map most frequent single letters to most frequent characters.
#map_letters(single_list, dup_list, cipher)



#replace_dict = {'/3':'e', '/zeta': 't', '/nabla': 't', '/t': 's', '/k': ' ', '/w': ' ', '/7': ' ', '/h': 'a'}
#replace characters with guess characters and produce new output (translated) file
#replace_dict, dict1 = replaceletters(cipher,replace_dict)

    #print(replacedlist)



#functions return 'none' or pd.df
