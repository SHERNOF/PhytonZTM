import xlwings as xw




# --------------- Interface ----------------------------------------------- #

# from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

# --------------- Interface ----------------------------------------------- #




# wb = xw.books.open(r"/Volumes/DDrive/PhytonZTM/Tex\ At\ Site\ Thread\ Gage\ Worksheet.xlsm")
# wb = xw.books.open(r"C:\Tex Onsite\Tex_reff\Tex At Site Thread Gage Worksheet.xlsm")
# wb = xw.books.open(r"/Volumes/DDrive/PhytonZTM/Tex At Site Thread Gage Worksheet.xlsm")
wb = xw.books.open(r'C:\SHERNOF\PhytonZTM\Tex At Site Thread Gage Worksheet.xlsm')
td = wb.sheets("Test Data")
vr = wb.sheets("Variables")


def float_range(start, stop, step):  
  while start < stop:
      yield round(start, 1)
      start += step
      
deviation_table = [
        [range(24, 51),{'du':3},{'dl':-3}, {'worn':-8},{'mu':6},{'ml':-6}],
        [range(51, 81),{'du':6},{'dl':-1}, {'worn':-7},{'mu':9},{'ml':-5}],
        [range(81, 126),{'du':11},{'dl':2}, {'worn':-6},{'mu':15},{'ml':-3}],
        [range(126, 201),{'du':18},{'dl':6}, {'worn':-5},{'mu':23},{'ml':1}],
        [range(201, 316),{'du':23},{'dl':9}, {'worn':-5},{'mu':30},{'ml':2}],
        [range(316, 501),{'du':33},{'dl':15}, {'worn':-3},{'mu':42},{'ml':6}],
        [range(501, 671),{'du':43},{'dl':21}, {'worn':-1},{'mu':54},{'ml':10}],
        ]

deviation_table_nogo = [
        [range(24, 51),{'du':6},{'dl':0}, {'worn':-3},{'mu':9},{'ml':-3}],
        [range(51, 81),{'du':7},{'dl':0}, {'worn':-4},{'mu':10},{'ml':-4}],
        [range(81, 126),{'du':9},{'dl':0}, {'worn':-5},{'mu':13},{'ml':-5}],
        [range(126, 201),{'du':11},{'dl':0}, {'worn':-6},{'mu':16},{'ml':-6}],
        [range(201, 316),{'du':14},{'dl':0}, {'worn':-8},{'mu':21},{'ml':-7}],
        [range(316, 501),{'du':18},{'dl':0}, {'worn':-10},{'mu':27},{'ml':-9}],
        [range(501, 671),{'du':22},{'dl':0}, {'worn':-12},{'mu':33},{'ml':-11}],
        ]



three_fourth_p =[
    [{'p':0.20},(0.13)],
    [{'p':0.25},(0.162)],
    [{'p':0.30},(0.195)],
    [{'p':0.35},(0.227)],
    [{'p':0.40},(0.26)],
    [{'p':0.45},(0.292)],
    [{'p':0.50},(0.325)],
    [{'p':0.55},(0.39)],
    [{'p':0.60},(0.455)],
    [{'p':0.65},(0.487)],
    [{'p':0.70},(0.52)],
    [{'p':0.75},(0.65)],
    [{'p':0.80},(0.812)],
    [{'p':1.0},(0.974)],
    [{'p':1.25},(1.137)],
    [{'p':1.50},(1.3)],
    [{'p':1.75},(1.624)],
    [{'p':2.0},(1.95)],
    [{'p':2.5},(2.273)],
    [{'p':3.0},(2.598)],
    [{'p':3.5},(2.923)],
    [{'p':4.0},(3.25)],
    [{'p':4.5},(3.572)],
    [{'p':5.0},(3.897)],
]


