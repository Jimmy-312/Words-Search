import xlrd,xlwt,xlutils
from xlutils import copy
wlist=[]

def read_file():
    global wlist
    file=xlrd.open_workbook(r'word.xls')
    sheet=file.sheet_by_index(0)
    for i in range(sheet.nrows):
        try:
            a=sheet.row_values(i)
            a=a[0]
            a=a.split()[1]
            wlist.append(a)
        except:
            continue
    print(wlist)

def write_file():
    global wlist
    file=xlrd.open_workbook(r'word.xls')
    sheet=file.sheet_by_index(4)
    for i in range(len(wlist)):
        sheet.put_cell(i+1,1,1,wlist[i],0)
        #print(sheet.row_values(i+1))
    file1=xlutils.copy.copy(file)
    file1.save('word.xls')

if __name__=='__main__':
    read_file()
    write_file()
