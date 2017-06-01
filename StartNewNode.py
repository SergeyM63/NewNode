# coding=utf-8

import os
import shutil
from nodes import *
#---------------MAIN-----------------------------------------------------------
if __name__ == "__main__":




    with open("input_E10-30.txt") as file:  # читаем построчно из входного файла
        ar = [row.strip() for row in file]  # и передаём строки в список
    print(ar)

    NewNodeMSV = Nodes(ar[0], ar[1], ar[2], ar[3], ar[4], ar[5], ar[6],
                       ar[7], ar[8], ar[9], ar[10], ar[11], ar[12], ar[13], ar[14],  # отр счётчики
                       ar[15], ar[16], ar[17], ar[18], ar[19], ar[20], ar[21], ar[22],  # пол счётчики
                       ar[23], ar[24], ar[25], ar[26],  # узлы впереди, сзади
                       ar[27], ar[28], ar[29], ar[30], ar[31], ar[32])  # стадии

    #NewNodeMSV.descriptionNode()       #печатаем свойства узла
    NewNodeMSV.createDirectory()      #готовим директорию
    NewNodeMSV.get_file_RoutineTXT()  #создаём файл Routine.txt
    NewNodeMSV.get_file_NodesTXT()    #создаём файл Nodes.txt
    NewNodeMSV.get_file_AlarmTXT()    #создаём файл Alarm.txt


