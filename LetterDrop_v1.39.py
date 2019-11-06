# -*- coding: utf-8 -*-
"""
Created on Thu May 31 17:09:13 2018

@author: dlekkas
"""
import random
import time
from colorama import init
init()
from colorama import Fore, Back

print '\n', ' ~PROGRAM INITIALIZED~', '\n'
print ' > Conceived and Coded by Damien Lekkas (c) 2018', '\n'

print '\t'*2, '     ', Fore.RED + '+---------------------------------------------------------------------------+' + Fore.RESET        
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + '                             LETTER DROP (v1.39)                           ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '+---------------------------------------------------------------------------+' + Fore.RESET 
print '\n'

print '\t'*2, '     ', Fore.RED + '+------------------------------- INSTRUCTIONS ------------------------------+' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + '                                                                           ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' Drop letters one at a time from above to construct words. During each     ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' turn, select a column (1-9) from which to drop a letter drawn at random.  ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' Words of at least three letters in length may be created within or across ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' columns and either forwards or backwards! Points are based solely on word ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' length and are earned once a valid word is formed. The corresponding      ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' letters used to construct the word are then cleared from the board. Any   ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' and all letters situated above these cleared letters will drop            ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' accordingly. If played in 2 Player Mode, the player forming the word      ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' receives another turn. The goal of the game is to achieve the match point ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' value (1 Player Mode) and achieve it before the other player (2 Player    ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' Mode). But BEWARE! The game is over if or when the letters reach the top  ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' of the board in any one of the nine columns (1 Player Mode), or the board ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' is completely filled with letters (2 Player Mode). In the latter case,    ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' the player with the highest score at Game Over is the winner. To make     ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' matters more interesting, there is a chance to draw blocker characters    ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' (denoted as #). Use these to stymie the opponent or carefully place       ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' them out of the way of critical locations. The only means of removing     ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' these blockers is to place three of them consecutively -- there is a      ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' twenty-five point bonus for doing so. Pay attention to the relative       ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' placement of letters as the board is filled as well as the intel on the   ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' next letter (located in the top right of the screen) to optimize your     ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' strategy and become a Letter Drop master!                                 ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + '                                                                           ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
print '\t'*2, '     ', Fore.RED + '+---------------------------------------------------------------------------+' + Fore.RESET, '\n' 

raw_input(' > PRESS ENTER TO SET GAME TYPE AND TARGET SCORE ')
print '\n'

all_words = open('30_sowpods_ld.txt').readlines()
all_words = [s.rstrip() for s in all_words]

#-------------------------INITIALIZE LETTER BAG--------------------------------
letter_bag = (['A']*7 + ['E']*10 + ['I']*8 + ['O']*6 + ['U']*3 + ['L']*5 + ['N']*6 + ['S']*9 + ['T']*6 + ['R']*6 + ['D']*4 + ['G']*3 + ['B']*2 + ['C']*4 + ['M']*3 + ['P']*3 + ['F']*2 + ['H']*2 + ['V']*1 + ['W']*1 + ['Y']*2 + ['K'] + ['J'] + ['X'] + ['Q'] + ['Z'] + ['#']*10) 

curr_letter = letter_bag[random.randint(0, len(letter_bag)-1)]

col1 = ['\t']*10
col2 = ['\t']*10
col3 = ['\t']*10
col4 = ['\t']*10
col5 = ['\t']*10
col6 = ['\t']*10
col7 = ['\t']*10
col8 = ['\t']*10
col9 = ['\t']*10
col10 = ['\t']*10
col_list = [col1, col2, col3, col4, col5, col6, col7, col8, col9, col10]
row_labels = ['J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']

game_mode = input (' > PLEASE SELECT GAME MODE (ONE PLAYER = 1  OR  TWO PLAYER = 2): ')
print '\n'

while game_mode != 1 and game_mode != 2:
    game_mode = input (' > INVALID ENTRY. PLEASE SELECT GAME MODE (ONE PLAYER = 1  OR  TWO PLAYER = 2): ')
    print '\n'

if game_mode == 2:
    match_score = input(' > PLEASE SET THE DESIRED MATCH SCORE (1 - 9999): ')
    print '\n'

elif game_mode == 1:
    match_score = input(' > PLEASE SET THE DESIRED TARGET SCORE (1 - 9999): ')
    print '\n'

while match_score not in range(1, 10000):
    match_score = input(' > INVALID ENTRY. PLEASE SET A VALID SCORE (1 - 9999): ')
    print '\n'

raw_input(' > OK! PRESS ENTER TO BEGIN GAME ')
print '\n'

game_start = time.time()
p1_score = 0
p2_score = 0
p1_words_formed = 0
p2_words_formed = 0
p1_maxword_len = 0
p2_maxword_len = 0
p1_flag = True
p2_flag = True
word_formed_flag = False
bust_flag = False

