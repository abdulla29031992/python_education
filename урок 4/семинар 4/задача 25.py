# Задача 25. Напишите программу, которая принимает на вход строку, и отслеживает, 
# сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

#  variant 1

# str1 = 'a a a b c a a d c d d'
# a = ''
# str1 = str1.split(' ')

# for i in str1:
#     count1 = a.count(i)
#     print(count1)
#     if a.count(i) == 0:
#         a += i+' '
#     else:
#         a += i+'_'+str(count1)+' '
# print(a.strip())


# variant 2

def Get_Count_Letter (sp):
  sp1=sp.split()
  lib={}
  sp_out=[]
  for i in sp1:
    if i in lib:
      
      sp_out.append(i+"_"+str(lib[i]))
      lib [i]=lib[i]+1
    else:
      lib [i]=1
      sp_out.append(i)
  return sp_out    
  
sp="a a a b c a a d c d d"
print (Get_Count_Letter(sp))