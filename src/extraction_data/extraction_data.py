import xlrd


class ExtractionData:
    def __init__(self, file: str, roles: list[str], ignore_sheet: list[str] = [], valid_ncols = 3):
        self.file = file
        self.roles = roles
        self.ignore_sheet = ignore_sheet
        self.valid_ncols = valid_ncols
        
    def execute(self) -> dict[str,dict[int, dict[str, str]]]:
        data = dict()
        for worksheet in self.__open_file(self.file).sheets():
            if self.__validate_sheet(worksheet):
                data[worksheet.name] = self.__extraction(worksheet)
        return data
                
    def __open_file(self, file):
        return xlrd.open_workbook(file)
    
    def getSheets(self):
        return [sh.name for sh in self.__open_file(self.file).sheets() if self.__validate_sheet(sh)]
       
    def __validate_sheet(self, sheet) -> list[str]:
        return sheet.ncols >= self.valid_ncols and sheet.name not in self.ignore_sheet
    
    def __search_index_titles(self, sheet): 
        indexs: list[tuple] = []
        for row in range(0, sheet.nrows):
            for column in range(0, sheet.ncols):
                if sheet.cell_value(row, column) in self.roles:
                   indexs.append((row, column))
                if len(indexs) != 0 and column == sheet.ncols-1:
                    return indexs
                
    def __extraction(self, sheet) -> dict[int, dict[str, str]]:
        data = dict()
        indexs = self.__search_index_titles(sheet)
        start  = 0
        for row in range(indexs[0][0], sheet.nrows):
            data[start] = []
            list:list[tuple] = []
            for index in indexs:
                list.append((sheet.cell_value(index[0], index[1]) , str(sheet.cell_value(row, index[1]))))
            data[start] = dict((x, y) for x, y in list)
            start += 1
        return data