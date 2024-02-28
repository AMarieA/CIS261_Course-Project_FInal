#ALaina Acton
#CIS 261
#Course Project Phase 3

def GetempName():
    empname = input("Enter Employee name: ")
    return empname

def GetdatesWorked():
    fromdate = input("Enter the start date (mm/dd/yyyy): ")
    todate = input("Enter the end date (mm/dd/yyyy): ")
    return fromdate, todate

def GethoursWorked():
    hours = float((input("Enter the amount of hours worked: ")))
    return hours

def GethourlyRate():
    hourlyrate = float(input("Enter the hourly rate: "))
    return hourlyrate

def GettaxRate():
    taxrate = float(input("Enter tax rate: "))
    return taxrate

def CalcTaxandNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printInfo(EmpDetailList): #Establish a list and assign places.
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    
    for EmpList in EmpDetailList:
        
        fromdate = EmpList[0]
        todate = EmpList[1]
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]
    
        grosspay, incometax, netpay = CalcTaxandNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.2f}", f"{hourlyrate:,.2f}", f"{grosspay:,.2f}", f"{taxrate:,.1%}", f"{incometax:,.2f}", f"{netpay:.2f}")
        
        #calculating and adding to...keeping a count
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
    
    EmpTotals["TotEmp"] = TotEmployees
    EmpTotals["TotHours"] = TotHours
    EmpTotals["TotGrossPay"] = TotGrossPay
    EmpTotals["TotTax"] = TotTax
    EmpTotals["TotNetPay"] = TotNetPay

def PrintTotals(EmpTotals):
    print()
    print(f"Total number of employess: {EmpTotals['TotEmp']}")
    print(f"Total hours worked: {EmpTotals['TotHours']}")
    print(f"Total Gross Pay: {EmpTotals['TotGrossPay']:,.2f}")
    print(f"Total Income Tax: {EmpTotals['TotTax']:,.1%}")
    print(f"Total Net Pay: {EmpTotals['TotNetPay']:,.2f}")
    
def WriteEmpInfo(employee):
    file = open("employeeinfo.txt", "a")
    file.write('{} | {} | {} | {} | {} | {}\n'.format(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))
    
def GetFromDate():
    valid = False
    fromdate = ""
    
    while not valid:
        fromdate = input("Enter from date (mm/dd/yyyy): ")
        if (len(fromdate.split('/')) != 3 and fromdate.upper() != 'ALL'):
            print("Invalid Date Format")
        else:
            valid = True
            
    return fromdate
        
def ReadEmpInfo(fromdate):
    EmpDetailList = []
    
    file = open("employeeinfo.txt", "r")
    data = file.readlines()
    
    condition = True
    
    if fromdate.upper() == 'ALL':
        condition = False
        
    for employee in data:
        employee = [x.strip() for x in employee.strip().split("|")]
        
        if not condition:
            EmpDetailList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
        else:
            if fromdate == employee[0]:
                EmpDetailList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
    return EmpDetailList
    
if __name__ == "__main__":
    EmpDetailList = []
    EmpTotals = {}
    
    while True:
        empname = GetempName()
        if (empname.upper() == "END"):
            break
        fromdate, todate = GetdatesWorked()
        hours = GethoursWorked()
        hourlyrate = GethourlyRate()
        taxrate = GettaxRate()
        
        print()
        EmpDetail = [fromdate, todate, empname, hours, hourlyrate, taxrate]
        WriteEmpInfo(EmpDetail)
    print()
    print()
    fromdate = GetFromDate()
    
    EmpDetailList = ReadEmpInfo(fromdate)
    
    print()
    printInfo(EmpDetailList)
    print()
    PrintTotals(EmpTotals)
    