def board_print():
        
    global curr_letter
    global next_letter
    global min_space_col
    
    if word_formed_flag == False:
        next_letter = letter_bag[random.randint(0, len(letter_bag)-1)]
    
    if bust_flag == True:
        for letter in range(len(col_list[min_space_col])):
             col_list[min_space_col][letter] = Fore.RED + col_list[min_space_col][letter] + Fore.RESET
    
    row_label_iter = 0
    score_box_iter1 = 0
    score_box_iter2 = 1
    J_print = A_print = Fore.RED + '|' + Fore.RESET + Back.BLUE + Fore.YELLOW + '\t'*2 + '   ' + next_letter + '\t'*2 + Fore.RESET + Back.RESET + Fore.RED + '|' + Fore.RESET 
    D_print = Fore.RED + '+---------' + Fore.RESET + Fore.YELLOW + ' SCORE ' + Fore.RESET + Fore.RED + '---------+' + Fore.RESET
    gap_print = Fore.RED + '|' + Back.BLUE + '                         ' + Back.RESET + '|' + Fore.RESET
    C_print = Fore.RED + '|' + Fore.RESET + Back.BLUE + Fore.GREEN + '  PLAYER 1 :   ' + str(p1_score).zfill(4) + '\t' + Fore.RESET + Back.RESET + Fore.RED + '|' + Fore.RESET
    B_print = Fore.RED + '|' + Fore.RESET + Back.BLUE + Fore.MAGENTA + '  PLAYER 2 :   ' + str(p2_score).zfill(4) + '\t' + Fore.RESET + Back.RESET + Fore.RED + '|' + Fore.RESET
    A_print = Fore.RED + '|' + Fore.RESET + Back.BLUE + Fore.YELLOW + '  MATCH PT :   ' + str(match_score).zfill(4) + '\t' + Fore.RESET + Back.RESET + Fore.RED + '|' + Fore.RESET                             
    base_print = Fore.RED + '+-------------------------+' + Fore.RESET
                                 
    score_box_draw = [gap_print, J_print, gap_print, base_print, '', '', '', '', '', '', '', '', D_print, gap_print, C_print, gap_print, B_print, gap_print, A_print, gap_print]

    print '\t'*2, Fore.RED + '+-----' + Fore.RESET + Fore.YELLOW + '\t', '01  ' + Fore.RESET + Fore.RED + '--' + Fore.RESET + Fore.YELLOW + '\t', '02  ' + Fore.RESET + Fore.RED + '--' + Fore.RESET + Fore.YELLOW + '\t', '03  ' + Fore.RESET + Fore.RED + '--' + Fore.RESET + Fore.YELLOW + '\t', '04  ' + Fore.RESET + Fore.RED + '--' + Fore.RESET + Fore.YELLOW + '\t', '05  ' + Fore.RESET + Fore.RED + '--' + Fore.RESET + Fore.YELLOW + '\t', '06  ' + Fore.RESET + Fore.RED + '--' + Fore.RESET + Fore.YELLOW + '\t', '07  ' + Fore.RESET + Fore.RED + '--' + Fore.RESET + Fore.YELLOW + '\t', '08  ' + Fore.RESET + Fore.RED + '--' + Fore.RESET + Fore.YELLOW + '\t', '09  ' + Fore.RESET + Fore.RED + '--' + Fore.RESET + Fore.YELLOW + '\t', '10  ' + Fore.RESET + Fore.RED + '----+' + Fore.RESET + Fore.RED + '     ' + '+------' + Fore.RESET + Fore.YELLOW + ' NEXT LETTER ' + Fore.RESET + Fore.RED + '------+' + Fore.RESET
    
    for x in range(10):
        print '\t'*2, Fore.RED + '|' + Fore.RESET + Back.BLUE + '\t'*11 + Back.RESET + Fore.RED + '|' + Fore.RESET + '     ' + str(score_box_draw[score_box_iter1])
        print '\t', Fore.YELLOW + row_labels[row_label_iter] + Fore.RESET + Fore.RED + ' +---', '\t', '|' + Fore.RESET + Back.BLUE + col1[x], col2[x], col3[x], col4[x], col5[x], col6[x], col7[x], col8[x], col9[x], col10[x], '\t' + Back.RESET + Fore.RED + '|' + Fore.RESET + '     ' + str(score_box_draw[score_box_iter2])
        row_label_iter += 1
        score_box_iter1 += 2
        score_box_iter2 += 2
    
    if word_formed_flag == True:
        next_letter = letter_bag[random.randint(0, len(letter_bag)-1)]
                        
    print '\t'*2, Fore.RED + '+---------------------------------------------------------------------------------------+' + Fore.RESET + '     ' + base_print      
    
    return


def p1_letter_drop():
    global col_list
    global p1_colsel
    global curr_letter
      
    print '\n'*2, '\t'*6, '      ', Fore.YELLOW + curr_letter, 'IS DRAWN' + Fore.RESET, '\n'
    
    while True:
        try: 
            p1_colsel = raw_input(' > PLAYER 1 LETTER DROP COLUMN: ')      
            print '\n'
            p1_colsel = int(p1_colsel)
            break
        except ValueError:
            print 'Invalid selection! Please select an appropriate column: '
            
            
    while p1_colsel not in range(1,11) or '\t' not in col_list[p1_colsel - 1]:
        p1_colsel = input('Invalid selection! Please select an appropriate column: ')
    
    else:
        space_count = col_list[p1_colsel - 1].count('\t')
        col_list[p1_colsel - 1][space_count-1] = '\t' + curr_letter
    
    curr_letter = next_letter           
    
    return       


def p2_letter_drop():
    global col_list
    global p2_colsel
    global curr_letter
     
    print '\n'*2, '\t'*6, '      ', Fore.YELLOW + curr_letter, 'IS DRAWN' + Fore.RESET, '\n'
    
    while True:
        try: 
            p2_colsel = raw_input(' > PLAYER 2 LETTER DROP COLUMN: ')      
            print '\n'
            p2_colsel = int(p2_colsel)
            break
        except ValueError:
            print 'Invalid selection! Please select an appropriate column: '
            
            
    while p2_colsel not in range(1,11) or '\t' not in col_list[p2_colsel - 1]:
        p2_colsel = input('Invalid selection! Please select an appropriate column: ')
    
    else:
        space_count = col_list[p2_colsel - 1].count('\t')
        col_list[p2_colsel - 1][space_count-1] = '\t' + curr_letter
    
    curr_letter = next_letter           
   
    return             


def p1_board_check():
    global col_list
    global word_formed_flag
    global p1_words_formed
    global p1_maxword_len
    global curr_letter
    global next_letter
    global match_score
    global game_mode
    
