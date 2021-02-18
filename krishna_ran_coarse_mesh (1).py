#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# for conduction
deltaTime = 0.5 #time step
deltaThickness=0.002  # in metres
K = 28 #thermal Conductivity of the material(W/mK)
rho = 8050 #density of the material (kg/m3)
C = 0.47 # specific heat capacity of the material (J/kgK)
g = 0.487 # Volumetric rate of the internal heat generation (W/m3)

# for convection
U  = 0.05 # flow speed
L = 0.01 #charcteristic length
rhoAir = 1.225 # density  of fluid kg/m3
Mu = 1 # Dynamic 
h = 0.5 #heat transfer coefficient W/m2k


# In[4]:


alpha = K/(rho*C) # thermal diffusivity (m2/sec)
print(alpha)
FourierNum = (alpha*deltaTime)/(deltaThickness**2) # fourier number
print(FourierNum)

HeatGenerationTerm = (g*alpha*deltaTime)/K
print(HeatGenerationTerm)

Nu = Mu/rhoAir # kinematic viscosity of fluid

#Pr = Nu/alpha # prandlt Number
Pr=0.7
print(Pr)
Re = (U*L)/Nu # reynolds number
#Re=10000
print(Re)
Pe = Re * Pr # Peclet Number
print(Pe)
Bi = (h*deltaThickness)/K
print(Bi)


# In[ ]:



    


# In[ ]:





# In[ ]:


# import itertools
from itertools import combinations_with_replacement
from itertools import product
f= open("output1.txt","a")
solid = ["a","b","d","e","f","g","l","h"] # colours for battery tempertures
fluid = ["c","o","p","q","r","s","i"] # colours for fluid temperatures
all_colours = ["a","b","d","e","l","f","g","c","o","p","q","r","s","i","h"]
tempeatures = [0,20,40,80,100,130,180,20,40,60,80,100,130,180,0]
Dictionary = dict()
for i in range(len(all_colours)):
    Dictionary[all_colours[i]]=tempeatures[i]
