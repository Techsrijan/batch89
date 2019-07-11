'''the format is;
\033[  Escape code, this is always the same
1 = Style, 1 for normal.
32 = Text colour, 32 for bright green.
40m = Background colour, 40 is for black.'''

'''
This table shows some of the available formats;
TEXT COLOR	CODE	   TEXT STYLE	CODE	BACKGROUND COLOR	CODE
Black	    30	        No effect	0	      Black	            40
Red	        31	        Bold	    1	      Red	            41
Green	    32	        Underline	2	      Green	            42
Yellow	    33	        Negative1	3	      Yellow        	43
Blue	    34	        Negative2	5	       Blue	            44
Purple	    35			                       Purple	        45
Cyan	    36			                        Cyan	        46
White	    37		                         	White	        47'''''

print('Training at Techsrijan Consultancy services Pvt Limited')

print("\033[1;31;40m Hello, I'm Vishal  ")
print("\033[3;32;40m Hello, I'm not a good guy !!  ")



st="Techsrijan, Consultancy, services ,Pvt Limited"
#print(st)

"""print(st.capitalize())
print(st.title()) # every first charater of word will be in capital
print(st.upper())
print(st.lower())
print(len(st))
print(st.split(","))
st2="welcome in Python in india"
print(st2.count('in'))
print(st2.find('in'))  #index
print(st2.endswith('ae'))

name= input("enter your name")
print(name,"hello")
#print(name.strip(),"hello")
#print(name.lstrip(),"hello")
print(name.rstrip(),"hello")

print(name.islower())
print(name.isupper())
print(name.isdigit())
print(name.swapcase())
name2= "Her name is Tamanna and an Tamanna is Good girl"
print(name2.replace("Tamanna","Sonia"))

st3="1232556"
print(st3.isdigit())
print(st3.isalpha())

st4="ffsdf3213+"
print(st4.isalnum())"""

name = input("Enter your Sentence : ")
capital=small=space = 0
for i in name:
    if i.isupper():
        capital += 1
    elif i.islower():
        small += 1
    else:
        space += 1

print("No. of Capital letters is : {}\nNo. of small letters is : {}\nNo. of total spaces is : {}".format(capital,small,space))
