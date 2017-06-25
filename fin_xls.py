#!/usr/bin/env python
import os
import sys
import xlwt,xlrd
from optparse import OptionParser

def option():
    parser = OptionParser()
    parser.add_option("-o","--output",
        dest = "getOutput",
        action = "store",
        type = "string",
        help = "Output file name",
        default = "output")
    parser.add_option("-f","--file",
        dest = "fileName",
        action = "store",
        type = "string",
        help = "File that contains data ",
        default = False)
    parser.add_option("-d","--dir",
        dest = "dirPath",
        action = "store",
        type = "string",
        help = "The directory to be analyzed ",
        default = False)
    options = parser.parse_args()[0]
    return options

def checkDir(options):
    args = {}
    if options.dirPath and options.fileName:
        print 'please input "filename" or "dirpath"'
        sys.exit(1)
    if not options.dirPath and not options.fileName:
        print "%s [-h--help]" % sys.argv[0]
        sys.exit(1)
    if options.getOutput:
        args['getOutput'] = options.getOutput
    if options.dirPath:
        args['dirPath'] = options.dirPath
        name = args['dirPath']
    if options.fileName:
        args['fileName'] = options.fileName
        name = args['fileName']
    return args, name

def createWorkBook():
    wb = xlwt.Workbook()
    return wb

def createSheet(wb,shName):
    sheet = wb.add_sheet(shName)
    return sheet

def createMyList(name):
    myList = []
    sh = ['ID:USERNAME:SALARY:COMPANY']
    if os.path.isfile(name):
        f = open(name,'r')
        ln = f.readline()
        st = ln.strip()
        if st == sh[0]:
            for i in (f.readlines()):
                st = i.strip()
                sp = st.split(':')
                if len(sp) > 4:
                    continue
                myList.append(sp)
        if myList == []:
            print 'The "%s" does not have the necessary data' % name
            sys.exit(1)
    elif os.path.isdir(name):
        for k in os.walk(name):
            for j in (k[2]):
                relPath = os.path.join(k[0],j)
                absPath = os.path.abspath(relPath)
                f = open(absPath, 'r')
                ln = f.readline()
                st = ln.strip()
                if st == sh[0]:
                    for i in (f.readlines()):
                        st = i.strip()
                        sp = st.split(':')
                        if len (sp) > 4:
                            continue
                        myList.append(sp)
        if myList == []:
            print 'The "%s" does not have the necessary data' % name
            sys.exit(1)
    else:
        print 'please, input correct "filename" or "dirpath"'
        sys.exit(1)
    f.close()
    return myList,sh
#def stripSplit(f,sh):
#    ln = f.readline()
#    st = ln.strip()
#    if st == sh[0]:
#        for i in (f.readlines()):
#            st = i.strip()
#            sp = st.split(':')
#    return sp

def writeInFile(sh,sheet, myList):
    font = xlwt.easyxf('''
                       font: height 220, name Arial,colour_index black,
                       bold off,italic off; 
                       align: wrap on, vert centre, horiz centre;
                       pattern: pattern solid, fore_colour yellow;
                       borders: top thin, bottom thin, left thin, right thin;
                       ''')
    font1 = xlwt.easyxf('''
                       font: height 240, name Arial,colour_index red,
                       bold off,italic off; 
                       align: wrap on, vert centre, horiz centre;
                       pattern: pattern solid, fore_colour blue;
                       borders: top thin, bottom thin, left thin, right thin;
                       ''')
    sh = sh[0].split(':')
    ml = 0
    colLength = []
    for i, j in enumerate(sh):
        sheet.write(ml, i, j, font1)
        sheet.row(ml).height = 400
        colLength.append(len(sh[i]))
    ml = 1
    for v in myList:
        for i, y in enumerate(v):
            sheet.write(ml, i, y, font )
            sheet.row(ml).height = 250
            if len(y) > colLength[i]:
                colLength[i] = len(y)
        ml += 1
    for col, length in enumerate(colLength):
        sheet.col(col).width = length * 320   

def saveProject(wb,sheet,destFileName):
    sheet.portrait = False
    sheet.set_print_scaling(85)
    wb.save(destFileName)

def main():
    sh = 'a'
    options = option()
    opt = checkDir(options)
    wb = createWorkBook()
    sheet = createSheet(wb,'test')
    myList = createMyList(opt[1])
    writeInFile(myList[1],sheet, myList[0])
    saveProject(wb, sheet,opt[0]['getOutput']+'.xls')

if __name__ == "__main__":
    main()


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4 filetype=python
