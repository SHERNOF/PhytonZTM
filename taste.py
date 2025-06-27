import xlwings as xw
wb = xw.books.open(r"C:\Tex Onsite\Tex_reff\Tex At Site Thread Gage Worksheet.xlsm")
sh = wb.sheets("Variables")


def float_range(start, stop, step):  
  while start < stop:
      yield round(start, 1)
      start += step

deviation_table = [
        range(24, 51),
        range(51, 81),
        range(81, 126),
        range(126, 201),
        range(201, 316),
        range(316, 501),
        range(501, 671),
        ]


tolerance_table = [
        # [float_range(0.99,1.44,0.01),{'pd':0.2},{'4':40,'5':'','6':'','7':'','8':''}], 'catherine's sample
        [float_range(sh.range("Q44").value,sh.range("R44").value,0.01),{'pd':0.2},{'4':40,'5':'','6':'','7':'','8':''}],
        [float_range(sh.range("Q45").value,sh.range("R45").value,0.01),{'pd':0.25},{'4':45,'5':56,'6':'','7':'','8':''}],
        [float_range(sh.range("Q46").value,sh.range("R46").value,0.01),{'pd':0.3},{'4':48,'5':60,'6':75,'7':'','8':''}],
        [float_range(sh.range("Q47").value,sh.range("R47").value,0.1),{'pd':0.2},{'4':42,'5':'','6':'','7':'','8':''}],
        [float_range(sh.range("Q48").value,sh.range("R48").value,0.1),{'pd':0.25},{'4':48,'5':60,'6':'','7':'','8':''}],
        [float_range(sh.range("Q49").value,sh.range("R49").value,0.1),{'pd':0.35},{'4':53,'5':67,'6':85,'7':'','8':''}],
        [float_range(sh.range("Q50").value,sh.range("R50").value,0.1),{'pd':0.4},{'4':56,'5':71,'6':90,'7':'','8':''}],
        [float_range(sh.range("Q51").value,sh.range("R51").value,0.1),{'pd':0.45},{'4':60,'5':75,'6':95,'7':'','8':''}],
        [float_range(sh.range("Q52").value,sh.range("R52").value,0.1),{'pd':0.35},{'4':56,'5':71,'6':90,'7':'','8':''}],
        [float_range(sh.range("Q53").value,sh.range("R53").value,0.1),{'pd':0.5},{'4':63,'5':80,'6':100,'7':125,'8':''}],
        [float_range(sh.range("Q54").value,sh.range("R54").value,0.1),{'pd':0.6},{'4':71,'5':90,'6':112,'7':140,'8':''}],
        [float_range(sh.range("Q55").value,sh.range("R55").value,0.1),{'pd':0.7},{'4':75,'5':95,'6':118,'7':150,'8':''}],
        [float_range(sh.range("Q56").value,sh.range("R56").value,0.1),{'pd':0.75},{'4':75,'5':95,'6':118,'7':150,'8':''}],
        [float_range(sh.range("Q57").value,sh.range("R57").value,0.1),{'pd':0.8},{'4':80,'5':100,'6':125,'7':160,'8':200}],
        [float_range(sh.range("Q58").value,sh.range("R58").value,0.1),{'pd':0.75},{'4':85,'5':106,'6':132,'7':170,'8':''}],
        [float_range(sh.range("Q59").value,sh.range("R59").value,0.1),{'pd':1},{'4':95,'5':118,'6':150,'7':190,'8':236}],
        [float_range(sh.range("Q60").value,sh.range("R60").value,0.1),{'pd':1.25},{'4':100,'5':125,'6':160,'7':200,'8':250}],
        [float_range(sh.range("Q61").value,sh.range("R61").value,0.1),{'pd':1.5},{'4':112,'5':140,'6':180,'7':224,'8':280}],
        [float_range(sh.range("Q62").value,sh.range("R62").value,0.1),{'pd':1},{'4':100,'5':125,'6':160,'7':200,'8':250}],
        [float_range(sh.range("Q63").value,sh.range("R63").value,0.1),{'pd':1.25},{'4':112,'5':140,'6':180,'7':224,'8':280}],
        [float_range(sh.range("Q64").value,sh.range("R64").value,0.1),{'pd':1.5},{'4':118,'5':150,'6':190,'7':236,'8':300}],
        [float_range(sh.range("Q65").value,sh.range("R65").value,0.1),{'pd':1.75},{'4':125,'5':160,'6':200,'7':250,'8':315}],
        [float_range(sh.range("Q66").value,sh.range("R66").value,0.1),{'pd':2},{'4':132,'5':170,'6':212,'7':265,'8':335}],
        [float_range(sh.range("Q67").value,sh.range("R67").value,0.1),{'pd':2.5},{'4':140,'5':180,'6':224,'7':280,'8':355}],
        [float_range(sh.range("Q68").value,sh.range("R68").value,0.1),{'pd':1},{'4':106,'5':132,'6':170,'7':212,'8':''}],
        [float_range(sh.range("Q69").value,sh.range("R69").value,0.1),{'pd':1.5},{'4':125,'5':160,'6':200,'7':250,'8':315}],
        [float_range(sh.range("Q70").value,sh.range("R70").value,0.1),{'pd':2},{'4':140,'5':180,'6':224,'7':280,'8':355}],
        [float_range(sh.range("Q71").value,sh.range("R71").value,0.1),{'pd':3},{'4':170,'5':212,'6':265,'7':335,'8':425}],
        [float_range(sh.range("Q72").value,sh.range("R72").value,0.1),{'pd':3.5},{'4':180,'5':224,'6':280,'7':355,'8':450}],
        [float_range(sh.range("Q73").value,sh.range("R73").value,0.1),{'pd':4},{'4':190,'5':236,'6':300,'7':375,'8':475}],
        [float_range(sh.range("Q74").value,sh.range("R74").value,0.1),{'pd':4.5},{'4':200,'5':250,'6':315,'7':400,'8':500}],
        [float_range(sh.range("Q75").value,sh.range("R75").value,0.1),{'pd':1.5},{'4':132,'5':170,'6':212,'7':265,'8':335}],
        [float_range(sh.range("Q76").value,sh.range("R76").value,0.1),{'pd':2},{'4':150,'5':190,'6':236,'7':300,'8':375}],
        [float_range(sh.range("Q77").value,sh.range("R77").value,0.1),{'pd':3},{'4':180,'5':224,'6':280,'7':355,'8':450}],
        [float_range(sh.range("Q78").value,sh.range("R78").value,0.1),{'pd':4},{'4':200,'5':250,'6':315,'7':400,'8':500}],
        [float_range(sh.range("Q79").value,sh.range("R79").value,0.1),{'pd':5},{'4':212,'5':265,'6':335,'7':425,'8':530}],
        [float_range(sh.range("Q80").value,sh.range("R80").value,0.1),{'pd':5.5},{'4':224,'5':280,'6':355,'7':450,'8':560}],
        [float_range(sh.range("Q81").value,sh.range("R81").value,0.1),{'pd':6},{'4':236,'5':300,'6':375,'7':475,'8':600}],
        [float_range(sh.range("Q82").value,sh.range("R82").value,0.1),{'pd':2},{'4':160,'5':200,'6':250,'7':315,'8':400}],
        [float_range(sh.range("Q83").value,sh.range("R83").value,0.1),{'pd':3},{'4':190,'5':236,'6':300,'7':375,'8':475}],
        [float_range(sh.range("Q84").value,sh.range("R84").value,0.1),{'pd':4},{'4':212,'5':265,'6':335,'7':425,'8':530}],                                                   
        [float_range(sh.range("Q85").value,sh.range("R85").value,0.1),{'pd':6},{'4':250,'5':315,'6':400,'7':500,'8':630}],
        [float_range(sh.range("Q86").value,sh.range("R86").value,0.1),{'pd':3},{'4':212,'5':265,'6':335,'7':425,'8':530}],
        [float_range(sh.range("Q87").value,sh.range("R87").value,0.1),{'pd':4},{'4':236,'5':300,'6':375,'7':475,'8':600}],
        [float_range(sh.range("Q88").value,sh.range("R88").value,0.1),{'pd':6},{'4':265,'5':355,'6':425,'7':530,'8':670}],                                           
        ]