boundary_condition_combinations = ["a","b","d","e","f","g","c","o","p","q","r","s","i","l","h"]
comb = [p for p in itertools.product(boundary_condition_combinations, repeat = 5)]
for i in comb:
    if(i[0] == "a"):
      #  for j in i:
        print(','.join(str(s) for s in i), end=",", file=f)
        print("a", file = f)
    elif(i[0] == "h"):
      #  for j in i:
        print(','.join(str(s) for s in i), end=",", file=f)
        print("h", file=f)    
    elif(i[0] in solid):
        Solid_neighbour = 0
        for k in range(1,5):
            if(i[k] in solid):
                Solid_neighbour += 1
        if(Solid_neighbour == 4 ):
            ResultantTemperature = Dictionary.get(i[0]) + FourierNum *(Dictionary.get(i[1])+Dictionary.get(i[2])+Dictionary.get(i[3])+Dictionary.get(i[1])-4*Dictionary.get(i[0]))+HeatGenerationTerm
            
            print(','.join(str(s) for s in i), end=",", file=f)
            if (ResultantTemperature > 20) & (ResultantTemperature <= 40):    # b color for 21-40
                 print("b", file=f)
            elif (ResultantTemperature > 40) & (ResultantTemperature <= 80):    # d color for 41-80
                print("d", file=f)
            elif (ResultantTemperature > 80) & (ResultantTemperature <= 100):    # yellow color for 81-100
                print("e", file=f)
            elif (ResultantTemperature > 100) & (ResultantTemperature <= 130):   # orange color for 101-130
                print("l", file=f)
            elif (ResultantTemperature > 130) & (ResultantTemperature <= 180):   # orange color for 131-180
                print("f", file=f)
            else:                             # red color for >180
                print("g", file=f)  
        elif(Solid_neighbour == 3):
            for k in range(1,5):
                if(i[k] in fluid):
                    fluidindex = k
                    if(k == 1):
                        fluidpos = 1 
                        fluidopp=3 
                        fluidright= 2 
                        fluidleft = 4
                    elif(k == 2):
                        fluidpos = 2 
                        fluidopp=4
                        fluidright= 3  
                        fluidleft = 1
                    elif(k==3):
                        fluidpos = 3 
                        fluidopp=1 
                        fluidright= 4 
                        fluidleft = 2
                    elif(k==4):
                        fluidpos = 4 
                        fluidopp=2 
                        fluidright= 1 
                        fluidleft = 3
                        
            ResultantTemperature = FourierNum*((2*Bi*(Dictionary.get(i[fluidpos])+273))+(2*(Dictionary.get(i[fluidopp])+273))+(Dictionary.get(i[fluidright])+273)+(Dictionary.get(i[fluidopp])+273)+((Dictionary.get(i[0])+273)*((1/FourierNum)-2*Bi-4)))
            print(','.join(str(s) for s in i), end=",", file=f)
            if (ResultantTemperature > (20+273)) & (ResultantTemperature <= (40+273)):    # b color for 21-40
                print("b", file=f)
            elif (ResultantTemperature > (40+273)) & (ResultantTemperature <= (80+273)):    # o color for 41-60
                print("d", file=f)  
            elif (ResultantTemperature > (80+273)) & (ResultantTemperature <= (100+273)):    # q color for 81-100
                print("e", file=f)
            elif (ResultantTemperature > (100+273)) & (ResultantTemperature <= (130+273)):   # orange color for 101-130
                print("l", file=f)
            elif (ResultantTemperature > (130+273)) & (ResultantTemperature <= (180+273)):   # orange color for 131-180
                print("f", file=f)
            else:                             # red color for >180
                print("g", file=f)  
        elif(Solid_neighbour == 2):
            fluid_pos_list = []
            solid_pos_list = []
            
            for z in range(1,5):
                if(i[z] in fluid):
                    fluid_pos_list.append(z)
                else:
                    solid_pos_list.append(z)
            ResultantTemperature = 2*FourierNum*((Bi*(Dictionary.get(i[fluid_pos_list[0]])+273))+(Bi*(Dictionary.get(i[fluid_pos_list[1]])+273))+(Dictionary.get(i[solid_pos_list[0]])+273)+(Dictionary.get(i[solid_pos_list[1]])+273)+((Dictionary.get(i[0])+273)*((1/2*FourierNum)-2*Bi-2)))       
            print(','.join(str(s) for s in i), end=",", file=f)
            if (ResultantTemperature > (20+273)) & (ResultantTemperature <= (40+273)):    # b color for 21-40
                print("b", file=f)
            elif (ResultantTemperature > (40+273)) & (ResultantTemperature <= (80+273)):    # o color for 41-60
                print("d", file=f)  
            elif (ResultantTemperature > (80+273)) & (ResultantTemperature <= (100+273)):    # q color for 81-100
                print("e", file=f)
            elif (ResultantTemperature > (100+273)) & (ResultantTemperature <= (130+273)):   # orange color for 101-130
                print("l", file=f)
            elif (ResultantTemperature > (130+273)) & (ResultantTemperature <= (180+273)):   # orange color for 131-180
                print("f", file=f)
            else:                             # red color for >180
                print("g", file=f)  
    elif(i[0] in fluid):
        fluid_neighbour = 0
        for k in range(1,5):
            if(i[k] in fluid):
                fluid_neighbour += 1
        if(fluid_neighbour == 4):
            ResultantTemperature = Dictionary.get(i[0]) + (deltaTime/(Pe*(deltaThickness**2)))*(Dictionary.get(i[1])+Dictionary.get(i[2])+Dictionary.get(i[3])+Dictionary.get(i[4])-4*Dictionary.get(i[0]))
            print(','.join(str(s) for s in i), end=",", file=f)
            if (ResultantTemperature > 20) & (ResultantTemperature <= 40):    # b color for 21-40
                print("c", file=f)
            elif (ResultantTemperature > 40) & (ResultantTemperature <= 60):    # o color for 41-60
                print("o", file=f)
            elif (ResultantTemperature > 60) & (ResultantTemperature <= 80):    # p color for 61-80
                print("p", file=f)  
            elif (ResultantTemperature > 80) & (ResultantTemperature <= 100):    # q color for 81-100
                print("q", file=f)
            elif (ResultantTemperature > 100) & (ResultantTemperature <= 130):   # orange color for 101-130
                print("r", file=f)
            elif (ResultantTemperature > 130) & (ResultantTemperature <= 180):   # orange color for 131-180
                print("s", file=f)
            else:                             # red color for >180
                print("i", file=f)
        elif(fluid_neighbour == 3 or fluid_neighbour == 2 ):
            for t in range(1,5):
                if(i[t] in solid):
                    sol_index = t
            ResultantTemperature = Dictionary.get(i[t])
            print(','.join(str(s) for s in i), end=",", file=f)
            if (ResultantTemperature > 20) & (ResultantTemperature <= 40):    # b color for 21-40
                print("c", file=f)
            elif (ResultantTemperature > 40) & (ResultantTemperature <= 60):    # o color for 41-60
                print("o", file=f)
            elif (ResultantTemperature > 60) & (ResultantTemperature <= 80):    # p color for 61-80
                print("p", file=f)  
            elif (ResultantTemperature > 80) & (ResultantTemperature <= 100):    # q color for 81-100
                print("q", file=f)
            elif (ResultantTemperature > 100) & (ResultantTemperature <= 130):   # orange color for 101-130
                print("r", file=f)
            elif (ResultantTemperature > 130) & (ResultantTemperature <= 180):   # orange color for 131-180
                print("s", file=f)
            else:                             # red color for >180
                print("i", file=f)
        #f.append("/r/n")
       
            
    
    

    
    


# In[ ]:


print("Hello stackoverflow!", file=open("output.txt", "a"))


# In[ ]:





# In[ ]:




