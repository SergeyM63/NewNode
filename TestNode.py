class Nodes:
    def __init__(self, Sys='617.6666.452', Name='E24/ 12', Rack="Rack_18",
                 NumberNode=23, ALG=100, ALG_A=2,
                 DRV=0,
                 CD1=0, CD2=0, CD3=0, CD4=0, CD5=0, CD6=0, CD7=0, CD8=0,
                 CU1=0, CU2=0, CU3=0, CU4=0, CU5=0, CU6=0, CU7=0, CU8=0,
                 CMD1=1, CMD2=2, CMD3=3, CMD4=4, CMD5=0, CMD6=0, CMD7=0, CMD8=0, ):  # Имя узла, номер узла,

        self.sys = Sys
        self.name = Name
        self.rack = Rack
        self.NumberNode = NumberNode
        self.NumberNode_Str = str(NumberNode)
        self.ALG = ALG
        self.ALG_Str = str(ALG)
        self.ALG_A = ALG_A
        self.ALG_A_Str = str(ALG_A)
        self.DRV = DRV
        self.DRV_Str = str(DRV)

        self.CD1 = CD1
        self.CD1_Str = str(CD1)
        self.CD2 = CD2
        self.CD2_Str = str(CD2)
        self.CD3 = CD3
        self.CD3_Str = str(CD3)
        self.CD1 = CD4
        self.CD1_Str = str(CD4)
        self.CD2 = CD5
        self.CD2_Str = str(CD5)
        self.CD2 = CD6
        self.CD2_Str = str(CD6)
        self.CD1 = CD7
        self.CD1_Str = str(CD7)
        self.CD2 = CD8
        self.CD2_Str = str(CD8)

        self.CU1 = CU1
        self.CU1_Str = str(CU1)
        self.CU2 = CU2
        self.CU2_Str = str(CU2)
        self.CU3 = CU3
        self.CU3_Str = str(CU3)
        self.CU4 = CU4
        self.CU4_Str = str(CU4)
        self.CU5 = CU5
        self.CU5_Str = str(CU5)
        self.CU6 = CU6
        self.CU6_Str = str(CU6)
        self.CU7 = CU7
        self.CU7_Str = str(CU7)
        self.CU8 = CU8
        self.CU8_Str = str(CU8)

        self.CMD1 = CMD1
        self.CMD1_Str = str(CMD1)
        self.CMD2 = CMD2
        self.CMD2_Str = str(CMD2)
        self.CMD3 = CMD3
        self.CMD3_Str = str(CMD3)
        self.CMD4 = CMD4
        self.CMD4_Str = str(CMD4)
        self.CMD5 = CMD5
        self.CMD5_Str = str(CMD5)
        self.CMD6 = CMD6
        self.CMD6_Str = str(CMD6)
        self.CMD7 = CMD7
        self.CMD7_Str = str(CMD7)
        self.CMD8 = CMD8
        self.CMD8_Str = str(CMD8)

        self.TXT = "ggfcjiwjfue"

    @property
    def NewNodeTXT(self):
        self.TXT = str("""qwqew""")

        f = open("""NewNode""" + self.name + """.txt""", "w")
        f.write(self.TXT)  # Вывести в файл
        f.close()
        return self.TXT




if __name__ == "__main__":
    NewNodeMSV = Nodes('617.017.45', 'E10-19', "Rack_S15", 42, 1108, 2, 65323,
                       101, 102, 103, 104, 105, 106, 107, 108,
                       201, 202, 203, 204, 205, 206, 207, 208)
    NewNodeMSV2 = Nodes('617.012.45', 'E40/ 8', "Rack_18", 45, 1007, 1, 7645,
                        301, 302, 303, 304, 305, 306, 307, 308,
                        401, 402, 403, 404, 405, 406, 407, 408)

    print("**************************************************************")
    print("Система - " + NewNodeMSV.sys)
    print("Узел - " + NewNodeMSV.name)
    print("Намбер - ", NewNodeMSV.NumberNode)
    print("Алгоритм - ", NewNodeMSV.ALG)
    print("Массив Алгоритмов - ", NewNodeMSV.ALG_A)
    print("Маска приводов - ", NewNodeMSV.DRV)
    print(NewNodeMSV.rack)
    print("Отрицательные счётчики: ")
    print("CD1 - ", NewNodeMSV.CD1)
    print("CD2 - ", NewNodeMSV.CD2)
    print("Положительные счётчики: ")
    print("CU1 - ", NewNodeMSV.CU1)
    print("CU2 - ", NewNodeMSV.CU2)
    print("Приказы: ")
    print("CMD1 - ", NewNodeMSV.CMD1)
    print("CMD2 - ", NewNodeMSV.CMD2)

    # print(NewNodeMSV.lastName())
    print("**************************************************************")

    print(NewNodeMSV.NewNodeTXT)
