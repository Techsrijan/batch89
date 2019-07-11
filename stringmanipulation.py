st="Techsrijan, Consultancy, services ,Pvt Limited"
print(st)

print(st.capitalize())
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
print(st4.isalnum())


