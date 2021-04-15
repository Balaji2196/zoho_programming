inp=input("enter string")
len_inp=len(inp)
#print(len_inp)
middle_term=len_inp//2
#print(inp[middle_term])
mid_char=inp[middle_term]
split_words=inp.split(mid_char)
#print(split_words)
#print(len(split_words[0]))
#print(len(split_words[1]))

#print(mid_char)
txt=''
mid=[mid_char]
for i in range(len(split_words[1])):
    txt1='{}'.format(split_words[1][i])
    txt=txt+txt1
    txt2=mid_char+txt
    print(txt2.rjust(len(inp)))


txt_f=''
for j in range(len(split_words[0])):
    txt3='{}'.format(split_words[0][j])
    #print(txt3)
    txt_f=txt_f+txt3
    txt_ff=txt2+txt_f
    print(txt_ff.rjust(len(inp)))