tolerance_table = [
        [float_range(0.99,1.44,0.01),{'pd':0.2},{'4':40,'5':'','6':'','7':'','8':''}],
        [float_range(0.99,1.44,0.01),{'pd':0.25},{'4':45,'5':56,'6':'','7':'','8':''}],
        [float_range(0.99,1.44,0.01),{'pd':0.3},{'4':48,'5':60,'6':75,'7':'','8':''}],
        
        [float_range(1.4,2.8,0.1),{'pd':0.2},{'4':42,'5':'','6':'','7':'','8':''}],
        [float_range(1.4,2.8,0.1),{'pd':0.25},{'4':48,'5':60,'6':'','7':'','8':''}],
        [float_range(1.4,2.8,0.1),{'pd':0.35},{'4':53,'5':67,'6':85,'7':'','8':''}],
        [float_range(1.4,2.8,0.1),{'pd':0.4},{'4':56,'5':71,'6':90,'7':'','8':''}],
        [float_range(1.4,2.8,0.1),{'pd':0.45},{'4':60,'5':75,'6':95,'7':'','8':''}],
        
        [float_range(2.8,5.6,0.1),{'pd':0.35},{'4':56,'5':71,'6':90,'7':'','8':''}],
        [float_range(2.8,5.6,0.1),{'pd':0.5},{'4':63,'5':80,'6':100,'7':125,'8':''}],
        [float_range(2.8,5.6,0.1),{'pd':0.6},{'4':71,'5':90,'6':112,'7':140,'8':''}],
        [float_range(2.8,5.6,0.1),{'pd':0.7},{'4':75,'5':95,'6':118,'7':150,'8':''}],
        [float_range(2.8,5.6,0.1),{'pd':0.75},{'4':75,'5':95,'6':118,'7':150,'8':''}],
        [float_range(2.8,5.6,0.1),{'pd':0.8},{'4':80,'5':100,'6':125,'7':160,'8':200}],
        
        [float_range(5.6,11.2,0.1),{'pd':0.75},{'4':85,'5':106,'6':132,'7':170,'8':''}],
        [float_range(5.6,11.2,0.1),{'pd':1},{'4':95,'5':118,'6':150,'7':190,'8':236}],
        [float_range(5.6,11.2,0.1),{'pd':1.25},{'4':100,'5':125,'6':160,'7':200,'8':250}],
        [float_range(5.6,11.2,0.1),{'pd':1.5},{'4':112,'5':140,'6':180,'7':224,'8':280}],
        
        [float_range(11.2,22.4,0.1),{'pd':1},{'4':100,'5':125,'6':160,'7':200,'8':250}],
        [float_range(11.2,22.4,0.1),{'pd':1.25},{'4':112,'5':140,'6':180,'7':224,'8':280}],
        [float_range(11.2,22.4,0.1),{'pd':1.5},{'4':118,'5':150,'6':190,'7':236,'8':300}],
        [float_range(11.2,22.4,0.1),{'pd':1.75},{'4':125,'5':160,'6':200,'7':250,'8':315}],
        [float_range(11.2,22.4,0.1),{'pd':2},{'4':132,'5':170,'6':212,'7':265,'8':335}],
        [float_range(11.2,22.4,0.1),{'pd':2.5},{'4':140,'5':180,'6':224,'7':280,'8':355}],
        
        [float_range(22.4,45,0.1),{'pd':1},{'4':106,'5':132,'6':170,'7':212,'8':''}],
        [float_range(22.4,45,0.1),{'pd':1.5},{'4':125,'5':160,'6':200,'7':250,'8':315}],
        [float_range(22.4,45,0.1),{'pd':2},{'4':140,'5':180,'6':224,'7':280,'8':355}],
        [float_range(22.4,45,0.1),{'pd':3},{'4':170,'5':212,'6':265,'7':335,'8':425}],
        [float_range(22.4,45,0.1),{'pd':3.5},{'4':180,'5':224,'6':280,'7':355,'8':450}],
        [float_range(22.4,45,0.1),{'pd':4},{'4':190,'5':236,'6':300,'7':375,'8':475}],
        [float_range(22.4,45,0.1),{'pd':4.5},{'4':200,'5':250,'6':315,'7':400,'8':500}],
        
        [range(45,90),{'pd':1.5},{'4':132,'5':170,'6':212,'7':265,'8':335}],
        [range(45,90),{'pd':2},{'4':150,'5':190,'6':236,'7':300,'8':375}],
        [range(45,90),{'pd':3},{'4':180,'5':224,'6':280,'7':355,'8':450}],
        [range(45,90),{'pd':4},{'4':200,'5':250,'6':315,'7':400,'8':500}],
        [range(45,90),{'pd':5},{'4':212,'5':265,'6':335,'7':425,'8':530}],
        [range(45,90),{'pd':5.5},{'4':224,'5':280,'6':355,'7':450,'8':560}],
        [range(45,90),{'pd':6},{'4':236,'5':300,'6':375,'7':475,'8':600}],
        
        [range(90,180),{'4':160,'5':200,'6':250,'7':315,'8':400}],
        [range(90,180),{'pd':3},{'4':190,'5':236,'6':300,'7':375,'8':475}],
        [range(90,180),{'pd':4},{'4':212,'5':265,'6':335,'7':425,'8':530}],                                                   
        [range(90,180),{'pd':6},{'4':250,'5':315,'6':400,'7':500,'8':630}],
        
        [range(180,355),{'pd':3},{'4':212,'5':265,'6':335,'7':425,'8':530}],
        [range(180,355),{'pd':4},{'4':236,'5':300,'6':375,'7':475,'8':600}],
        [range(180,355),{'pd':6},{'4':265,'5':355,'6':425,'7':530,'8':670}],                                           
        ]


def my_tolerance(): 
    found = False
    model = td.range('D11').value
    x = model.index('X')
    dsh = model.index('-')
    # print(x)
    # print(dsh)
    dia = int(model[1:x])
    # print(dia)
    pd = float(model[x + 1:dsh])
    # print(type(pd))
    tol = str(model[dsh + 1])
    # print(tol)
    gauge = model[len(model)-1:len(model)]
    # print(gauge)
    
    for i in tolerance_table:
        if dia in i[0]:
            if pd in i[1].values():
                if tol in i[2]:
                    # print(i[2].get(tol))
                    # vr.range('AF5').value = i[2].get(tol) #getting the value using the key
                    tolerance = i[2].get(tol)
                    
                    
    for i, rng in enumerate(deviation_table):
        # print(tolerance)
        if tolerance in rng[0]:
            print('yes')
            
            vr.range('AG5').value = i
        


my_tolerance()
    
        
    
    

