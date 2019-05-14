import os
from tkinter import *
import time
import turtle

np = Tk()
np.title("Periodic Table")
np.maxsize(995,510)
np.minsize(995,510)
np.iconbitmap('logo_Ysw_icon.ico')

shells = 0
symb = ""
atmc = 0
Ad=0;Bd=0;Cd=0;Dd=0;Ed=0;Fd=0;Gd=0;

def drawConfig(shll,symbl,atmc,a,b,c,d,e,f,g):
    
    turtle.Turtle._screen = None
    turtle.TurtleScreen._RUNNING = True
    turtle.title("Electron configuration of: "+symb)
    
    vh = turtle.Turtle()
    vh.speed(0)
    Txxt = ("Georgia",20,"bold")
    TxxtS = ("Georgia",10,"bold")
    vh.ht()
    vh.write(symb,font=Txxt,align='center')
    vh.penup()
    vh.goto(-320,-280)
    vh.pendown()
    vh.color('green')
    vh.write("MahirTech MMXIX",font=TxxtS,align='left')
    vh.penup()

    vh.color('black')
    for shell in range (0,shells):
        vh.goto(0,(-20*shell)-40)
        vh.pendown()
        vh.circle((shell*20+60) )
        vh.penup()

    vh.width(2)
    vh.color('blue')
    for x in range(1,a+1):
        vh.penup()
        vh.goto(0,-40)
        vh.circle(60,x*(360/a))
        vh.pendown()
        vh.circle(10)
        vh.penup()
        vh.goto(0,0)
        vh.seth(0)
    for x in range(1,b+1):
        vh.penup()
        vh.goto(0,-60)
        vh.circle(80,x*(360/b))
        vh.pendown()
        vh.circle(10)
        vh.penup()
        vh.goto(0,0)
        vh.seth(0)
    for x in range(1,c+1):
        vh.penup()
        vh.goto(0,-80)
        vh.circle(100,x*(360/c))
        vh.pendown()
        vh.circle(10)
        vh.penup()
        vh.goto(0,0)
        vh.seth(0)
    for x in range(1,d+1):
        vh.penup()
        vh.goto(0,-100)
        vh.circle(120,x*(360/d))
        vh.pendown()
        vh.circle(10)
        vh.penup()
        vh.goto(0,0)
        vh.seth(0)
    for x in range(1,e+1):
        vh.penup()
        vh.goto(0,-120)
        vh.circle(140,x*(360/e))
        vh.pendown()
        vh.circle(10)
        vh.penup()
        vh.goto(0,0)
        vh.seth(0)
    for x in range(1,f+1):
        vh.penup()
        vh.goto(0,-140)
        vh.circle(160,x*(360/f))
        vh.pendown()
        vh.circle(10)
        vh.penup()
        vh.goto(0,0)
        vh.seth(0)
    for x in range(1,g+1):
        vh.penup()
        vh.goto(0,-160)
        vh.circle(180,x*(360/g))
        vh.pendown()
        vh.circle(10)
        vh.penup()
        vh.goto(0,0)
        vh.seth(0)

