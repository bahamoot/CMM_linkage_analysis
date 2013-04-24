import sys
import csv
import xlwt

member1_csv  = sys.argv[1]
member1_code = sys.argv[2]
member2_csv  = sys.argv[3]
member2_code = sys.argv[4]
incommon_csv = sys.argv[5]
output_file  = sys.argv[6]

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def add_csv_sheet(wb, sheet_name, csv_file, st):
    ws = wb.add_sheet(sheet_name)
    with open(csv_file, 'rb') as csvfile:
        csv_records = list(csv.reader(csvfile, delimiter='\t'))
        for row in xrange(len(csv_records)):
            csv_record = csv_records[row]
            for col in xrange(len(csv_record)):
                if (isFloat(csv_record[7]) and (float(csv_record[7])<=0.1)) or (csv_record[7]=='') :
                    if (csv_record[2] != 'synonymous SNV'):
                        ws.write(row, col, csv_record[col], st)
                    else:
                        ws.write(row, col, csv_record[col])
                else:
                    ws.write(row, col, csv_record[col])
    ws.set_panes_frozen(True)
    ws.set_horz_split_pos(1)

wb = xlwt.Workbook()
yellow_st = xlwt.easyxf('pattern: pattern solid, fore_colour yellow;')

add_csv_sheet(wb, member1_code, member1_csv, yellow_st)
add_csv_sheet(wb, member2_code, member2_csv, yellow_st)
add_csv_sheet(wb, "In common", incommon_csv, yellow_st)

wb.save(output_file)

