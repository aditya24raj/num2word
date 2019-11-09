#number to word assets
n09=["0","1","2","3","4","5","6","7","8","9"]
w09=["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]

n10_19=["10","11","12","13","14","15","16","17","18","19"]
w10_19=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    
n20_90=["2","3","4","5","6","7","8","9"]
w20_90=["Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninty"]


#manually check asset for error
def asset_check_manual():
 for i in range(len(n09)):
	 print(n09[i],w09[i])
 for i in range(len(n10_19)):
	 print(n10_19[i],w10_19[i])
 for i in range(len(n20_90)):
	 print(n20_90[i]+"0",w20_90[i])
	 exit()

#all good in last check 14-10-19, 11:20pm
#asset_check_manual()

#take valid input, a max 9 digit p+ int
n=input("\nEnter A Number(Min 1, Max 9 Digits):\n")
try:
 n=int(n)
except ValueError:
  print("\ninvalid integer:",n)
  print("Try Again")
  exit()
       
n=str(n)
n_l=list(n)
if len(n_l)>9:
 print("Max 9 Digit Numbers Supported.")
 print(n,": Has",len(n_l),"Digits.")
 exit()
#print(n_l)
    
#length of num and array for word
    
index_range=len(n_l)
w_l=[""]*index_range


#define conversion

#unit place conversion
def unit():
	for i in range(len(n09)):
		if n09[i]==n_l[-1]:
			w_l[-1]=w09[i]

#tens place conversion
def tens():
	if n_l[-2]=="0":
		w_l[-2]=""
		unit()
		
	if n_l[-2]=="1":
		for i in range(len(n10_19)):
			if n10_19[i]==n_l[-2]+n_l[-1]:
				w_l[-1]=w10_19[i]
				
	if n_l[-2]!="0" and n_l[-2]!="1":
		for i in range(len(n20_90)):
			if n20_90[i]==n_l[-2]:
				w_l[-2]=w20_90[i]
		unit()

#hundreds place conversion
def hundreds():
	if n_l[-3]=="0":
		w_l[-3]=""
		tens()
	else:
		for i in range(len(n09)):
			if n09[i]==n_l[-3]:
				 w_l[-3]=w09[i]+" Hundred "
		tens()
	
#thousands place conversion
def thousands():
	if n_l[-4]=="0":
		if index_range>4:
			if n_l[-5]!="0":
				w_l[-4]=" Thousand "
		else:
			w_l[-4]=""
			
		hundreds()
	else:
		for i in range(len(n09)):
			if n09[i]==n_l[-4]:
				w_l[-4]=w09[i]+" Thousand "
		hundreds()
		
#ten thousands place conversion
def ten_thousands():
	if n_l[-5]=="0":
		w_l[-5]=""
		thousands()
	
	if n_l[-5]=="1":
		for i in range(len(n10_19)):
			if n_l[-5]+n_l[-4]==n10_19[i]:
				w_l[-5]=w10_19[i]+" Thousand "
				w_l[-4]=""
		hundreds()
	
	if n_l[-5]!="1" and n_l[-5]!="0":
		for i in range(len(n20_90)):
			if n_l[-5]==n20_90[i]:
				w_l[-5]=w20_90[i]
		thousands()

#lakhs place conversion

def lakhs():
	if n_l[-6]=="0":
		if index_range>6:
			if n_l[-7]!="0":
				w_l[-6]=" Lakh "
		else:
			w_l[-6]=""
			
		ten_thousands()
	else:
		for i in range(len(n09)):
			if n_l[-6]==n09[i]:
				w_l[-6]=w09[i]+" Lakh "
		ten_thousands()
 
#ten lakhs place conversion

def ten_lakhs():
    if n_l[-7]=="0":
        w_l[-7]=""
        lakhs()
        
    if n_l[-7]=="1":
        for i in range(len(n10_19)):
            if n_l[-7]+n_l[-6]==n10_19[i]:
                w_l[-7]=w10_19[i]+" Lakh "
                w_l[-6]=""
        ten_thousands()
                
    if n_l[-7]!="1" and n_l[-7]!="0":
        for i in range(len(n20_90)):
            if n_l[-7]==n20_90[i]:
                w_l[-7]=w20_90[i]
        lakhs()


#crores place conversion

def crores():
    if n_l[-8]=="0":
        if index_range>8:
            if n_l[-9]!="0":
                w_l[-8]=" Crore "
            else:
                n_l[-8]=""
        ten_lakhs()
                
   
    else:
        for i in range(len(n09)):
            if n_l[-8]==n09[i]:
                w_l[-8]=w09[i]+" Crore "
        ten_lakhs()
        
#ten crore place conversion

def ten_crores():
    if n_l[-9]=="0":
        n_l[-9]=""
        crores()
    
    if n_l[-9]=="1":
        for i in range(len(n10_19)):
            if n_l[-9]+n_l[-8]==n10_19[i]:
                w_l[-9]=w10_19[i]+" Crore "
                w_l[-8]=""
        ten_lakhs()
    
    if n_l[-9]!="0" and n_l[-9]!="1":
        for i in range(len(n20_90)):
            if n_l[-9]==n20_90[i]:
                w_l[-9]=w20_90[i]
        crores()




#attempt conversion
if index_range==1:
    unit()
if index_range==2:
    tens()
if index_range==3:
    hundreds()
if index_range==4:
    thousands()
if index_range==5:
    ten_thousands()
if index_range==6:
    lakhs()
if index_range==7:
    ten_lakhs()
if index_range==8:
    crores()
if index_range==9:
    ten_crores()




#test point 

#print(n_l)
#print(w_l)




#print the output

consider0=True
print("\nIn Words:\n",end="")
for i in w_l:
    if consider0: 
        if i!="":
            print(i,end="")
            if i!="Zero":
                consider0=False
    else:
        if i!="" and i!="Zero":
            print(i,end="")
print("\n")
exit()

