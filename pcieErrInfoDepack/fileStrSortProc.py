# coding=utf-8

import time, datetime
import os ,sys

def getCurrTime():
    curr_time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    # print(curr_time)

    return curr_time


def getfileLine(fileName):
    #reload(sys)
    # sys.setdefaultencoding("gdk")

    count = 0
   # thefile = open(r"d:\lines_test.txt",'rb')
    thefile = open(fileName, 'r')

    while True:
        buffer = thefile.read(1024 * 8192)
        if not buffer:
            break
        count += buffer.count('\n')

    thefile.close()

    return count

strOld = [": PC802_0 " ," PRINTF: msg="  , " dir_q="  , " ALLOC " , " PUT " , " GET " , " FREE " , "type= "  , "SLot_SFN = "  ,  " mcycle="]
strNew = [": PC802_0 ,",",PRINTF: msg=," , ",dir_q=," , ",ALLOC " , ",PUT " , ",GET " , ",FREE " , ",type= ," , "SLot_SFN = ," ,  ",mcycle=,"]

def strReplaceInfo(strIn):
    strOut = strIn
    for i in range(len(strOld)):
        strOut = strOut.replace(strOld[i], strNew[i])

    mStart = strOut.find("PC802_0 ")
    strOut_new = strOut[mStart+9:]
    
    return strOut_new
        

def main_func(argv):
    strSortInfo = []
    for i in range(1,len(argv) - 1):
        strSortInfo.append(argv[i])
        print("Argv[%d] = { %s }" %(i, argv[i]))

    if len(argv) > 1:
        pfiNum = "_pfi" + argv[len(argv) - 1]
    else:
        pfiNum = "_pfi" + "0"
        strSortInfo.append("PFI 1 PRINTF: msg=")

    # 打开文件
    sortFilePath = os.getcwd()  # 得到进程当前工作目录
    
    allFileList = os.listdir(sortFilePath)
    fileNums = len(allFileList)
    lineCheck = 0
    for filePtrR in allFileList:
        if ".log" in filePtrR:
            # filePtrW = filePtrR.split('-')[-2] + getCurrTime() + pfiNum + '.txt'   #+ filePtrR.split('.')[-1]
            filePtrW = filePtrR[-43:-4] + getCurrTime()+ pfiNum + '.txt'   #+ filePtrR.split('.')[-1]
            print('The write file is %s...' %filePtrW)
            
            file_r = open(filePtrR, 'r')
            file_w = open(filePtrW, 'w')
            
            fileLens = getfileLine(filePtrR)
            print("%s size is %d \n" %(filePtrR , fileLens))
            for cnt in range(fileLens):
                str_line = file_r.readline()
                for strSort in strSortInfo:
                    if strSort in str_line:
                        lineCheck = lineCheck + 1
                    
                if lineCheck == len(strSortInfo):
                    str_line_new = strReplaceInfo(str_line)   
                    file_w.writelines(str_line_new)
                    # break
                lineCheck = 0

            file_r.close()
            file_w.close()
            
            time.sleep(2)

if __name__ == '__main__':
    main_func(sys.argv)
    # smain_func(["mac - Total:TbCrc pass, have" "Total:PolarCrc pass, have " "TbCrc fail, have "])