def get_tolerance():
     tg = str(sh.range("Q7").value)
     dia = int(sh.range("Q5").value)
     pd = float(sh.range("Q6").value)
     fo = False
     for item in tolerance_table:
         
         if dia in item[0]:  
             fo = True
             if pd in item[1].values():
                 fo = True 
                 if tg in item[2]:
                     fo = True
                     sh.range('R5').value = item[2].get(tg)
                 else:
                    fo=False
                    sh.range('A3').value = fo

def tolerance_index():
    tolerance = int(sh.range("R5").value)
    for i, rng in enumerate(deviation_table):
        if tolerance in rng:
            sh.range('S5').value = i
            if tolerance not in rng:
                print('Tolerance {tolerance} not found in any range')

get_tolerance()
tolerance_index()

'''
- the get_tolerance() and tolerance_index() are the functions to retrieve the tolerance of the given thread gage. once tolerance is known
  it needs not to define the index to be use in getting the different specs like the Devation, worn, major and minor diameter tolerances.
- The ranges from 4.2 are converted from float to integer by using the integer generator using the float_range()
- it was decided to put the table hard coded in this file to maintain integrity of the specs 
- issue was found when getting the index in tolerance_index() due to a typo error in a range of the deviation_table. this was fixed by using the enumerate() function which is a function to get and display the index and a value.

'''





# def tol_ind():
#     tolerance = int(sh.range("A2").value)
#     in_range = False
#     print(tolerance)
#     for item in deviation_table:
#         # print(item)
#         if tolerance in item:
#             # print('Yses')
#             print(item.index(tolerance))
   

# tolerance_index()

# deviation_table = [
#         float_range(sh.range("Q18").value,sh.range("R18").value),
#         float_range(sh.range("Q19").value,sh.range("R19").value),
#         float_range(sh.range("Q20").value,sh.range("R20").value),
#         float_range(sh.range("Q21").value,sh.range("R21").value),
#         float_range(sh.range("Q22").value,sh.range("R22").value),
#         float_range(sh.range("Q23").value,sh.range("R23").value),
#         float_range(sh.range("Q24").value,sh.range("R24").value),
#         ]
