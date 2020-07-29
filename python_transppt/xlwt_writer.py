#-*- coding:utf-8 -*-
import xlwt
import xlrd

# read file
r_wb=xlrd.open_workbook("kbo_rank.xlsx")
r_ws=r_wb.sheet_by_index(0)

ncol=r_ws.ncols
nrow=r_ws.nrows

# write file
wb=xlwt.Workbook(encoding='utf-8')
ws=wb.add_sheet('sheet1')

def load_score(rank):
    for i in range(nrow):
    	ws.write(0,i, r_ws.row_values(rank)[i])

rank=raw_input("순위를 입력하세요 :  ")

load_score(int(rank))
wb.save('team_score.xls')