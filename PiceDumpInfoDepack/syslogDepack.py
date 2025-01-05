# coding=utf-8

import os, sys

def getfileLine(fileName):
    # reload(sys)
    # sys.setdefaultencoding("gdk")

    count = 0
    # thefile = open(r"d:\lines_test.txt",'rb')
    thefile = open(fileName, 'r', encoding='UTF-8')

    while True:
        buffer = thefile.read(1024 * 8192)
        if not buffer:
            break
        count += buffer.count('\n')

    thefile.close()

    return count

def replace(str):

    pos = str.find("PC802_0 PFI ",1)
    print("Pos = %d" %pos)
    str_line = str[pos:]

    str_line = str_line.replace("PC802_0 PFI", ",PC802_0 PFI")
    str_line = str_line.replace("msg=", "msg=,")
    str_line = str_line.replace(" dir_q=0x01 ", ", dir_q,0x01,")
    str_line = str_line.replace(" dir_q=0x02 ", ", dir_q,0x02,")
    str_line = str_line.replace(" dir_q=0x11 ", ", dir_q,0x11,")
    str_line = str_line.replace(" dir_q=0x12 ", ", dir_q,0x12,")

    str_line = str_line.replace(" type= ", ", type= ,")
    str_line = str_line.replace("SLot_SFN = ", "SLot_SFN  ,")
    str_line = str_line.replace(" mcycle=", ", mcycle,")

    return str_line


def main_func(argv):
    strSortInfo = []

    if len(argv) == 1:
        print(" The input is not enough...")
        return

    for i in range(len(argv) - 1):
        strSortInfo.append(argv[i])
        print(argv[i])

    fileAttr = argv[-1]

    #fileAttr = "_1.log"
    #strSortInfo.append("mcycle=")
    '''
    strSortInfo.append("Memory Section")
    fileAttr = "_mem.txt"
    '''

    # 打开文件
    sortFilePath = os.getcwd()  # 得到进程当前工作目录

    allFileList = os.listdir(sortFilePath)
    fileNums = len(allFileList)

    for filePtrR in allFileList:
        if ".log" in filePtrR:
            filePtrW = filePtrR.split('.')[-2] + fileAttr  # + filePtrR.split('.')[-1]
            print('The write file is %s...' % filePtrW)

            file_r = open(filePtrR, 'r', encoding='UTF-8')
            file_w = open(filePtrW, 'w')

            fileLens = getfileLine(filePtrR)
            print("%s size is %d" % (filePtrR, fileLens))
            for cnt in range(fileLens):
                str_line = file_r.readline()
                for strSort in strSortInfo:
                    if strSort in str_line:
                        strWrite = replace(str_line)
                        print(strWrite)

                        file_w.writelines("%4d %s" % (cnt, strWrite))
                        break

            file_r.close()
            file_w.close()


if __name__ == '__main__':
    main_func(sys.argv)
    # main_func(["POLAR UL Checking End sfn", "] are now at slot[" , "_cycle.txt"])
