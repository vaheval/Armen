#!/usr/bin/env python


#1#Function counts the length of a string
def my_len (a):
    k=0
    for i in a:
        k=k+1
    return k


#2#Function divides a string by a given character
def my_split (string, n):
    x = 0
    splitstring = []
    for i in range( my_len(string)):
        if string[i] == n:
            splitstring.append ( string[x:i] )
            x = i + 1
    splitstring.append ( string[x:] )
    return splitstring 


#3#The function check is the same as the beginning of the line with the pattern
def my_startswich(example,string):
    for i in range ( my_len ( example )):
        if example[i] != string[i]:
             return False
    return True

#4#The function "my_find" searches for matches with the example and returns the match indexes
def my_find (examp,string):
    p = my_len(examp)
    a = 0
    for y in string:
        if string[a:p] == examp:
            return a
        a = a + 1
        p = p + 1

#5#Function counts the quantity of words in the string.
def my_words(string):
    n = 0
    y = 0 
    if string[0] != ' ':
        n = n + 1
    for i in string [ 1:my_len(string) - 1 ]:
	y = y + 1		
        if string[y] != " " and string[y+1] == ' ':
            n=n+1
    return n

#6#Gives out a string in the reverse order in the "start" "stop" interval
def my_reverse(string,start,stop):
	new = ''
	n = 0
	for i in string [start:stop-n]:
		new = new + string [stop-n]
		n = n + 1
	if start == 0:
		new = new + string[0]
	return new

#7#Function changes the old value of the string to a new value
def my_replace(string,old,new):
	n = 0
	r = (my_len(old))
	newstring = ''
	for i in string:
		if string[n:n+r] == old:
			newstring = string[0:n] + new + string[n+r:my_len(string)+1]
		else:
			n = n + 1
	return newstring				
#8#Function removes spaces at the beginning and end of the line
def my_spacedel(string):
	newstring ='' 
	n = 0
	l = my_len(string)
	for i in string:
		if string [n] == ' ':
			n = n + 1
		elif string [l-1] == ' ':
			l = l - 1 
		else:
			newstring = string[n:l-1]
	return newstring

#9#The function defines a string of digits or not
def my_isdigit(string):
	n = 0 
        for i in string:
                if ord(i) < 47 or ord(i) > 58:
                	return False
	return True  

#10#Function collects a string from a list with a separator "examp"
def my_join ( examp, string ):
        string1=''
        for a in string:
                string1 = string1 + a + examp
        return string1 