#-----------------------------CHECK COLUMNS------------------------------------    
    col_check_for = ''.join([i for i in col_list[p1_colsel-1]])
    col_check_for = col_check_for.replace('\t', '')
    col_poss_words_for = []
    col_poss_words_rev = []
    n = len(col_check_for)
    from_ind = 0
    to_ind = n
    
    cols_for = []
    col_from_inds_for = []
    col_to_inds_for = []
    
#ALL POSSIBLE LETTER COMBINATIONS
    for x in range(n*(n+1)/2):
        if from_ind == to_ind:
           from_ind = 0
           to_ind -= 1
        if from_ind != to_ind:
            word = col_check_for[from_ind : to_ind]
            col_poss_words_for.append(word)
            cols_for.append(p1_colsel-1)
            col_from_inds_for.append(from_ind)
            col_to_inds_for.append(to_ind-1)
            from_ind += 1
   
    for word in col_poss_words_for:
        word = word[::-1]
        col_poss_words_rev.append(word)
   
    cols_rev = cols_for
    col_from_inds_rev = col_to_inds_for
    col_to_inds_rev = col_from_inds_for
    
##IMPORTANT INDEX VARIABLES    
    #print 'Column forward words:', col_poss_words_for
    #print 'Column forward Word indices (Col/from/to): '
    #print cols_for, '\n', col_from_inds_for, '\n', col_to_inds_for, '\n'
     
    #print 'Column reverse words:', col_poss_words_rev
    #print 'Column reverse word indices (col/from/to): ' 
    #print cols_rev, '\n', col_from_inds_rev, '\n', col_to_inds_rev, '\n'
    
    
#-----------------------------CHECK ROWS---------------------------------------    
    curr_height = 10 - col_list[p1_colsel-1].count('\t')
    
    row_check_for = []
    cols_row_for_pre = []  
    rows_row_for = []
    row_from_inds_for = []
    row_to_inds_for = []

    for i in range(10):
        row_check_for.append(col_list[i][10-curr_height])
    
    poss_words = ['']*10
    pointer = 0
    col_iterator = 0
    for letter in row_check_for:
        if letter == '\t':
            pointer += 1
            
        else:
            poss_words[pointer] = poss_words[pointer] + letter
            cols_row_for_pre.append(col_iterator)
        col_iterator += 1
    
    poss_words = filter(None, poss_words)
    
    cols_row_for_pre_copy = [] 
    for col in cols_row_for_pre:
        cols_row_for_pre_copy.append(col)
    
    row_check_for = []
    
    for word in poss_words:
        row_check_for.append(word.replace('\t', ''))
    
    for word in row_check_for:
        wordlen = len(word)
        row_from_inds_for.append(cols_row_for_pre[0])
        row_to_inds_for.append(cols_row_for_pre[wordlen-1])    
        del cols_row_for_pre[0:wordlen]
        
    extended_row_from_inds_for = []
    extended_row_to_inds_for = []
    
    row_poss_words_for = []
    row_poss_words_rev = []
    
    wordnum = 0 
    pointer = 0
    for z in row_check_for:
        word = ''
        wordlen = len(z)
        from_ind = 0
        to_ind = wordlen
        
        for x in range(wordlen*(wordlen+1)/2):
            if from_ind == to_ind:
                from_ind = 0
                to_ind -= 1
            
            if from_ind != to_ind:
                word = row_check_for[wordnum][from_ind : to_ind]
                row_poss_words_for.append(word)
                from_ind += 1
            
                temp_wordletters = []
        
                for zz in z:
                    temp_wordletters.append(zz)
               
        incr1 = cols_row_for_pre_copy[pointer]
        incr2 = cols_row_for_pre_copy[pointer] + wordlen-1
    
        for y in range(wordlen*(wordlen+1)/2):
            extended_row_from_inds_for.append(incr1)    
            if incr1 == incr2:
                incr2 -= 1
                incr1 = cols_row_for_pre_copy[pointer]
            else:
                incr1 += 1
            
        incr1 = wordlen-1 + cols_row_for_pre_copy[pointer]
        incr2 = cols_row_for_pre_copy[pointer]     
        incr3 = cols_row_for_pre_copy[pointer]
        for yy in range(wordlen*(wordlen+1)/2):       
            extended_row_to_inds_for.append(incr1)
            incr2 += 1
            if incr2 == wordlen + incr3:
                incr1 -= 1
                incr2 = cols_row_for_pre_copy[pointer]  
                incr3 -= 1
        
        pointer = pointer + wordlen        
        wordnum += 1  
        
        rows_row_for = [curr_height-1]*len(row_poss_words_for)

    for word in row_poss_words_for:
        word = word[::-1]
        row_poss_words_rev.append(word)
    
    rows_row_rev = rows_row_for
    extended_row_from_inds_rev = extended_row_to_inds_for 
    extended_row_to_inds_rev = extended_row_from_inds_for

#IMPORTANT INDEX VARIABLES    
    #print 'Row forward words:', row_poss_words_for
    #print 'Word row indices forward: ', rows_row_for
    #print 'Words from col index forward: ', extended_row_from_inds_for
    #print 'Words to col index forward: ', extended_row_to_inds_for
    
    #print 'Row reverse words:', row_poss_words_rev
    #print 'Row reverse words:', row_poss_words_rev
    #print 'Word row indices reverse: ', rows_row_rev
    #print 'Words from col index reverse: ', extended_row_from_inds_rev
    #print 'Words to col index reverse: ', extended_row_to_inds_rev
    
    
#------------------CHECK ALL POSSIBLE WORDS AGAINST DICTIONARY-----------------    
    all_poss_words = col_poss_words_for + col_poss_words_rev + row_poss_words_for + row_poss_words_rev    
    all_poss_words_col = col_poss_words_for + col_poss_words_rev
    all_poss_words_row = row_poss_words_for + row_poss_words_rev
    all_word_row_froms = col_from_inds_for + col_from_inds_rev + rows_row_for + rows_row_rev
    all_word_row_tos = col_to_inds_for + col_to_inds_rev + rows_row_for + rows_row_rev
    all_word_col_froms = cols_for + cols_rev + extended_row_from_inds_for + extended_row_from_inds_rev
    all_word_col_tos = cols_for + cols_rev + extended_row_to_inds_for + extended_row_to_inds_rev
   
    
    #print 'ALL POSSIBLE WORDS:', all_poss_words
    #print 'COLUMN FROM COORDS:', all_word_col_froms
    #print 'COLUMN TO COORDS:', all_word_col_tos
    #print 'ROW FROM COORDS:', all_word_row_froms
    #print 'ROW TO COORDS:', all_word_row_tos 
        
    valid_words = []
    valid_words_lens = []
    valid_words_colfrom_coords = []
    valid_words_colto_coords = []
    valid_words_rowfrom_coords = []
    valid_words_rowto_coords = []
    
    for word in range(len(all_poss_words)):
        if len(all_poss_words[word]) > 2 and all_poss_words[word] in all_words:
             valid_words.append(all_poss_words[word])
             valid_words_lens.append(len(all_poss_words[word]))
             valid_words_colfrom_coords.append(all_word_col_froms[word])
             valid_words_colto_coords.append(all_word_col_tos[word])
             valid_words_rowfrom_coords.append(all_word_row_froms[word])
             valid_words_rowto_coords.append(all_word_row_tos[word])
    
    max_possword_len_col = 0
    for word in all_poss_words_col:
        if len(word) > max_possword_len_col:
            max_possword_len_col = len(word)
    
    max_possword_len_row = 0
    for word in all_poss_words_row:
        if len(word) > max_possword_len_row:
            max_possword_len_row = len(word)
    
    #print 'VALID WORDS:', valid_words
    #print 'VALID WORD LENGTHS:', valid_words_lens    
    #print 'VALID WORD COLUMN FROM COORDS:', valid_words_colfrom_coords    
    #print 'VALID WORD COLUMN TO COORDS:', valid_words_colto_coords
    #print 'VALID WORD ROW FROM COORDS:', valid_words_rowfrom_coords
    #print 'VALID WORD ROW TO COORDS:', valid_words_rowto_coords
    
    if len(valid_words) != 0:
        word_select = ''
        word_select_ind = 0
        curr_word_len = 0
        for word in valid_words:
            if len(word) > curr_word_len:
                curr_word_len = len(word)
                word_select = word
                word_select_ind = valid_words.index(word)
        
        word_select_len = len(word_select)
        
        if word_select_len > p1_maxword_len:
            p1_maxword_len = word_select_len  
        
        
#-----------------SCORE WORD AND REMOVE LETTERS FROM BOARD--------------------#
        if valid_words_colfrom_coords[word_select_ind] == int(valid_words_colto_coords[word_select_ind]):
            k = int(valid_words_colfrom_coords[word_select_ind])
            l = int(valid_words_colto_coords[word_select_ind])
            m = int(valid_words_rowfrom_coords[word_select_ind] + (10 - max_possword_len_col))
            n = int(valid_words_rowto_coords[word_select_ind] + (10 - max_possword_len_col))
            o = 0
            
            if k > l:
                o = k
                k = l
                l = o
            
            if m > n:
                o = m
                m = n
                n = o
        
            for col in range(k, l+1):
                for row in range(m, n+1):
                    col_list[col][row] = Fore.YELLOW + col_list[col][row] + Fore.RESET
                    
            word_formed_flag = True
            board_print()
            word_formed_flag = False
            
            print '\n'*2, '\t'*6, '   ', '<', Fore.YELLOW + word_select + Fore.RESET, 'FORMED!', '>' '\n'
            p1_words_formed += 1
            
            for col in range(k, l+1):
                for row in range(m, n+1):
                    del col_list[col][row]
                    col_list[col].insert(0, '\t')
                
        elif valid_words_rowfrom_coords[word_select_ind] == valid_words_rowto_coords[word_select_ind]:
            k = int(valid_words_colfrom_coords[word_select_ind])
            l = int(valid_words_colto_coords[word_select_ind])
            m = int(9 - valid_words_rowfrom_coords[word_select_ind])
            n = int(9 - valid_words_rowto_coords[word_select_ind])
            o = 0
        
            if k > l:
                o = k
                k = l
                l = o
            
            if m > n:
                o = m
                m = n
                n = o
            
            for col in range(k, l+1):
                for row in range(m, n+1):
                    col_list[col][row] = Fore.YELLOW + col_list[col][row] + Fore.RESET
            
            word_formed_flag = True
            board_print()
            word_formed_flag = False
            
            print '\n'*2, '\t'*6, '   ', '<', Fore.YELLOW + word_select + Fore.RESET, 'FORMED!', '>' '\n'
            p1_words_formed += 1
            
            for col in range(k, l+1):
                for row in range(m, n+1):
                    del col_list[col][row]
                    col_list[col].insert(0, '\t')
    
        global p1_score
        p1_turn_score = 0
        
        if word_select == '###':
            p1_turn_score = 25
        
        elif len(word_select) == 3:
            p1_turn_score = 10
         
        elif len(word_select) == 4:
            p1_turn_score = 15
            
        elif len(word_select) == 5:
            p1_turn_score = 30           
        
        elif len(word_select) == 6:
            p1_turn_score = 50
        
        elif len(word_select) == 7:
            p1_turn_score = 100
        
        elif len(word_select) == 8:
            p1_turn_score = 200
            
        elif len(word_select) == 9:
            p1_turn_score = 300
            
        elif len(word_select) == 10:
            p1_turn_score = 500
        
        p1_score = p1_score + p1_turn_score
        
        print '\n'*2, '\t'*6, 'PLAYER 1:', Fore.YELLOW + '+', str(p1_turn_score), 'POINTS!' + Fore.RESET, '\n'
        
        if game_mode == 2:
            print '\t'*2, '     ', Fore.GREEN + '[ PLAYER 1 CURRENT SCORE:', str(p1_score).rjust(4), ']' + Fore.RESET, '\t'*2, Fore.MAGENTA + '[ PLAYER 2 CURRENT SCORE:', str(p2_score).rjust(4), ']' + Fore.RESET, '\n'*3
        
        if p1_score >= match_score:
            return                            
        
        if game_mode == 2:                            
            print ' > PLAYER 1 TAKES ANOTHER TURN!', '\n'                            
        
        if game_mode == 1:
            print '\n'
        
        raw_input(' > PRESS ENTER TO CONTINUE ')    
        print '\n'                        
        
        if game_mode == 2:
            board_print()
        
        return
    
    print '\n'
    global p1_flag
    global p2_flag
    p1_flag = False
    p2_flag = True
    
    word_formed_flag = False
    
    return 

def p2_board_check():
    global col_list
    global word_formed_flag
    global p2_words_formed
    global p2_maxword_len
    global curr_letter
    global next_letter
    global match_score
    
#-----------------------------CHECK COLUMNS------------------------------------    
    col_check_for = ''.join([i for i in col_list[p2_colsel-1]])
    col_check_for = col_check_for.replace('\t', '')
    col_poss_words_for = []
    col_poss_words_rev = []
    n = len(col_check_for)
    from_ind = 0
    to_ind = n
    
    cols_for = []
    col_from_inds_for = []
    col_to_inds_for = []
    
#ALL POSSIBLE LETTER COMBINATIONS

    for x in range(n*(n+1)/2):
        if from_ind == to_ind:
           from_ind = 0
           to_ind -= 1
        if from_ind != to_ind:
            word = col_check_for[from_ind : to_ind]
            col_poss_words_for.append(word)
            cols_for.append(p2_colsel-1)
            col_from_inds_for.append(from_ind)
            col_to_inds_for.append(to_ind-1)
            from_ind += 1
    
    for word in col_poss_words_for:
        word = word[::-1]
        col_poss_words_rev.append(word)
   
    cols_rev = cols_for
    col_from_inds_rev = col_to_inds_for
    col_to_inds_rev = col_from_inds_for
    
##IMPORTANT INDEX VARIABLES    
    #print 'Column reverse words:', col_poss_words_rev
    #print 'Column reverse word indices (col/from/to): ' 
    #print cols_rev, '\n', col_from_inds_rev, '\n', col_to_inds_rev, '\n'
    
    #print 'Column forward words:', col_poss_words_for
    #print 'Column forward Word indices (Col/from/to): '
    #print cols_for, '\n', col_from_inds_for, '\n', col_to_inds_for, '\n'
    
#-----------------------------CHECK ROWS---------------------------------------    
    curr_height = 10 - col_list[p2_colsel-1].count('\t')
    
    row_check_for = []
    cols_row_for_pre = []  
    rows_row_for = []
    row_from_inds_for = []
    row_to_inds_for = []

    for i in range(10):
        row_check_for.append(col_list[i][10-curr_height])
    
    poss_words = ['']*10
    pointer = 0
    col_iterator = 0
    for letter in row_check_for:
        if letter == '\t':
            pointer += 1
            
        else:
            poss_words[pointer] = poss_words[pointer] + letter
            cols_row_for_pre.append(col_iterator)
        col_iterator += 1
    
    poss_words = filter(None, poss_words)
    
    cols_row_for_pre_copy = [] 
    for col in cols_row_for_pre:
        cols_row_for_pre_copy.append(col)
    
    row_check_for = []
    
    for word in poss_words:
        row_check_for.append(word.replace('\t', ''))

    for word in row_check_for:
        wordlen = len(word)
        row_from_inds_for.append(cols_row_for_pre[0])
        row_to_inds_for.append(cols_row_for_pre[wordlen-1])    
        del cols_row_for_pre[0:wordlen]
        
    extended_row_from_inds_for = []
    extended_row_to_inds_for = []
    
    row_poss_words_for = []
    row_poss_words_rev = []
    
    wordnum = 0 
    pointer = 0
    for z in row_check_for:
        word = ''
        wordlen = len(z)
        from_ind = 0
        to_ind = wordlen
        
        for x in range(wordlen*(wordlen+1)/2):
            if from_ind == to_ind:
                from_ind = 0
                to_ind -= 1
            
            if from_ind != to_ind:
                word = row_check_for[wordnum][from_ind : to_ind]
                row_poss_words_for.append(word)
                from_ind += 1
            
                temp_wordletters = []
        
                for zz in z:
                    temp_wordletters.append(zz)
               
        incr1 = cols_row_for_pre_copy[pointer]
        incr2 = cols_row_for_pre_copy[pointer] + wordlen-1
    
        for y in range(wordlen*(wordlen+1)/2):
            extended_row_from_inds_for.append(incr1)    
            if incr1 == incr2:
                incr2 -= 1
                incr1 = cols_row_for_pre_copy[pointer]
            else:
                incr1 += 1
        
        incr1 = wordlen-1 + cols_row_for_pre_copy[pointer]
        incr2 = cols_row_for_pre_copy[pointer]     
        incr3 = cols_row_for_pre_copy[pointer]
        for yy in range(wordlen*(wordlen+1)/2):       
            extended_row_to_inds_for.append(incr1)
            incr2 += 1
            if incr2 == wordlen + incr3:
                incr1 -= 1
                incr2 = cols_row_for_pre_copy[pointer]  
                incr3 -= 1
        
        pointer = pointer + wordlen        
        wordnum += 1  
        
        rows_row_for = [curr_height-1]*len(row_poss_words_for)

    for word in row_poss_words_for:
        word = word[::-1]
        row_poss_words_rev.append(word)
    
    rows_row_rev = rows_row_for
    extended_row_from_inds_rev = extended_row_to_inds_for 
    extended_row_to_inds_rev = extended_row_from_inds_for