def search(D):
    global shells
    global symb
    global atmc
    global Ad;global Bd ;global Cd;global Dd;global Ed;global Fd;global Gd
    
    
    names = {"H":"Hydrogen","He":"Helium","Li":"Lithium","Be":"Beryllium",'B':'Boron','C':'Carbon',"N":"Nitrogen","O":"Oxygen","F":"Fluorine","Ne":"Neon","Na":"Sodium","Mg":"Magnesium","Al":"Aluminium","Si":"Silicon","P":"Phosphorous","S":"Sulphur","Cl":"Chlorine","Ar":"Argon","K":"Potassium","Ca":"Calcium","Sc":"Scandium","Ti":"Titanium","V":"Vanadium","Cr":"Chromium","Mn":"Manganese","Fe":"Iron",'Co':"Cobalt",'Ni':"Nickel",'Cu':"Copper",'Zn':"Zinc",'Ga':"Gallium",'Ge':"Germanium",'As':"Arsenic",'Se':"Selenium",'Br':"Bromine",'Kr':"Krypton",'Rb':"Rubidium",'Sr':"Strontium",'Y':"Yttrium",'Zr':"Zirconium",'Nb':"Niobium",'Mo':"Molybdenum",'Tc':"Technetium",'Ru':"Ruthenium",'Rh':"Rhodium",'Pd':"Palladium",'Ag':"Silver",'Cd':"Cadmium",'In':"Indium",'Sn':"Tin",'Sb':"Antimony",'Te':"Tellerium",'I':"Iodine",'Xe':"Xenon",'Cs':"Caesium",'Ba':"Barium",'La':"Lanthium",'Hf':"Hafnium",'Ta':"Tantalum",'W':"Tungsten",'Re':"Rhenium",'Os':"Osmium",'Ir':"Iridium",'Pt':"Platinum",'Au':"Gold",'Hg':"Mercury",'Tl':"Thallium",'Pb':"Lead",'Bi':"Bismuth",'Po':"Polonium",'At':"Astatine",'Rn':"Radon",'Fr':"Francium",'Ra':"Radium",'Ac':"Actinium",'Rf':"Rutherfordium",'Db':"Dubnium",'Sg':"Seaborgium",'Bh':"Bohrium",'Hs':"Hassium",'Mt':"Meitnerium",'Ds':"Darmstadtium",'Rg':"Roentgenium",'Cn':"Copernicium",'Nh':"Nihonium",'Fl':"Flerovium",'Mc':"Moscovium",'Lv':"Livermorium",'Ts':"Tennessine",'Og':"Oganesson",'Ce':"Cerium",'Pr':"Praesodynium",'Nd':"Neodynium",'Pm':"Promethium",'Sm':"Samarium",'Eu':"Europium",'Gd':"Gadolinium",'Tb':"Terbium",'Dy':"Dysporium",'Ho':"Holmium",'Er':"Erbium",'Tm':"Thulium",'Yb':"Ytterbium",'Lu':"Lutetium",'Th':"Thorium",'Pa':"Protactinium",'U':"Uranium",'Np':"Neptunium",'Pu':"Plutonium",'Am':"Americium",'Cm':"Calafornium",'Bk':"Berkelium",'Cf':"Calafornium",'Es':"Einsteinium",'Fm':"Fermium",'Md':"Mendelevium",'No':"Nobelium",'Lr':"Lawrencium",0:0,}
    ANumber = {0:0,"H":1,"He":2,"Li":3,"Be":4,'B':5,'C':6,"N":7,"O":8,"F":9,"Ne":10,"Na":11,"Mg":12,"Al":13,"Si":14,"P":15,"S":16,"Cl":17,"Ar":18,"K":19,"Ca":20,"Sc":21,"Ti":22,"V":23,"Cr":24,"Mn":25,"Fe":26,'Co':27,'Ni':28,'Cu':29,'Zn':30,'Ga':31,'Ge':32,'As':33,'Se':34,'Br':35,'Kr':36,'Rb':37,'Sr':38,'Y':39,'Zr':40,'Nb':42,'Mo':42,'Tc':43,'Ru':44,'Rh':45,'Pd':46,'Ag':47,'Cd':48,'In':49,'Sn':50,'Sb':51,'Te':52,'I':53,'Xe':54,'Cs':55,'Ba':56,'La':57,'Hf':72,'Ta':73,'W':74,'Re':75,'Os':76,'Ir':77,'Pt':78,'Au':79,'Hg':80,'Tl':81,'Pb':82,'Bi':83,'Po':84,'At':85,'Rn':86,'Fr':87,'Ra':88,'Ac':89,'Rf':104,'Db':105,'Sg':106,'Bh':107,'Hs':108,'Mt':109,'Ds':110,'Rg':111,'Cn':112,'Nh':113,'Fl':114,'Mc':115,'Lv':116,'Ts':117,'Og':118,'Ce':58,'Pr':59,'Nd':60,'Pm':61,'Sm':62,'Eu':63,'Gd':64,'Tb':65,'Dy':66,'Ho':67,'Er':68,'Tm':69,'Yb':70,'Lu':71,'Th':90,'Pa':91,'U':92,'Np':93,'Pu':94,'Am':95,'Cm':96,'Bk':97,'Cf':98,'Es':99,'Fm':100,'Md':101,'No':102,'Lr':103,}
    MolarMass = {0:0,"H":1.0079,"He":4.0026,"Li":6.941,"Be":9.0122,'B':10.811,'C':12.0107,"N":14.0067,"O":15.9994,"F":18.9984,"Ne":20.1797,"Na":22.9897,"Mg":24.305,"Al":26.9815,"Si":28.0855,"P":30.9738,"S":32.065,"Cl":35.453,"Ar":39.948,"K":39.0983,"Ca":40.078,"Sc":44.9559,"Ti":47.867,"V":50.9415,"Cr":51.9961,"Mn":54.938,"Fe":55.845,'Co':58.9332,'Ni':58.6934,'Cu':63.546,'Zn':65.39,'Ga':69.723,'Ge':72.64,'As':74.9216,'Se':78.96,'Br':79.904,'Kr':83.8,'Rb':85.4678,'Sr':87.62,'Y':88.9059,'Zr':91.224,'Nb':92.9064,'Mo':95.94,'Tc':98,'Ru':101.07,'Rh':102.9055,'Pd':106.42,'Ag':107.8682,'Cd':112.411,'In':114.818,'Sn':118.71,'Sb':121.76,'Te':127.6,'I':126.9045,'Xe':131.293,'Cs':132.9055,'Ba':137.327,'La':138.9055,'Hf':178.49,'Ta':180.9479,'W':183.84,'Re':186.207,'Os':190.23,'Ir':192.217,'Pt':195.078,'Au':196.9665,'Hg':200.59,'Tl':204.3833,'Pb':207.2,'Bi':208.9804,'Po':209,'At':210,'Rn':222,'Fr':223,'Ra':226,'Ac':227,'Rf':261,'Db':262,'Sg':266,'Bh':264,'Hs':277,'Mt':268,'Ds':281,'Rg':272,'Cn':285,'Nh':286,'Fl':289,'Mc':288,'Lv':292,'Ts':293,'Og':294,'Ce':140.116,'Pr':140.9077,'Nd':144.24,'Pm':145,'Sm':150.36,'Eu':151.964,'Gd':157.25,'Tb':158.9253,'Dy':162.5,'Ho':164.9303,'Er':167.259,'Tm':168.9342,'Yb':173.04,'Lu':174.967,'Th':232.0381,'Pa':231.0359,'U':238.0289,'Np':237,'Pu':244,'Am':243,'Cm':247,'Bk':247,'Cf':251,'Es':252,'Fm':257,'Md':258,'No':259,'Lr':262,}
    ElectroNeg = {0:"",1:2.20,2:"Unknown",3:0.98,4:1.57,5:2.04,6:2.55,7:3.04,8:3.44,9:3.98,10:"Unknown", 11:0.93,12:1.31,13:1.61,14:1.90,15:2.19,16:2.58,17:3.16,18:"Unknown",19:0.82,20:1.00,21:1.36,22:1.54,23:1.63,24:1.66,25:1.55,26:1.83,27:1.88,28:1.91,29:1.90,30:1.65,31:1.81,32:2.01,33:2.18,34:2.55,35:2.96,36:3.00,37:0.82,38:0.95,39:1.22,40:1.33,41:1.6,42:2.16,43:1.9,44:2.2,45:2.28,46:2.20,47:1.93,48:1.69,49:1.78,50:1.96,51:2.05,52:2.1,53:2.66,54:2.6,55:0.79,56:0.89,57:1.10,58:1.12,59:1.13,60:1.14,61:1.13,62:1.17,63:1.2,64:1.2,65:1.22,66:1.23,67:1.24,68:1.24,69:1.25,70:1.1,71:1.27,72:1.3,73:1.5,74:2.36,75:1.9,76:2.2,77:2.2,78:2.28,79:2.54,80:2.00,81:1.62,82:2.33,83:2.02,84:2.0,85:2.2,86:"Unknown",87:0.7,88:0.89,89:1.1,90:1.3,91:1.5,92:1.38,93:1.36,94:1.28,95:1.3,96:1.3,97:1.3,98:1.3,99:1.3,100:1.3,101:1.3,102:1.3,103:"Unknown",104:"Unknown",105:"Unknown",106:"Unknown",107:"Unknown",108:"Unknown",109:"Unknown",110:"Unknown",111:"Unknown",112:"Unknown",113:"Unknown",114:"Unknown",115:"Unknown",116:"Unknown",117:"Unknown",118:"Unknown"}
    MPoint = {-272:2,-259:1,-249:10,-220:9,-218:8,-210:7,-189:18,-157:36,-112:54,-101:17,-71:86,-39:80,-7:35,27:87,29:55,  30:31,39:37,44:15,64:19,98:11,113:16,114:53,157:49,180:3,217:34,232:50,254:84,271:83,302:85,303:81,321:48,327:82,420:30,449:52,630:51,639:12,640:93,640:94,660:13,700:88,725:56,769:38,795:58,8168:33,822:63,824:70,827:102,839:20,860:99,900:98,920:57,935:59,937:32,962:47,986:97,994:95,1010:60,1050:89,1064:79,1072:62,1083:29,1100:61,1132:92,1245:25,1278:4,1311:64,1340:96,1360:65,1410:14,1412:66,1453:28,1470:67,1495:27,1522:68,1523:39,1527:100,1535:26,1539:21,1545:69,1552:46,1568:91,1627:103,1656:71,1660:22,1750:90,1772:78,1852:40,1857:24,1890:23,1966:45,2150:72,2200:43,2250:44,2300:5,2410:77,2468:41,2617:42,2996:73,3045:76,3180:75,3410:74,3500:6,"Unknown":101,"Unknown":104,"Unknown":105,"Unknown":106,"Unknown":107,"Unknown":108,"Unknown":109,"Unknown":110,"Unknown":111,"Unknown":112,"Unknown":113,"Unknown":114,"Unknown":115,"Unknown":116,"Unknown":117,"Unknown":118,"":0}
    BPoint = {-269:2,-253:1,-246:10,-196:7,-188:9,-186:18,-183:8,-153:36,-108:54,-62:86,-35:17,58.8:35,184:53,280:15,337:85,357:80,445:16,613:33,677:87,678:55,685:34,688:37,760:19,765:48,774:19,883:11,907:30,962:84,990:52,1090:12,1140:56,1347:3,1384:38,1457:81,1466:70,1484:20,1560:83,1597:63,1727:69,1737:88,1740:82,1750:51,1900:62,1962:25,2000:49,2212:47,2270:50,2355:14,2403:31,2467:13,2510:68,2550:5,2562:66,2567:29,2607:95,2672:24,2720:67,2732:28,2750:26,2807:79,2830:32,2832:21,2870:27,2927:46,2970:4,3000:61,3041:65,3127:59,3127:60,3200:89,3233:64,3235:94,3257:58,3287:22,3315:71,3337:39,3380:23,3469:57,3727:45,3818:92,3827:78,3900:44,3902:93,4377:40,4527:77,4612:42,4790:90,4827:6,4877:43,4927:41,5027:76,5400:72,5425:73,5627:75,5660:74,"Unknown":91,"Unknown":96,"Unknown":97,"Unknown":98,"Unknown":99,"Unknown":100,"Unknown":101,"Unknown":102,"Unknown":103,"Unknown":104,"Unknown":105,"Unknown":106,"Unknown":107,"Unknown":108,"Unknown":109,"Unknown":110,"Unknown":111,"Unknown":112,"Unknown":113,"Unknown":114,"Unknown":115,"Unknown":116,"Unknown":117,"Unknown":118,"":0}
    
    COVER.lift();CLOSE.lift();ETIT.lift();PRTN.lift();MASS.lift();ELCTR.lift();MPOINT.lift();BPOINT.lift();IMG.lift();ECON.lift();CONLAB.lift()

    atmc = ANumber[D]
    symbl = D
    
    SO1 = [0]#[0]=s, [1]=p, [2]=d, [3]=f
    SO2 = [0,0]
    SO3 = [0,0,0]
    SO4 = [0,0,0,0]
    SO5 = [0,0,0,0]
    SO6 = [0,0,0]
    SO7 = [0,0]
    Config = ""
    for e in range(0,ANumber[D]):
        if e < 2:
            SO1[0]+=1
        if e >= 2 and e < 4:
            SO2[0]+=1
        if e >= 4 and e < 10:
            SO2[1]+=1
        if e >= 10 and e < 12:
            SO3[0]+=1
        if e >= 12 and e < 18:
            SO3[1]+=1
        if e >= 18 and e < 20:
            SO4[0]+=1
        if e >= 20 and e < 30:
            SO3[2]+=1
        if e >= 30 and e < 36:
            SO4[1]+=1
        if e >= 36 and e < 38:
            SO5[0]+=1
        if e >= 38 and e < 48:
            SO4[2]+=1
        if e >= 48 and e < 54:
            SO5[1]+=1
        if e >= 54 and e < 56:
            SO6[0]+=1
        if e >= 56 and e < 70:
            SO4[3]+=1
        if e >= 70 and e < 80:
            SO5[2]+=1
        if e >= 80 and e < 86:
            SO6[1]+=1
        if e >= 86 and e < 88:
            SO7[0]+=1
        if e >= 88 and e < 102:
            SO5[3]+=1
        if e >= 102 and e < 112:
            SO6[2]+=1
        if e >= 112 and e < 118:
            SO7[1]+=1

    if D == "Cr" or D == "Cu":
        SO4[0]-=1
        SO3[2]+=1
    
    if SO1[0] != 0:
        shells +=1
    if SO2[0] != 0:
        shells +=1
    if SO3[0] != 0:
        shells +=1
    if SO4[0] != 0:
        shells +=1
    if SO5[0] != 0:
        shells +=1
    if SO6[0] != 0:
        shells +=1
    if SO7[0] != 0:
        shells +=1
        
    SuperSC = {1:"¹",2:"²",3:"³",4:"⁴",5:"⁵",6:"⁶",7:"⁷",8:"⁸",9:"⁹",10:"¹⁰",11:"¹¹",12:"¹²",13:"¹³",14:"¹⁴"}    
    if SO1[0] != 0:
        Config += "1s"+SuperSC[SO1[0]]+" "
    if SO2[0] != 0:
        Config += "2s"+SuperSC[SO2[0]]+" "
    if SO2[1] != 0:
        Config += "2p"+SuperSC[SO2[1]]+" "
    if SO3[0] != 0:
        Config += "3s"+SuperSC[SO3[0]]+" "
    if SO3[1] != 0:
        Config += "3p"+SuperSC[SO3[1]]+" "
    if SO4[0] != 0:
        Config += "4s"+SuperSC[SO4[0]]+" "
    if SO3[2] != 0:
        Config += "3d"+SuperSC[SO3[2]]+" "
    if SO4[1] != 0:
        Config += "4p"+SuperSC[SO4[1]]+" "
    if SO5[0] != 0:
        Config += "5s"+SuperSC[SO5[0]]+" "
    if SO4[2] != 0:
        Config += "4d"+SuperSC[SO4[2]]+" "
    if SO5[1] != 0:
        Config += "5p"+SuperSC[SO5[1]]+" "
    if SO6[0] != 0:
        Config += "6s"+SuperSC[SO6[0]]+" "
    if SO4[3] != 0:
        Config += "4f"+SuperSC[SO4[3]]+" "
    if SO5[2] != 0:
        Config += "5d"+SuperSC[SO5[2]]+" "
    if SO6[1] != 0:
        Config += "6p"+SuperSC[SO6[1]]+" "
    if SO7[0] != 0:
        Config += "7s"+SuperSC[SO7[0]]+" "
    if SO5[3] != 0:
        Config += "5f"+SuperSC[SO5[3]]+" "
    if SO6[2] != 0:
        Config += "6d"+SuperSC[SO6[2]]+" "
    if SO7[1] != 0:
        Config += "7p"+SuperSC[SO7[1]]
    
    ETIT['text'] = names[D]
    PRTN['text'] = "Atomic Number: "+str(ANumber[D])
    MASS['text'] = "Molar Mass: "+str(MolarMass[D])
    ELCTR['text'] = "Electronegativity: "+str(ElectroNeg[ANumber[D]])

    for x,y in MPoint.items():
        if ANumber[D] == y:
            MPOINT['text'] = "Melting point: "+str(x)+"°C"

    for x,y in BPoint.items():
        if ANumber[D] == y:
            BPOINT['text'] = "Boiling point: "+str(x)+"°C"

    CONLAB['text'] = "Electron configuration: "+Config
    
    if D == 0:
        COVER.lower();CLOSE.lower();ETIT.lower();PRTN.lower();MASS.lower();ELCTR.lower();MPOINT.lower();BPOINT.lower();IMG.lower();ECON.lower();CONLAB.lower()
        shells = 0

    Ad = sum(SO1);Bd = sum(SO2);Cd = sum(SO3);Dd = sum(SO4);Ed = sum(SO5);Fd = sum(SO6);Gd = sum(SO7)
    symb = D
    atmc = ANumber[D]


period1 = ["H", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "He"]
period2 = ["Li", "Be", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "B", "C", "N", "O", "F", "Ne"]
period3 = ["Na", "Mg", 0, 0, 0,0, 0, 0, 0, 0, 0, 0, "Al","Si","P", "S", "Cl", "Ar"]
period4 = ["K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr']
period5 = ['Rb', 'Sr', 'Y','Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I','Xe']
period6 = ['Cs', 'Ba', 'La', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn']
period7 = ['Fr', 'Ra', 'Ac', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
Lanthanides = [0, 0, 0, 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu',0]
Actinides = [0 ,0 ,0 ,'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk' ,'Cf' ,'Es', 'Fm', 'Md', 'No', 'Lr', 0]

#Period Tags
Label(np,text="1",bg="#fafafa",fg="#000",font="System 10 bold").grid(row=1,column=0)
Label(np,text="2",bg="#fafafa",fg="#000",font="System 10 bold").grid(row=2,column=0)
Label(np,text="3",bg="#fafafa",fg="#000",font="System 10 bold").grid(row=3,column=0)
Label(np,text="4",bg="#fafafa",fg="#000",font="System 10 bold").grid(row=4,column=0)
Label(np,text="5",bg="#fafafa",fg="#000",font="System 10 bold").grid(row=5,column=0)
Label(np,text="6",bg="#fafafa",fg="#000",font="System 10 bold").grid(row=6,column=0)
Label(np,text="7",bg="#fafafa",fg="#000",font="System 10 bold").grid(row=7,column=0)

Label(np,text="IA",bg="#fafafa",fg="#000",font="System 4").grid(row=0,column=1)
Label(np,text="IIA",bg="#fafafa",fg="#000",font="System 4").grid(row=0,column=2)
Label(np,text="IIIB",bg="#fafafa",fg="#000",font="System 4").grid(row=0,column=3)
Label(np,text="IVB",bg="#fafafa",fg="#000",font="System 4").grid(row=0,column=4)
Label(np,text="VB",bg="#fafafa",fg="#000",font="System 4").grid(row=0,column=5)
Label(np,text="VIB",bg="#fafafa",fg="#000",font="System 4").grid(row=0,column=6)
Label(np,text="VIIB",bg="#fafafa",fg="#000",font="System 4").grid(row=0,column=7)
Label(np,text="VIIIB",bg="#fafafa",fg="#000",font="System 4").grid(row=0,column=8)
Label(np,text="VIIIIB",bg="#fafafa",fg="#000",font="System 4").grid(row=0,column=9)
Label(np,text="VIIIIIB",bg="#fafafa",fg="#000",font="System 4").grid(row=0,column=10)
Label(np,text="IB",bg="#fafafa",fg="#000",font="System 4").grid(row=0,column=11)
Label(np,text="IIB",bg="#fafafa",fg="#000",font="System 4").grid(row=0,column=12)
Label(np,text="IIIA",bg="#fafafa",fg="#000",font="System 4").grid(row=0,column=13)
Label(np,text="IVA",bg="#fafafa",fg="#000",font="System 4").grid(row=0,column=14)
Label(np,text="VA",bg="#fafafa",fg="#000",font="System 4").grid(row=0,column=15)
Label(np,text="VIA",bg="#fafafa",fg="#000",font="System 4").grid(row=0,column=16)
Label(np,text="VIIA",bg="#fafafa",fg="#000",font="System 4").grid(row=0,column=17)
Label(np,text="VIIIA",bg="#fafafa",fg="#000",font="System 4").grid(row=0,column=18)

"""
Colour scheme:
Alkali metals = a00000
Alkali earth metals = c9810a
Halogens (ex Ts) = caaebe
Noble gases = 865689
Other non-metals (B,C,N,O,SI,P,S,AS,SE,TE) = 0d6306
Trans Metals = 566789
Lanthanides = e9ab00
Actinides = 999999
"""
for e in period1:
    if e == "H":
        a = Button(np,text=e,fg="white",bg="#a00000",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("H"))
        a.grid(row=1,column=period1.index(e)+1)
    elif e == "He":
        a = Button(np,text=e,fg="white",bg="#865689",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("He"))
        a.grid(row=1,column=period1.index(e)+1)

for e in period2:
    if e == "Ne":
        a = Button(np,text=e,fg="white",bg="#865689",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Ne"))
        a.grid(row=2,column=period2.index(e)+1)
    elif e == "Li":
        a = Button(np,text=e,fg="white",bg="#a00000",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Li"))
        a.grid(row=2,column=period2.index(e)+1)
    elif e == "Be":
        a = Button(np,text=e,fg="white",bg="#c9810a",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Be"))
        a.grid(row=2,column=period2.index(e)+1)
    elif e == "F":
        a = Button(np,text=e,fg="white",bg="#caaebe",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("F"))
        a.grid(row=2,column=period2.index(e)+1)
    elif e == "B":
        a = Button(np,text=e,fg="white",bg="#0d6306",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("B"))
        a.grid(row=2,column=period2.index(e)+1)
    elif e == "C":
        a = Button(np,text=e,fg="white",bg="#0d6306",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("C"))
        a.grid(row=2,column=period2.index(e)+1)
    elif e=="N":
        a = Button(np,text=e,fg="white",bg="#0d6306",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("N"))
        a.grid(row=2,column=period2.index(e)+1)
    elif e=="O":
        a = Button(np,text=e,fg="white",bg="#0d6306",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("O"))
        a.grid(row=2,column=period2.index(e)+1)

for e in period3:
    if e == "Ar":
        a = Button(np,text=e,fg="white",bg="#865689",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Ar"))
        a.grid(row=3,column=period3.index(e)+1)
    elif e == "Na":
        a = Button(np,text=e,fg="white",bg="#a00000",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Na"))
        a.grid(row=3,column=period3.index(e)+1)
    elif e == "Mg":
        a = Button(np,text=e,fg="white",bg="#c9810a",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Mg"))
        a.grid(row=3,column=period3.index(e)+1)
    elif e == "Cl":
        a = Button(np,text=e,fg="white",bg="#caaebe",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Cl"))
        a.grid(row=3,column=period3.index(e)+1)
    elif e == "Al":
        a = Button(np,text=e,fg="white",bg="#898989",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Al"))
        a.grid(row=3,column=period3.index(e)+1)
    elif e == "Si":
        a = Button(np,text=e,fg="white",bg="#0d6306",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Si"))
        a.grid(row=3,column=period3.index(e)+1)
    elif e=="P":
        a = Button(np,text=e,fg="white",bg="#0d6306",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("P"))
        a.grid(row=3,column=period3.index(e)+1)
    elif e=="S":
        a = Button(np,text=e,fg="white",bg="#0d6306",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("S"))
        a.grid(row=3,column=period3.index(e)+1)
    elif e != 0:
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search(e))
        a.grid(row=3,column=period3.index(e)+1)

for e in period4:
    if e == "Kr":
        a = Button(np,text=e,fg="white",bg="#865689",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Kr"))
        a.grid(row=4,column=period4.index(e)+1)
    elif e == "K":
        a = Button(np,text=e,fg="white",bg="#a00000",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("K"))
        a.grid(row=4,column=period4.index(e)+1)
    elif e == "Ca":
        a = Button(np,text=e,fg="white",bg="#c9810a",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Ca"))
        a.grid(row=4,column=period4.index(e)+1)
    elif e == "Zn":
        a = Button(np,text=e,fg="white",bg="#898989",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Zn"))
        a.grid(row=4,column=period4.index(e)+1)
    elif e == "Ga":
        a = Button(np,text=e,fg="white",bg="#898989",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Ga"))
        a.grid(row=4,column=period4.index(e)+1)
    elif e == "Ge":
        a = Button(np,text=e,fg="white",bg="#898989",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Ge"))
        a.grid(row=4,column=period4.index(e)+1)
    elif e == "Br":
        a = Button(np,text=e,fg="white",bg="#caaebe",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Br"))
        a.grid(row=4,column=period4.index(e)+1)
    elif e == "As":
        a = Button(np,text=e,fg="white",bg="#0d6306",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("As"))
        a.grid(row=4,column=period4.index(e)+1)
    elif e == "Se":
        a = Button(np,text=e,fg="white",bg="#0d6306",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Se"))
        a.grid(row=4,column=period4.index(e)+1)

    elif e == "Sc":
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Sc"))
        a.grid(row=4,column=period4.index(e)+1)
    elif e == "Ti":
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Ti"))
        a.grid(row=4,column=period4.index(e)+1)
    elif e == "V":
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("V"))
        a.grid(row=4,column=period4.index(e)+1)
    elif e == "Cr":
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Cr"))
        a.grid(row=4,column=period4.index(e)+1)
    elif e == "Mn":
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Mn"))
        a.grid(row=4,column=period4.index(e)+1)
    elif e == "Fe":
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Fe"))
        a.grid(row=4,column=period4.index(e)+1)
    elif e == "Co":
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Co"))
        a.grid(row=4,column=period4.index(e)+1)
    elif e == "Ni":
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Ni"))
        a.grid(row=4,column=period4.index(e)+1)
    elif e == "Cu":
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Cu"))
        a.grid(row=4,column=period4.index(e)+1)
        
for e in period5:
    if e == "Xe":
        a = Button(np,text=e,fg="white",bg="#865689",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Xe"))
        a.grid(row=5,column=period5.index(e)+1)
    elif e == "Rb":
        a = Button(np,text=e,fg="white",bg="#a00000",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Rb"))
        a.grid(row=5,column=period5.index(e)+1)
    elif e == "Sr":
        a = Button(np,text=e,fg="white",bg="#c9810a",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Sr"))
        a.grid(row=5,column=period5.index(e)+1)
        
    elif e == "Cd":
        a = Button(np,text=e,fg="white",bg="#898989",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Cd"))
        a.grid(row=5,column=period5.index(e)+1)
    elif e == "In":
        a = Button(np,text=e,fg="white",bg="#898989",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("In"))
        a.grid(row=5,column=period5.index(e)+1)
    elif e == "Sn":
        a = Button(np,text=e,fg="white",bg="#898989",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Sn"))
        a.grid(row=5,column=period5.index(e)+1)
    elif e == "Sb":
        a = Button(np,text=e,fg="white",bg="#898989",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Sb"))
        a.grid(row=5,column=period5.index(e)+1)
        
    elif e == "I":
        a = Button(np,text=e,fg="white",bg="#caaebe",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("I"))
        a.grid(row=5,column=period5.index(e)+1)
    elif e == "Te":
        a = Button(np,text=e,fg="white",bg="#0d6306",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Te"))
        a.grid(row=5,column=period5.index(e)+1)
        
    elif e == 'Y':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Y"))
        a.grid(row=5,column=period5.index(e)+1)
    elif e == 'Zr':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Zr"))
        a.grid(row=5,column=period5.index(e)+1)
    elif e == 'Nb':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Nb"))
        a.grid(row=5,column=period5.index(e)+1)
    elif e == 'Mo':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Mo"))
        a.grid(row=5,column=period5.index(e)+1)
    elif e == 'Tc':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Tc"))
        a.grid(row=5,column=period5.index(e)+1)
    elif e == 'Ru':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Ru"))
        a.grid(row=5,column=period5.index(e)+1)
    elif e == 'Rh':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Rh"))
        a.grid(row=5,column=period5.index(e)+1)
    elif e == 'Pd':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Pd"))
        a.grid(row=5,column=period5.index(e)+1)
    elif e == 'Ag':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Ag"))
        a.grid(row=5,column=period5.index(e)+1)

for e in period6:
    if e == "Rn":
        a = Button(np,text=e,fg="white",bg="#865689",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Rn"))
        a.grid(row=6,column=period6.index(e)+1)
    elif e == "Cs":
        a = Button(np,text=e,fg="white",bg="#a00000",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Cs"))
        a.grid(row=6,column=period6.index(e)+1)
    elif e == "Ba":
        a = Button(np,text=e,fg="white",bg="#c9810a",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Ba"))
        a.grid(row=6,column=period6.index(e)+1)
        
    elif e == "Hg":
        a = Button(np,text=e,fg="white",bg="#898989",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Hg"))
        a.grid(row=6,column=period6.index(e)+1)
    elif e == "Tl":
        a = Button(np,text=e,fg="white",bg="#898989",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Tl"))
        a.grid(row=6,column=period6.index(e)+1)
    elif e == "Pb":
        a = Button(np,text=e,fg="white",bg="#898989",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Pb"))
        a.grid(row=6,column=period6.index(e)+1)
    elif e == "Bi":
        a = Button(np,text=e,fg="white",bg="#898989",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Bi"))
        a.grid(row=6,column=period6.index(e)+1)
    elif e == "Po":
        a = Button(np,text=e,fg="white",bg="#898989",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Po"))
        a.grid(row=6,column=period6.index(e)+1)
        
    elif e == "At":
        a = Button(np,text=e,fg="white",bg="#caaebe",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("At"))
        a.grid(row=6,column=period6.index(e)+1)
    elif e == "La":
        a = Button(np,text=e,fg="white",bg="#e9ab00",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("La"))
        a.grid(row=6,column=period6.index(e)+1)
        
    elif e == 'Hf':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Hf"))
        a.grid(row=6,column=period6.index(e)+1)
    elif e == 'Ta':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Ta"))
        a.grid(row=6,column=period6.index(e)+1)
    elif e == 'W':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("W"))
        a.grid(row=6,column=period6.index(e)+1)
    elif e == 'Re':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Re"))
        a.grid(row=6,column=period6.index(e)+1)
    elif e == 'Os':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Os"))
        a.grid(row=6,column=period6.index(e)+1)
    elif e == 'Ir':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Ir"))
        a.grid(row=6,column=period6.index(e)+1)
    elif e == 'Pt':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Pt"))
        a.grid(row=6,column=period6.index(e)+1)
    elif e == 'Au':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Au"))
        a.grid(row=6,column=period6.index(e)+1)

for e in period7:
    if e == "Fr":
        a = Button(np,text=e,fg="white",bg="#a00000",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Fr"))
        a.grid(row=7,column=period7.index(e)+1)
    elif e == "Ra":
        a = Button(np,text=e,fg="white",bg="#c9810a",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Ra"))
        a.grid(row=7,column=period7.index(e)+1)
        
    elif e == "Nh":
        a = Button(np,text=e,fg="white",bg="#898989",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Nh"))
        a.grid(row=7,column=period7.index(e)+1)
    elif e == "Fl":
        a = Button(np,text=e,fg="white",bg="#898989",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Fl"))
        a.grid(row=7,column=period7.index(e)+1)
    elif e == "Mc":
        a = Button(np,text=e,fg="white",bg="#898989",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Mc"))
        a.grid(row=7,column=period7.index(e)+1)
    elif e == "Lv":
        a = Button(np,text=e,fg="white",bg="#898989",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Lv"))
        a.grid(row=7,column=period7.index(e)+1)
    elif e == "Cn":
        a = Button(np,text=e,fg="white",bg="#898989",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Cn"))
        a.grid(row=7,column=period7.index(e)+1)
    elif e == "Ts":
        a = Button(np,text=e,fg="white",bg="#898989",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Ts"))
        a.grid(row=7,column=period7.index(e)+1)

    elif e == "Og":
        a = Button(np,text=e,fg="white",bg="#865689",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Og"))
        a.grid(row=7,column=period7.index(e)+1)
    elif e == "Ac":
        a = Button(np,text=e,fg="white",bg="#999999",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Ac"))
        a.grid(row=7,column=period7.index(e)+1)
        
    elif e == 'Rf':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Rf"))
        a.grid(row=7,column=period7.index(e)+1)
    elif e == 'Db':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Db"))
        a.grid(row=7,column=period7.index(e)+1)
    elif e == 'Sg':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Sg"))
        a.grid(row=7,column=period7.index(e)+1)
    elif e == 'Bh':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Bh"))
        a.grid(row=7,column=period7.index(e)+1)
    elif e == 'Hs':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Hs"))
        a.grid(row=7,column=period7.index(e)+1)
    elif e == 'Mt':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Mt"))
        a.grid(row=7,column=period7.index(e)+1)
    elif e == 'Ds':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Ds"))
        a.grid(row=7,column=period7.index(e)+1)
    elif e == 'Rg':
        a = Button(np,text=e,fg="white",bg="#566789",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Rg"))
        a.grid(row=7,column=period7.index(e)+1)

pry = Label(np,height=1)
pry.grid(row=8,column=0)

for e in Lanthanides:
    if e == "Ce":
        a = Button(np,text=e,fg="white",bg="#e9ab00",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Ce"))
        a.grid(row=9,column=Lanthanides.index(e) )
    if e == "Pr":
        a = Button(np,text=e,fg="white",bg="#e9ab00",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Pr"))
        a.grid(row=9,column=Lanthanides.index(e) )
    if e == "Nd":
        a = Button(np,text=e,fg="white",bg="#e9ab00",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Nd"))
        a.grid(row=9,column=Lanthanides.index(e) )
    if e == "Pm":
        a = Button(np,text=e,fg="white",bg="#e9ab00",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Pm"))
        a.grid(row=9,column=Lanthanides.index(e) )
    if e == "Sm":
        a = Button(np,text=e,fg="white",bg="#e9ab00",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Sm"))
        a.grid(row=9,column=Lanthanides.index(e) )
    if e == "Eu":
        a = Button(np,text=e,fg="white",bg="#e9ab00",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Eu"))
        a.grid(row=9,column=Lanthanides.index(e) )
    if e == "Gd":
        a = Button(np,text=e,fg="white",bg="#e9ab00",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Gd"))
        a.grid(row=9,column=Lanthanides.index(e) )
    if e == "Tb":
        a = Button(np,text=e,fg="white",bg="#e9ab00",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Tb"))
        a.grid(row=9,column=Lanthanides.index(e) )
    if e == "Dy":
        a = Button(np,text=e,fg="white",bg="#e9ab00",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Dy"))
        a.grid(row=9,column=Lanthanides.index(e) )
    if e == "Ho":
        a = Button(np,text=e,fg="white",bg="#e9ab00",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Ho"))
        a.grid(row=9,column=Lanthanides.index(e) )
    if e == "Er":
        a = Button(np,text=e,fg="white",bg="#e9ab00",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Er"))
        a.grid(row=9,column=Lanthanides.index(e) )
    if e == "Tm":
        a = Button(np,text=e,fg="white",bg="#e9ab00",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Tm"))
        a.grid(row=9,column=Lanthanides.index(e) )
    if e == "Yb":
        a = Button(np,text=e,fg="white",bg="#e9ab00",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Yb"))
        a.grid(row=9,column=Lanthanides.index(e) )
    if e == "Lu":
        a = Button(np,text=e,fg="white",bg="#e9ab00",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search("Lu"))
        a.grid(row=9,column=Lanthanides.index(e) )


for e in Actinides:
    if e == 'Th':
        a = Button(np,text=e,fg="white",bg="#999999",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search('Th'))
        a.grid(row=10,column=Actinides.index(e) )
    if e == 'Pa':
        a = Button(np,text=e,fg="white",bg="#999999",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search('Pa'))
        a.grid(row=10,column=Actinides.index(e) )
    if e == 'U':
        a = Button(np,text=e,fg="white",bg="#999999",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search('U'))
        a.grid(row=10,column=Actinides.index(e) )
    if e == 'Np':
        a = Button(np,text=e,fg="white",bg="#999999",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search('Np'))
        a.grid(row=10,column=Actinides.index(e) )
    if e == 'Pu':
        a = Button(np,text=e,fg="white",bg="#999999",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search('Pu'))
        a.grid(row=10,column=Actinides.index(e) )
    if e == 'Am':
        a = Button(np,text=e,fg="white",bg="#999999",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search('Am'))
        a.grid(row=10,column=Actinides.index(e) )
    if e == 'Cm':
        a = Button(np,text=e,fg="white",bg="#999999",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search('Cm'))
        a.grid(row=10,column=Actinides.index(e) )
    if e == 'Bk':
        a = Button(np,text=e,fg="white",bg="#999999",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search('Bk'))
        a.grid(row=10,column=Actinides.index(e) )
    if e == 'Cf':
        a = Button(np,text=e,fg="white",bg="#999999",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search('Cf'))
        a.grid(row=10,column=Actinides.index(e) )
    if e == 'Es':
        a = Button(np,text=e,fg="white",bg="#999999",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search('Es'))
        a.grid(row=10,column=Actinides.index(e) )
    if e == 'Fm':
        a = Button(np,text=e,fg="white",bg="#999999",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search('Fm'))
        a.grid(row=10,column=Actinides.index(e) )
    if e == 'Md':
        a = Button(np,text=e,fg="white",bg="#999999",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search('Md'));a.grid(row=10,column=Actinides.index(e) )
    if e == 'No':
        a = Button(np,text=e,fg="white",bg="#999999",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search('No'));a.grid(row=10,column=Actinides.index(e) )
    if e == 'Lr':
        a = Button(np,text=e,fg="white",bg="#999999",height=2,width=4,font="Georgia 13 bold",borderwidth=0,command=lambda: search('Lr'));a.grid(row=10,column=Actinides.index(e) )

TITLE = Label(np,text="Periodic Table",fg="black",bg="#ffffff",font="Georgia 30 bold")
TITLE.place(relx=0.25,rely=0.14)
COPR = Label(np, text="MahirTech MMXIX ©", fg="white", bg="green", font="Fixedsys 12")
COPR.place(relx=0.325, rely=0.25)

COVER = Label(np,bg="#eee",padx=570,pady=295);COVER.place(relx=0.0,rely=0.0);COVER.lower()

CLOSE = Button(np,text="r",fg="white",bg="#f01010",font="Webdings 22 bold",borderwidth=0,command=lambda: search(0));CLOSE.place(anchor="center",relx=0.05,rely=0.07);CLOSE.lower()
ETIT = Label(np,text="",fg="black",bg="#eee",font="Georgia 40 bold");ETIT.place(anchor="w",relx=0.1,rely=0.08);ETIT.lower()
PRTN = Label(np,text="",fg="black",bg="#eee",font="Georgia 20");PRTN.place(anchor=W,relx=0.05,rely=0.22);PRTN.lower()
MASS = Label(np,text="",fg="black",bg="#eee",font="Georgia 20");MASS.place(anchor=W,relx=0.05,rely=0.31);MASS.lower()
ELCTR = Label(np,text="",fg="black",bg="#eee",font="Georgia 20");ELCTR.place(anchor=W,relx=0.05,rely=0.40);ELCTR.lower()
MPOINT = Label(np,text="",fg="black",bg="#eee",font="Georgia 20");MPOINT.place(anchor=W,relx=0.05,rely=0.49);MPOINT.lower()
BPOINT = Label(np,text="",fg="black",bg="#eee",font="Georgia 20");BPOINT.place(anchor=W,relx=0.05,rely=0.58);BPOINT.lower()
CONLAB = Label(np,text="",fg="black",bg="#eee",font="Georgia 14");CONLAB.place(anchor='center',relx=0.5,rely=0.92);CONLAB.lower()

ec = PhotoImage(file="Electro.jpg")
IMG = Button(np,image=ec,text="TEST",fg="#fff",bg="#3090b0",font="Georgia 12",borderwidth=0); IMG.place(anchor=E,relx=0.99,rely=0.35); IMG.lower();
ECON = Button(np,text="Click here to see electronic configuaration",fg="#fff",bg="#3090b0",font="Georgia 12",borderwidth=0,command = lambda:drawConfig(shells,symb,atmc,Ad,Bd,Cd,Dd,Ed,Fd,Gd));ECON.place(anchor=E,relx=0.985,rely=0.7);ECON.lower()

np.mainloop()
