import os
import xlrd
import arcpy

#make a workspace
arcpy.env.workspace = r"V:\QNAP RTRR Folder\Projects\Heatwave risk mapping\arcgis_workspace"

# Perform the conversion
in_excel = r"V:\QNAP RTRR Folder\Projects\Heatwave risk mapping\Data\RCP 4.5 Year % Deaths.xlsm"
arcpy.ExcelToTable_conversion(in_excel, "excess_deaths_rcp45.gdb", "Sheet1")


#def importallsheets(in_excel, out_gdb):
#    workbook = xlrd.open_workbook(in_excel)
#    sheets = [sheet.name for sheet in workbook.sheets()]
#
#    print('{} sheets found: {}'.format(len(sheets), ','.join(sheets)))
#    for sheet in sheets:
#        # The out_table is based on the input excel file name
#        # a underscore (_) separator followed by the sheet name
#        out_table = os.path.join(
#            out_gdb,
#            arcpy.ValidateTableName(
#                "{0}_{1}".format(os.path.basename(in_excel), sheet),
#                out_gdb))
#
#        print('Converting {} to {}'.format(sheet, out_table))
#
#        # Perform the conversion
#        arcpy.ExcelToTable_conversion(in_excel, out_table, sheet)
#
#if __name__ == '__main__':
#    importallsheets('c:/data/data.xls',
#                    'c:/data/outgdb.gdb')