#IMPORTANT INDEX VARIABLES    
    #print 'Row forward words:', row_poss_words_for
    #print 'Word row indices forward: ', rows_row_for
    #print 'Words from col index forward: ', extended_row_from_inds_for
    #print 'Words to col index forward: ', extended_row_to_inds_for
    
    #print 'Row reverse words:', row_poss_words_rev
    #print 'Row reverse words:', row_poss_words_rev
    #print 'Word row indices reverse: ', rows_row_rev
    #print 'Words from col index reverse: ', extended_row_from_inds_rev
    #print 'Words to col index reverse: ', extended_row_to_inds_rev
    
    
#------------------CHECK ALL POSSIBLE WORDS AGAINST DICTIONARY-----------------    
    all_poss_words = col_poss_words_for + col_poss_words_rev + row_poss_words_for + row_poss_words_rev    
    all_poss_words_col = col_poss_words_for + col_poss_words_rev
    all_poss_words_row = row_poss_words_for + row_poss_words_rev
    all_word_row_froms = col_from_inds_for + col_from_inds_rev + rows_row_for + rows_row_rev
    all_word_row_tos = col_to_inds_for + col_to_inds_rev + rows_row_for + rows_row_rev
    all_word_col_froms = cols_for + cols_rev + extended_row_from_inds_for + extended_row_from_inds_rev
    all_word_col_tos = cols_for + cols_rev + extended_row_to_inds_for + extended_row_to_inds_rev
   
    
    #print 'ALL POSSIBLE WORDS:', all_poss_words
    #print 'COLUMN FROM COORDS:', all_word_col_froms
    #print 'COLUMN TO COORDS:', all_word_col_tos
    #print 'ROW FROM COORDS:', all_word_row_froms
    #print 'ROW TO COORDS:', all_word_row_tos 
        
    valid_words = []
    valid_words_lens = []
    valid_words_colfrom_coords = []
    valid_words_colto_coords = []
    valid_words_rowfrom_coords = []
    valid_words_rowto_coords = []
    
    for word in range(len(all_poss_words)):
        if len(all_poss_words[word]) > 2 and all_poss_words[word] in all_words:
             valid_words.append(all_poss_words[word])
             valid_words_lens.append(len(all_poss_words[word]))
             valid_words_colfrom_coords.append(all_word_col_froms[word])
             valid_words_colto_coords.append(all_word_col_tos[word])
             valid_words_rowfrom_coords.append(all_word_row_froms[word])
             valid_words_rowto_coords.append(all_word_row_tos[word])
    
    max_possword_len_col = 0
    for word in all_poss_words_col:
        if len(word) > max_possword_len_col:
            max_possword_len_col = len(word)
    
    max_possword_len_row = 0
    for word in all_poss_words_row:
        if len(word) > max_possword_len_row:
            max_possword_len_row = len(word)
    
    #print 'VALID WORDS:', valid_words
    #print 'VALID WORD LENGTHS:', valid_words_lens    
    #print 'VALID WORD COLUMN FROM COORDS:', valid_words_colfrom_coords    
    #print 'VALID WORD COLUMN TO COORDS:', valid_words_colto_coords
    #print 'VALID WORD ROW FROM COORDS:', valid_words_rowfrom_coords
    #print 'VALID WORD ROW TO COORDS:', valid_words_rowto_coords
    
    if len(valid_words) != 0:
        word_select = ''
        word_select_ind = 0
        curr_word_len = 0
        for word in valid_words:
            if len(word) > curr_word_len:
                curr_word_len = len(word)
                word_select = word
                word_select_ind = valid_words.index(word)
        
        word_select_len = len(word_select)
        
        if word_select_len > p2_maxword_len:
            p2_maxword_len = word_select_len    
        
        
