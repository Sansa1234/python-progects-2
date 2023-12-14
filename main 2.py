print("les devoir")
physic = float(input("physic"))
sience = float(input("sience"))
islam = float(input("islam"))
math = float(input("math"))
technologie = float(input("technologie"))
arab = float(input("arab"))
english = float(input("english"))
french = float(input("french"))
geo_hist = float(input("geo_hist"))
paint = float(input("paint"))
sports = float(input("sport"))
computer = float(input("computer"))
print("les devoir 2")
physic2 = float(input("physic"))
sience2 = float(input("sience"))
math2 = float(input("math"))
print("ta9wim")
physic_dev = float(input("physic"))
sience_dev = float(input("sience"))
islam_dev = float(input("islam"))
math_dev = float(input("math"))
technologie_dev = float(input("technologie"))
arab_dev = float(input("arab"))
english_dev = float(input("english"))
french_dev = float(input("french"))
geo_hist_dev = float(input("geo_hist"))
paint_dev = float(input("paint"))
sports_dev = float(input("sport"))
computer_dev = float(input("computer"))
print("examen")
physic_ex = float(input("physic"))
sience_ex = float(input("sience"))
islam_ex = float(input("islam"))
math_ex = float(input("math"))
technologie_ex = float(input("technologie"))
arab_ex = float(input("arab"))
english_ex = float(input("english"))
french_ex = float(input("french"))
geo_hist_ex = float(input("geo_hist"))
paint_ex = float(input("paint"))
sports_ex = float(input("sport"))
computer_ex = float(input("computer"))
print("a3mal_ta4bi9iya")
physic_3ml = float(input("physic"))
sience_3ml = float(input("sience"))
technologie_3ml = float(input("technologie"))
arab_3ml = float(input("arab"))
english_3ml = float(input("english"))
french_3ml = float(input("french"))
paint_3ml = float(input("paint"))
computer_3ml = float(input("computer"))

physic_VAL = 4
sience_VAL = 4
islam_VAL = 2
math_VAL = 5
technologie_VAL = 2
arab_VAL = 3
english_VAL = 2
french_VAL = 2
geo_hist_VAL = 2
paint_VAL = 1
sports_VAL = 1
computer_VAL = 2

physic_MO3 = (physic + physic2)/2
sience_MO3 = (sience + sience2)/2
islam_MO3 = islam
math_MO3 = (math + math2)/2
technologie_MO3 = technologie
arab_MO3 = arab
english_MO3 = english
french_MO3 = french
geo_hist_MO3 = geo_hist
paint_MO3 = paint
sports_MO3 = sports
computer_MO3 = computer

physic_examf = physic_ex*2
sience_examf = sience_ex*2
islam_examf = islam_ex*2
math_examf = math_ex*2
technologie_examf = technologie_ex*2
arab_examf = arab_ex*2
english_examf = english_ex*2
french_examf = french_ex*2
geo_hist_examf = geo_hist_ex*2
paint_examf = paint_ex*2
sports_examf = sports_ex*2
computer_examf = computer_ex*2


physic_target = ((physic_dev + physic_3ml + physic_MO3 + physic_examf)/5)*physic_VAL
sience_target = ((sience_dev + sience_3ml + sience_MO3 + sience_examf)/5)*sience_VAL
islam_target = ((islam_dev + islam_MO3 + islam_examf)/4)*islam_VAL
math_target = ((math_dev + math_MO3 + math_examf)/4)*math_VAL
technologie_target = ((technologie_dev + technologie_3ml + technologie_MO3 + technologie_examf)/5)*technologie_VAL
arab_target = ((arab_dev + arab_3ml + arab_MO3 + arab_examf)/5)*arab_VAL
english_target = ((english_dev + english_3ml + english_MO3 + english_examf)/5)*english_VAL
french_target = ((french_dev + french_3ml + french_MO3 + french_examf)/5)*french_VAL
geo_hist_target = ((geo_hist_dev + geo_hist_MO3 + geo_hist_examf)/4)*geo_hist_VAL
paint_target = ((paint_dev + paint_3ml + paint_MO3 + paint_examf)/5)*paint_VAL
sports_target = ((sports_dev + sports_MO3 + sports_examf)/4)*sports_VAL
computer_target = ((computer_dev + computer_3ml + computer_MO3 + computer_examf)/5)*computer_VAL

total_mo3 = 30

mo3adal = (physic_target + sience_target + islam_target + math_target + technologie_target + arab_target + english_target + french_target + geo_hist_target + paint_target + sports_target + computer_target)/total_mo3
mo3adal_fix = round(mo3adal, 2)
print("your ma3adal is: " + str(mo3adal_fix))
