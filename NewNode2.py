# coding=utf-8


# import glob
import os
import shutil


class Nodes:
    def __init__(self, Sys='617.6666.452', Name='E24/ 12', Rack="Rack_18",
                 NumberNode="23", ALG="100", ALG_A="2",
                 DRV="0",
                 CD1="0", CD2="0", CD3="0", CD4="0", CD5="0", CD6="0", CD7="0", CD8="0",
                 CU1="0", CU2="0", CU3="0", CU4="0", CU5="0", CU6="0", CU7="0", CU8="0",
                 #CMD1="1", CMD2="2", CMD3="3", CMD4="4", CMD5="0", CMD6="0", CMD7="0", CMD8="0",
                 BackNode1="E24-11", BackNode2="E24-12", ForwardNode1="E19-11", ForwardNode2="E19-12",
                 STD1="10", STD2="20", STD3="13", STD4="23", STD5="17", STD6="27"):  # Имя узла, номер узла,

        self.sys = Sys
        self.name = Name
        self.rack = Rack
        self.NumberNode = NumberNode
        self.ALG = ALG
        self.ALG_A = ALG_A
        self.DRV = DRV

        self.CD1 = CD1
        self.CD2 = CD2
        self.CD3 = CD3
        self.CD4 = CD4
        self.CD5 = CD5
        self.CD6 = CD6
        self.CD7 = CD7
        self.CD8 = CD8

        self.CU1 = CU1
        self.CU2 = CU2
        self.CU3 = CU3
        self.CU4 = CU4
        self.CU5 = CU5
        self.CU6 = CU6
        self.CU7 = CU7
        self.CU8 = CU8

        # self.CMD1 = CMD1
        # self.CMD2 = CMD2
        # self.CMD3 = CMD3
        # self.CMD4 = CMD4
        # self.CMD5 = CMD5
        # self.CMD6 = CMD6
        # self.CMD7 = CMD7
        # self.CMD8 = CMD8

        self.backNode1 = BackNode1
        self.backNode2 = BackNode2
        self.forwardNode1 = ForwardNode1
        self.forwardNode2 = ForwardNode2

        self.std1 = STD1
        self.std2 = STD2
        self.std3 = STD3
        self.std4 = STD4
        self.std5 = STD5
        self.std6 = STD6


        self.STDs = ['301', '401', '302', '505', '605', '521']

        self.DIR = self.sys + '_' + self.name
        self.FullName = self.name + '  ' + self.sys

        self.TXT = ""

    def descriptionNode(self):
        print("**************************************************************")
        print(self.FullName)
        print("Система - " + self.sys)
        print("Узел - " + self.name)
        print("Намбер - ", self.NumberNode)
        print("Алгоритм - ", self.ALG)
        print("Массив Алгоритмов - ", self.ALG_A)
        print("Маска приводов - ", self.DRV)
        print(self.rack)
        print("Отрицательные счётчики: ")
        print("CD1 - ", self.CD1)
        print("CD2 - ", self.CD2)
        print("Положительные счётчики: ")
        print("CU1 - ", self.CU1)
        print("CU2 - ", self.CU2)
        print("Приказы: ")
        # print("CMD1 - ", self.CMD1)
        # print("CMD2 - ", self.CMD2)
        print("**************************************************************")

    def createDirectory(self):
        if os.path.isdir(self.DIR):  # проверка существованя папки
            shutil.rmtree(self.DIR)  # удаляем директорию
        os.mkdir(self.DIR)           # создаём папку

        # names = os.listdir(NewNodeMSV.DIR)  # список файлов и поддиректорий в данной директории
        # print(names)
        # for nameF in names:
        #     fullname = os.path.join(NewNodeMSV.DIR, nameF)  # получаем полное имя
        #     if os.path.isfile(fullname):  # если это файл...
        #         os.remove(fullname)  # удаляем

        # os.removedirs(NewNodeMSV.DIR)  # удаляем директорию

    def get_file_RoutineTXT(self):
        self.TXT = str(
            """EQU(CurrentNumberNode,""" + self.NumberNode + """)[MOV(""" + self.ALG + """,NODES[""" + self.NumberNode + """,0]) ,MOV(""" + self.ALG_A + """,NODES[""" + self.NumberNode + """,1]) ]MOV(""" + self.DRV + """,NODES[""" + self.NumberNode + """,2])[OTL(NODES[""" + self.NumberNode + """,2].15) ,OTL(NODES[""" + self.NumberNode + """,2].13) ][MOV(""" + self.CD1 + """,NODES[""" + self.NumberNode + """,4]) MOV(""" + self.CD2 + """,NODES[""" + self.NumberNode + """,5]),MOV(""" + self.CU1 + """,NODES[""" + self.NumberNode + """,12]) MOV(""" + self.CU2 + """,NODES[""" + self.NumberNode + """,13]) ];
     XIC(""" + self.rack + """:I.Data[0].1)OTE(NODES[""" + self.NumberNode + """,42].0);
     XIC(""" + self.rack + """:I.Data[0].2)OTE(NODES[""" + self.NumberNode + """,43].0);
     XIC(""" + self.rack + """:I.Data[0].3)OTE(NODES[""" + self.NumberNode + """,36].1);
     XIC(""" + self.rack + """:I.Data[0].3)OTE(NODES[""" + self.NumberNode + """,36].2);
     XIC(""" + self.rack + """:I.Data[0].4)OTE(NODES[""" + self.NumberNode + """,37].1);
     XIC(""" + self.rack + """:I.Data[0].4)OTE(NODES[""" + self.NumberNode + """,37].2);
     XIC(""" + self.rack + """:I.Data[0].5)OTE(NODES[""" + self.NumberNode + """,38].1);
     XIC(""" + self.rack + """:I.Data[0].5)OTE(NODES[""" + self.NumberNode + """,38].2);
     XIC(""" + self.rack + """:I.Data[0].6)OTE(NODES[""" + self.NumberNode + """,39].1);
     XIC(""" + self.rack + """:I.Data[0].6)OTE(NODES[""" + self.NumberNode + """,39].2);
     XIC(""" + self.rack + """:I.Data[0].7)OTL(NODES[""" + self.NumberNode + """,40].1);
     XIC(""" + self.rack + """:I.Data[0].7)OTL(NODES[""" + self.NumberNode + """,40].2);
     OTE(NODES[""" + self.NumberNode + """,44].3);
     AFI()JSR(SUPER,0);
     XIC(NODES[""" + self.NumberNode + """,51].0)OTE(""" + self.rack + """:O.Data[7].1);
     XIC(NODES[""" + self.NumberNode + """,46].1)OTE(""" + self.rack + """:O.Data[7].2);
     XIC(NODES[""" + self.NumberNode + """,46].2)OTE(""" + self.rack + """:O.Data[7].2);
     XIC(NODES[""" + self.NumberNode + """,48].1)OTE(""" + self.rack + """:O.Data[7].3);
     XIC(NODES[""" + self.NumberNode + """,49].1)OTE(""" + self.rack + """:O.Data[7].4);""")

        f = open(self.DIR + """\Routine_""" + self.name + """.txt""", "w")
        f.write(self.TXT)  # Вывести в файл
        f.close()
        print ("Файл Routine создан")
        # return self.TXT


    def get_file_NodesTXT(self):
        self.TXT = str(
            """
NODE	=	""" + self.name + """	""" + self.NumberNode + """	1
{
CounterNode	=	""" + self.CD1 + """	1-
CounterNode	=	""" + self.CD2 + """	2-
CounterNode	=	""" + self.CU1 + """	1+
CounterNode	=	""" + self.CU2 + """	2+
BackNode	=	""" + self.backNode1 + """
BackNode	=	""" + self.backNode2 + """
ForwardNode	=	""" + self.forwardNode1 + """
ForwardNode	=	""" + self.forwardNode2 + """
ChangeStage	=	0	""" + self.std1 + """	'Выпуск с 1 нитки'
ChangeStage	=	0	""" + self.std2 + """	'Выпуск со 2 нитки'
ChangeStage	=	0	""" + self.std3 + """	'Сход с В21 на В32'
ChangeStage	=	0	""" + self.std4 + """	'Сход с В21 на В31'
}
""")

        f = open(self.DIR + """\\Nodes_""" + self.name + """.txt""", "w")
        f.write(self.TXT)  # Вывести в файл
        f.close()
        print ("Файл Nodes создан")
        # return self.TXT


    def get_file_AlarmTXT(self):
        self.TXT = str("""
Dev_Name=""" + self.name + """
Dev_Number=""" + self.NumberNode + """
Messages=
NODES[""" + self.NumberNode + """,34].0	A	Авария по В21
NODES[""" + self.NumberNode + """,34].1	A	Авария по пропуску В21
NODES[""" + self.NumberNode + """,34].2	A	Авария по В22
NODES[""" + self.NumberNode + """,34].3	A	Авария по пропуску В22
NODES[""" + self.NumberNode + """,34].15	A	Авария по стрелке В91
_NODES[""" + self.NumberNode + """,42].0	W	Ручной режим
NODES[""" + self.NumberNode + """,43].0	O	Деблок. с пульта

""")

        f = open(self.DIR + """\Alarm_""" + self.name + """.txt""", "w")
        f.write(self.TXT)  # Вывести в файл
        f.close()
        print ("Файл Alarm создан")
        # return self.TXT


if __name__ == "__main__":

    with open("input.txt") as file:         #читаем построчно из входного файла
        ar = [row.strip() for row in file]  # и передаём строки в список
        #print(ar)

    NewNodeMSV = Nodes(ar[0], ar[1], ar[2], ar[3], ar[4], ar[5], ar[6],
                       ar[7], ar[8], ar[9], ar[10], ar[11], ar[12], ar[13], ar[14],
                       ar[15], ar[16], ar[17], ar[18], ar[19], ar[20], ar[21], ar[22],
                       ar[23], ar[24], ar[25], ar[26], # узлы впереди, сзади
                       ar[27], ar[28], ar[29], ar[30], ar[31], ar[32]) # стадии

    NewNodeMSV.descriptionNode()       #печатаем свойства узла
    NewNodeMSV.createDirectory()      #готовим директорию
    NewNodeMSV.get_file_RoutineTXT()  #создаём файл Routine.txt
    NewNodeMSV.get_file_NodesTXT()    #создаём файл Nodes.txt
    NewNodeMSV.get_file_AlarmTXT()    #создаём файл Alarm.txt