#-----------------SCORE WORD AND REMOVE LETTERS FROM BOARD--------------------#
        if valid_words_colfrom_coords[word_select_ind] == int(valid_words_colto_coords[word_select_ind]):
            k = int(valid_words_colfrom_coords[word_select_ind])
            l = int(valid_words_colto_coords[word_select_ind])
            m = int(valid_words_rowfrom_coords[word_select_ind] + (10 - max_possword_len_col))
            n = int(valid_words_rowto_coords[word_select_ind] + (10 - max_possword_len_col))
            o = 0
        
            if k > l:
                o = k
                k = l
                l = o
            
            if m > n:
                o = m
                m = n
                n = o
        
            for col in range(k, l+1):
                for row in range(m, n+1):
                    col_list[col][row] = Fore.YELLOW + col_list[col][row] + Fore.RESET
            
            word_formed_flag = True
            board_print()
            word_formed_flag = False
            
            print '\n'*2, '\t'*6, '   ', '<', Fore.YELLOW + word_select + Fore.RESET, 'FORMED!', '>' '\n'
            p2_words_formed += 1
            
            for col in range(k, l+1):
                for row in range(m, n+1):
                    del col_list[col][row]
                    col_list[col].insert(0, '\t')
    
        elif valid_words_rowfrom_coords[word_select_ind] == valid_words_rowto_coords[word_select_ind]:
            k = int(valid_words_colfrom_coords[word_select_ind])
            l = int(valid_words_colto_coords[word_select_ind])
            m = int(9 - valid_words_rowfrom_coords[word_select_ind])
            n = int(9 - valid_words_rowto_coords[word_select_ind])
            o = 0
        
            if k > l:
                o = k
                k = l
                l = o
            
            if m > n:
                o = m
                m = n
                n = o
            
            for col in range(k, l+1):
                for row in range(m, n+1):
                    col_list[col][row] = Fore.YELLOW + col_list[col][row] + Fore.RESET
            
            word_formed_flag = True
            board_print()
            word_formed_flag = False
            
            print '\n'*2, '\t'*6, '   ', '<', Fore.YELLOW + word_select + Fore.RESET, 'FORMED!', '>' '\n'
            p2_words_formed += 1
            
            for col in range(k, l+1):
                for row in range(m, n+1):
                    del col_list[col][row]
                    col_list[col].insert(0, '\t')
    
        global p2_score
        p2_turn_score = 0
        
        if word_select == '###':
            p2_turn_score = 25
        
        elif len(word_select) == 3:   
            p2_turn_score = 10
           
        elif len(word_select) == 4:
            p2_turn_score = 15
            
        elif len(word_select) == 5:
            p2_turn_score = 30            
        
        elif len(word_select) == 6:
            p2_turn_score = 50
        
        elif len(word_select) == 7:
            p2_turn_score = 100
        
        elif len(word_select) == 8:
            p2_turn_score = 200
            
        elif len(word_select) == 9:
            p2_turn_score = 300
            
        elif len(word_select) == 10:
            p2_turn_score = 500
        
        p2_score = p2_score + p2_turn_score
        print '\n'*2, '\t'*6, 'PLAYER 2:', Fore.YELLOW + '+', str(p2_turn_score), 'POINTS!' + Fore.RESET, '\n'
        print '\t'*2, '     ', Fore.GREEN + '[ PLAYER 1 CURRENT SCORE:', str(p1_score).rjust(4), ']' + Fore.RESET, '\t'*2, Fore.MAGENTA + '[ PLAYER 2 CURRENT SCORE:', str(p2_score).rjust(4), ']' + Fore.RESET, '\n'*3
        
        if p2_score >= match_score:
            return
                            
        print ' > PLAYER 2 TAKES ANOTHER TURN!', '\n'                            
        raw_input(' > PRESS ENTER TO CONTINUE ')   
        print '\n'                         
        
        board_print()
       
        return
    
    print '\n'
    global p1_flag
    global p2_flag
    p1_flag = True
    p2_flag = False
    word_formed_flag = False
    
    return 

#------------------------------GAME MODES--------------------------------------

#TWO PLAYER MODE

while game_mode == 2:
    space_count = 0
    for col in col_list:
        for entry in col:
            if entry == '\t':
                space_count += 1
    
    if space_count != 0:
        board_print()
            
        while p1_flag == True:
            p1_letter_drop()
            p1_board_check()
            if p1_score >= match_score:
                game_end = time.time()
                print ' > PLAYER 1 MATCH SCORE ACHIEVED!', '\n'
                raw_input(' > PRESS ENTER FOR GAME SUMMARY ')
                print '\n'*2
                break
        
        if p1_score >= match_score:
            break
        
        if space_count == 0:
            game_end = time.time()
            print ' > GAME OVER!', '\n'
            raw_input(' > PRESS ENTER FOR GAME SUMMARY ')
            print '\n'*2
            break
        
        board_print()
        
        while p2_flag == True:
            p2_letter_drop()
            p2_board_check()
            if p2_score >= match_score:
                game_end = time.time()
                print ' > PLAYER 2 MATCH SCORE ACHIEVED!', '\n'
                raw_input(' > PRESS ENTER FOR GAME SUMMARY ')
                print '\n'*2
                break
    
        if p2_score >= match_score:
            break
           
    else:
        game_end = time.time()
        print ' > GAME OVER!', '\n'
        raw_input(' > PRESS ENTER FOR GAME SUMMARY ')
        print '\n'*2
        break

#ONE PLAYER MODE

while game_mode == 1:
    space_count = 0
    for col in col_list:
        for entry in col:
            if entry == '\t':
                space_count += 1
    
    min_space = 10
    min_space_col = 10
    for col in col_list:
        col_space = 0
        for entry in col:
            if entry == '\t':
                col_space += 1               
        if col_space < min_space:
            min_space = col_space
            min_space_col = col_list.index(col)
            
    if min_space != 0:
        board_print()
             
        p1_letter_drop()
        p1_board_check()
       
        if p1_score >= match_score:
            game_end = time.time()
            print ' > PLAYER 1 TARGET SCORE ACHIEVED!', '\n'
            raw_input(' > PRESS ENTER FOR GAME SUMMARY ')
            print '\n'*2
            break
        
        if space_count == 0:
            game_end = time.time()
            print ' > GAME OVER!', '\n'
            raw_input(' > PRESS ENTER FOR GAME SUMMARY ')
            print '\n'*2
            break
        
    else:
        bust_flag = True
        board_print()
        game_end = time.time()
        print ' > GAME OVER!', '\n'
        raw_input(' > PRESS ENTER FOR GAME SUMMARY ')
        print '\n'*2
        break

mins_elapsed = round((float(game_end) - game_start)/60, 1)

if game_mode == 2:    
    if p1_score > p2_score:
        print '\t'*5 + Fore.GREEN + 'P  ' + Fore.RED + 'L  ' + Fore.YELLOW + 'A  ' + Fore.MAGENTA + 'Y  ' + Fore.CYAN + 'E  ' + Fore.GREEN + 'R  ' + Fore.RED + '  1    ' + Fore.YELLOW + 'W  ' + Fore.MAGENTA + 'I  ' + Fore.CYAN + 'N  ' + Fore.GREEN + 'S  ' + Fore.RED + '  !  ' + Fore.YELLOW + '  !  ' + Fore.MAGENTA + '  !' + Fore.RESET, '\n'*2
    
    elif p2_score > p1_score:
        print '\t'*5 + Fore.GREEN + 'P  ' + Fore.RED + 'L  ' + Fore.YELLOW + 'A  ' + Fore.MAGENTA + 'Y  ' + Fore.CYAN + 'E  ' + Fore.GREEN + 'R  ' + Fore.RED + '  2    ' + Fore.YELLOW + 'W  ' + Fore.MAGENTA + 'I  ' + Fore.CYAN + 'N  ' + Fore.GREEN + 'S  ' + Fore.RED + '  !  ' + Fore.YELLOW + '  !  ' + Fore.MAGENTA + '  !' + Fore.RESET, '\n'*2 

    else:
        print '\t'*5 + Fore.GREEN + 'T  ' + Fore.RED + 'I  ' + Fore.YELLOW + 'E  ' + Fore.MAGENTA + '  G  ' + Fore.CYAN + 'A  ' + Fore.GREEN + 'M  ' + Fore.RED + 'E  ' + Fore.YELLOW + '  !', '\n'*2 

    print '\t'*2, '     ', Fore.RED + '+------------------------------- GAME SUMMARY ------------------------------+' + Fore.RESET 
    print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + '                                                                           ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
    print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' PLAYER 1 FINAL SCORE        : ' + str(p1_score).rjust(5) + '  POINTS                               ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
    print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' PLAYER 2 FINAL SCORE        : ' + str(p2_score).rjust(5) + '  POINTS                               ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
    print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + '                                                                           ' + Back.RESET + Fore.RED + '|' + Fore.RESET                                                                                                         
    print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' PLAYER 1 TOTAL WORDS FORMED : ' + str(p1_words_formed).rjust(5) + '  WORDS                                ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
    print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' PLAYER 2 TOTAL WORDS FORMED : ' + str(p2_words_formed).rjust(5) + '  WORDS                                ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
    print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + '                                                                           ' + Back.RESET + Fore.RED + '|' + Fore.RESET    
    print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' PLAYER 1 LONGEST WORD LENGTH: ' + str(p1_maxword_len).rjust(5) + '  LETTERS                              ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
    print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' PLAYER 2 LONGEST WORD LENGTH: ' + str(p2_maxword_len).rjust(5) + '  LETTERS                              ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
    print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + '                                                                           ' + Back.RESET + Fore.RED + '|' + Fore.RESET    
    print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' TOTAL GAME TIME ELAPSED     : ' + str(mins_elapsed).rjust(5) + '  MINUTES' + '                              ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
    print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + '                                                                           ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
    print '\t'*2, '     ', Fore.RED + '+---------------------------------------------------------------------------+' + Fore.RESET, '\n'*2
    

if game_mode == 1:    
    if p1_score >= match_score:
        print '\t'*4 + Fore.GREEN + 'C  ' + Fore.RED + 'O  ' + Fore.YELLOW + 'N  ' + Fore.MAGENTA + 'G  ' + Fore.CYAN + 'R  ' + Fore.GREEN + 'A  ' + Fore.RED + 'T  ' + Fore.YELLOW + 'U  ' + Fore.MAGENTA + 'L  ' + Fore.CYAN + 'A  ' + Fore.GREEN + 'T  ' + Fore.RED + 'I  ' + Fore.YELLOW + 'O  ' + Fore.MAGENTA + 'N  ' + Fore.CYAN + 'S  ' + Fore.GREEN + '  !  ' + Fore.RED + '  !  ' + Fore.YELLOW + '  !' + Fore.RESET, '\n'*2
    
   
    print '\t'*2, '     ', Fore.RED + '+------------------------------- GAME SUMMARY ------------------------------+' + Fore.RESET 
    print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + '                                                                           ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
    print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' PLAYER 1 FINAL SCORE        : ' + str(p1_score).rjust(5) + '  POINTS                               ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
    print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' PLAYER 1 TARGET SCORE       : ' + str(match_score).rjust(5) + '  POINTS                               ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
    print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + '                                                                           ' + Back.RESET + Fore.RED + '|' + Fore.RESET                                                                                                         
    print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' PLAYER 1 TOTAL WORDS FORMED : ' + str(p1_words_formed).rjust(5) + '  WORDS                                ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
    print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + '                                                                           ' + Back.RESET + Fore.RED + '|' + Fore.RESET    
    print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' PLAYER 1 LONGEST WORD LENGTH: ' + str(p1_maxword_len).rjust(5) + '  LETTERS                              ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
    print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + '                                                                           ' + Back.RESET + Fore.RED + '|' + Fore.RESET    
    print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + ' TOTAL GAME TIME ELAPSED     : ' + str(mins_elapsed).rjust(5) + '  MINUTES' + '                              ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
    print '\t'*2, '     ', Fore.RED + '|' + Fore.RESET + Back.BLUE + '                                                                           ' + Back.RESET + Fore.RED + '|' + Fore.RESET 
    print '\t'*2, '     ', Fore.RED + '+---------------------------------------------------------------------------+' + Fore.RESET, '\n'*2
    


raw_input(' > THANKS FOR PLAYING! PRESS ENTER TO EXIT: ')
print '\n', '~PROGRAM TERMINATED~', '\n'


