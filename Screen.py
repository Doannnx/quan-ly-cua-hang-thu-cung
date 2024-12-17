import tkinter as tk
import ttkbootstrap as ttk
from Service import *
from functools import partial

petShopSV = Service()

ScreenWidth = 1045
ScreenHeight = 563

root = ttk.Window(themename="lumen")
root.geometry("{w}x{h}+0+0".format(w=ScreenWidth, h=ScreenHeight))
root.title("PETSHOP NGANGO management System")
root.resizable(width=False, height=False)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


# frame = Frame(root)
# frame.pack()

numProduct = 0

menuBar = ttk.Frame(root, width=ScreenWidth * 0.17, height=ScreenHeight)
menuBar.pack(side=ttk.LEFT, fill=ttk.BOTH)

mainStyle = ttk.Style()
# mainStyle.theme_use('default')
# Configure the Treeview Colors
mainStyle.configure("Treeview",
	background="#D3D3D3",
	foreground="black",
	rowheight=25,
	fieldbackground="#D3D3D3")

# Change Selected Color #347083
# mainStyle.map('Treeview',
# 	background=[('selected', ttk.saved_highlight_color)])
mainStyle.configure('success.TButton', font=("Helvetica", 12),
                   width=18)

mainStyle.configure('success.Outline.TButton', font=("Helvetica", 12),
                   width=18)

mainFrame = ttk.Frame(root, width=ScreenWidth * 0.825, height=ScreenHeight)
mainFrame.pack(side=ttk.RIGHT, fill=ttk.BOTH)
mainFrame.pack_propagate(0)

def increaseNumberProduct(proQuanLabel):
    petShopSV.numProduct = petShopSV.numProduct + 1
    proQuanLabel.config(text=petShopSV.numProduct)

def decreaseNumberProduct(proQuanLabel):
    if petShopSV.numProduct > 0:
        petShopSV.numProduct = petShopSV.numProduct - 1
    proQuanLabel.config(text=petShopSV.numProduct)

def showOrderAndImport():
    for widget in mainFrame.winfo_children():
        widget.destroy()

    homeFrame = ttk.Frame(mainFrame, width=ScreenWidth * 0.825, height=ScreenHeight)
    homeFrame.pack(side=ttk.RIGHT, fill=ttk.BOTH)
    homeFrame.pack_propagate(0)

    homeFrame.update()
    creOrderFr = ttk.Frame(homeFrame, width=homeFrame.winfo_width()* 0.38,
                  height=homeFrame.winfo_height()*0.95, bootstyle="info")
    creOrderFr.update()
    creOrderFr.pack(side=tk.RIGHT, padx=10, pady=10)
    creOrderFr.pack_propagate(0)

    homeFrame.update()
    billFrame = ttk.Frame(homeFrame, width=homeFrame.winfo_width()*0.55,
                  height=homeFrame.winfo_height()*0.95)
    billFrame.place(width=homeFrame.winfo_width()*0.55,height=homeFrame.winfo_height()*0.95)
    billFrame.pack(side=tk.LEFT, padx=10, pady=10)
    billFrame.pack_propagate(0)

    billFrame.update()

    BillPrdFrame = tk.Frame(billFrame, width=billFrame.winfo_width() * 0.97,
                  height=billFrame.winfo_height()*0.5)
    # v = tk.Scrollbar(BillPrdFrame)
    # v.pack(side = tk.RIGHT, fill = tk.Y)

    # v.config(command=BillPrdFrame.yview)
    # BillPrdFrame.grid(row=0, column=0, rowspan=3, columnspan=2, padx=10, pady=10)
    BillPrdFrame.pack(side=tk.TOP, padx=10, pady=10)
    BillPrdFrame.pack_propagate(0)

    lb1 = tk.Label(creOrderFr, text="Type Product", width=15, height=2)
    lb1.pack(side=tk.TOP, pady=10)

    tplst = petShopSV.getTypeProduct()
    typeList = []
    for x in tplst:
        typeList.append(x[0])

    nVal2 = tk.StringVar()
    global listProductcmb 
    listProductcmb = ttk.Combobox(creOrderFr, width = 27, textvariable = nVal2)

    nVal1 = tk.StringVar()
    global listTypecmb
    listTypecmb = ttk.Combobox(creOrderFr, width = 27, textvariable = nVal1, values=typeList)
    listTypecmb.current(0)
    listTypecmb.pack(side=tk.TOP, pady=10, padx=10)
    listTypecmb.bind("<<ComboboxSelected>>", setComboBoxListProduct)  

    lb2 = tk.Label(creOrderFr, text="Product", width=15, height=2)
    lb2.pack(side=tk.TOP, pady=10)

    listProductcmb.pack(side=tk.TOP)
    listProductcmb.bind("<<ComboboxSelected>>", setAvailabelPrice)  

    addBut = ttk.Button(creOrderFr, text="ADD", width=30,
                        command=partial(addProductToList, BillPrdFrame))
    addBut.pack(side=tk.BOTTOM, pady=10)

    global lbAvaiPrice
    lbAvaiPrice = tk.Label(creOrderFr, text="Availabel:        Price:    ", width=30, height=2)
    lbAvaiPrice.pack(side=tk.TOP, pady=10)

    proQuanLabel = tk.Label(creOrderFr, text=petShopSV.numProduct, width=5, height=2)

    adQuan = ttk.Button(creOrderFr, text="+", width=5, command=partial(increaseNumberProduct, proQuanLabel))
    deQuan = ttk.Button(creOrderFr, text="-", width=5, command=partial(decreaseNumberProduct, proQuanLabel))

    adQuan.pack(side=tk.RIGHT, padx=40, pady=5)
    deQuan.pack(side=tk.LEFT, padx=40, pady=5)
    proQuanLabel.pack(pady=5, padx=5, expand=True)

    billTotal = ttk.Frame(billFrame, width=billFrame.winfo_width() * 0.97,
                  height=billFrame.winfo_height()*0.2)
    # billTotal.grid(row=3, column=0, columnspan = 2, padx = 5, pady = 5)
    billTotal.pack(side=tk.TOP, padx=10, pady=10)
    billTotal.pack_propagate(0)
    billTotal.update()

    frPr1 = ttk.Frame(billTotal)
    frPr1.pack(side=tk.LEFT, pady=5)

    textTotalLabel = "Subtotal:\n\nTax:\n\nTotal"

    prTo = tk.Label(frPr1, text=textTotalLabel, width=10, height=10)
    prTo.pack(side=tk.TOP, pady=5, padx=5)

    frPr2 = ttk.Frame(billTotal)
    frPr2.pack(side=tk.RIGHT, pady=5)

    # Tinh tong gia tri don hang
    totalText = ""
    subtotal, tax, total = petShopSV.calTotalOrder()
    totalText = "{}\n\n{}\n\n{}".format(subtotal, tax, total)

    global productTotal
    productTotal = tk.Label(frPr2, text=totalText, width=10, height=10)
    productTotal.pack(side=tk.TOP, pady=5, padx=5)

    billFrame.update()
    payAndCancelFr = tk.Frame(billFrame, width=billFrame.winfo_width() * 0.97,
                  height=10)
    payAndCancelFr.pack(side=tk.BOTTOM)

    global payBut
    payBut = tk.Button(payAndCancelFr, text="Pay {pr}".format(pr=total),
                       padx=10, pady=10,
                       command=partial(PayFunction, BillPrdFrame))
    canBut = tk.Button(payAndCancelFr, text="Cancel",
                       padx=10, pady=10,
                       command=partial(clearAllProduct, BillPrdFrame))

    payBut.pack(side=tk.RIGHT)
    canBut.pack(side=tk.LEFT)

    reloadBill(BillPrdFrame)
    # payBut.grid(row = 5, column = 1, rowspan=1, padx=5, pady=5)
    # canBut.grid(row = 5, column = 0, rowspan=1, padx=5, pady=5)

def reloadBill(BillPrdFrame):
    orderFr = []
    totalPrice = 0

    for widget in BillPrdFrame.winfo_children():
        widget.destroy()

    for i in range(len(petShopSV.orderProduct)):
        BillPrdFrame.update()
        fr1 = ttk.Frame(BillPrdFrame, width=BillPrdFrame.winfo_width() * 0.97,
                  height=30)
        fr1.update()
        fr1.pack_propagate(0)
        fr1.pack(side=tk.TOP, pady=2)

        stt = tk.Label(fr1, text="{ord}".format(ord=i), width=5,
                height=int(fr1.winfo_height()*0.96))
        stt.pack(side=tk.LEFT, pady=5)

        prName = tk.Label(fr1, text="{na}".format(na=petShopSV.orderProduct[i][1]), width=20,
                height=int(fr1.winfo_height()*0.96))
        prName.pack(side=tk.LEFT, pady=5, padx=5)

        prQuan = tk.Label(fr1, text="{qu}c".format(qu=petShopSV.orderProduct[i][2]), width=8,
                height=int(fr1.winfo_height()*0.96))
        prQuan.pack(side=tk.LEFT, pady=5, padx=5)

        prSum = tk.Label(fr1, text="{su}$".format(su=petShopSV.orderProduct[i][2]*petShopSV.orderProduct[i][3]),
                  width=10, height=int(fr1.winfo_height()*0.96))
        prSum.pack(side=tk.LEFT, pady=5, padx=5)

        canBut = tk.Button(fr1, text="X", width=7,
                    height=int(fr1.winfo_height()*0.96), command=partial(delProductInList, BillPrdFrame, i))
        canBut.pack(side=tk.RIGHT, pady=5, padx=5)

        orderFr.append(fr1)
        totalPrice += petShopSV.orderProduct[i][2]*petShopSV.orderProduct[i][3]
    
    subtotal, tax, total = petShopSV.calTotalOrder()
    totalText = "{}\n\n{}\n\n{}".format(subtotal, tax, total)

    productTotal.config(text=totalText)

    payBut.config(text="Pay {pr}".format(pr=total))

    return totalPrice

def delProductInList(billFrame, stt):
    petShopSV.orderProduct.pop(stt)
    reloadBill(billFrame)
    
def clearAllProduct(billFrame):
    petShopSV.clearListOrder()
    reloadBill(billFrame)

def PayFunction(billFrame):
    petShopSV.orderRequest()
    petShopSV.clearListOrder()
    # reloadBill(billFrame)
    for widget in billFrame.winfo_children():
        widget.destroy()

    bill_frame = tk.Frame(billFrame, bd=3, relief=tk.RIDGE)
    bill_frame.pack(side=tk.LEFT, padx=20)
    bill_frame.place(x=0, y=0, width=400, height=280)

    title_lbl2 = tk.Label(bill_frame, text="Bills", font=('Georgia', 20), bg='orange')
    title_lbl2.pack(side=tk.TOP, fill=tk.X)

    scroll_y2 = tk.Scrollbar(bill_frame, orient=tk.VERTICAL)
    billOrderArea = tk.Text(bill_frame, bg="lightyellow", yscrollcommand=scroll_y2.set)
    scroll_y2.pack(side=tk.RIGHT, fill=tk.Y)
    scroll_y2.config(command=billOrderArea.yview)
    billOrderArea.pack(fill=tk.BOTH, expand=1)

    billName = petShopSV.getBillName()

    billOrderArea.delete('1.0', tk.END)
    with open(f'bills/{billName}', 'r', encoding='utf-8') as fp:
        for line in fp:
            billOrderArea.insert(tk.END, line.encode('utf-8'))

def addProductToList(BillPrdFrame):
    id = 0

    id = petShopSV.getProductIDfromName(listProductcmb.get())
    petShopSV.addToListProduct(id, listProductcmb.get(), int(petShopSV.numProduct), petShopSV.mainFrameStatus)

    reloadBill(BillPrdFrame)

    subtotal, tax, total = petShopSV.calTotalOrder()
    totalText = "{}\n\n{}\n\n{}".format(subtotal, tax, total)
    productTotal.config(text=totalText)

    payBut.config(text="Pay {pr}".format(pr=total))

def setComboBoxListProduct(event):
    id = 0
    for idx in range(len(listTypecmb['values'])):
        if listTypecmb['values'][idx] == listTypecmb.get():
            id = idx + 1
            break

    tupleList = petShopSV.getProductListFromType(id)
    listProduct = []
    for lst in tupleList:
        listProduct.append(lst[0])

    listProductcmb.config(values=listProduct)

def setAvailabelPrice(event):
    id = petShopSV.getProductIDfromName(listProductcmb.get())

    avai = petShopSV.availabelProduct(id)

    price = petShopSV.getProductPrice(id, petShopSV.mainFrameStatus)
    textAvaiPrice = "Availabel: {}        Price:{}    ".format(avai, price)
    lbAvaiPrice.config(text=textAvaiPrice)

def homePageDisplay():
    for widget in mainFrame.winfo_children():
        widget.destroy()
    mainFrame.config(width=ScreenWidth * 0.825, height=ScreenHeight)
    mainFrame.update()

    sortFrame = tk.LabelFrame(mainFrame, width=mainFrame.winfo_width() * 0.9,
                         height=mainFrame.winfo_height() * 0.15, text="Sort")
    sortFrame.pack_propagate(False)
    sortFrame.pack(side=tk.TOP, padx=10, pady=20)

    global radio_val
    radio_val = tk.StringVar(value="Type")

    # Nut sort tren man hinh "Home"
    typeRadio = ttk.Radiobutton(sortFrame, bootstyle="info toolbutton",
                                variable=radio_val, text="Type", value="Type", command=staticSort)
    typeRadio.pack(side=tk.LEFT, padx=20)

    nameRadio = ttk.Radiobutton(sortFrame, bootstyle="info toolbutton",
                                variable=radio_val, text="Name", value="Name", command=staticSort)
    nameRadio.pack(side=tk.LEFT, padx=20)

    saleRadio = ttk.Radiobutton(sortFrame, bootstyle="info toolbutton",
                                variable=radio_val, text="Sale", value="Sale", command=staticSort)
    saleRadio.pack(side=tk.LEFT, padx=20)

    remainRadio = ttk.Radiobutton(sortFrame, bootstyle="info toolbutton",
                                variable=radio_val, text="Remain", value="Remain", command=staticSort)
    remainRadio.pack(side=tk.LEFT, padx=20)

    profitRadio = ttk.Radiobutton(sortFrame, bootstyle="info toolbutton",
                                variable=radio_val, text="Profit", value="Profit", command=staticSort)
    profitRadio.pack(side=tk.LEFT, padx=20)

    # Bang thong ke
    TableViewFrame = tk.LabelFrame(mainFrame, width=mainFrame.winfo_width() * 0.9,
                         height=mainFrame.winfo_height() * 0.6)
    TableViewFrame.pack_propagate(False)
    TableViewFrame.pack(side=tk.TOP, padx=20)

    TableViewFrame.update()

    tree_scroll = ttk.Scrollbar(TableViewFrame)

    # Create The Treeview
    global statisTree
    statisTree = ttk.Treeview(TableViewFrame, yscrollcommand=tree_scroll.set, selectmode="extended")
    statisTree.pack(side=tk.LEFT)
    # tree_scroll.pack(side=tk.LEFT)

    # Configure the Scrollbar
    tree_scroll.config(command=statisTree.yview)

    statisTree['columns'] = ("Type", "Product", "Sale", "Remain", "Profit")

    # Format Our Columns
    statisTree.column("#0", width=0, stretch=ttk.NO)
    statisTree.column("Type", anchor=ttk.W, width=140)
    statisTree.column("Product", anchor=ttk.W, width=200)
    statisTree.column("Sale", anchor=ttk.CENTER, width=100)
    statisTree.column("Remain", anchor=ttk.CENTER, width=100)
    statisTree.column("Profit", anchor=ttk.CENTER, width=100)

    # Create Headings
    statisTree.heading("#0", text="", anchor=ttk.W)
    statisTree.heading("Type", text="Type", anchor=ttk.W)
    statisTree.heading("Product", text="Product", anchor=ttk.W)
    statisTree.heading("Sale", text="Sale", anchor=ttk.CENTER)
    statisTree.heading("Remain", text="Remain", anchor=ttk.CENTER)
    statisTree.heading("Profit", text="Profit", anchor=ttk.CENTER)

    statisTree.tag_configure('oddrow', background="white")
    statisTree.tag_configure('evenrow', background="lightblue")

    petShopSV.sortByType()

    for idx in range(len(petShopSV.statisData)):
        row = petShopSV.statisData[idx]
        statisTree.insert(parent='', index='end', iid=idx,
                      values=(
                          row[0], row[1], row[2], row[3], row[4]
                      ))

    # Tinh tong ket duoi bang thong ke
    sumTableFrame = tk.LabelFrame(mainFrame, width=mainFrame.winfo_width() * 0.9,
                         height=mainFrame.winfo_height() * 0.08)
    sumTableFrame.pack_propagate(False)
    sumTableFrame.pack(side=tk.TOP)

    sumTableFrame.update()

    sumTableLabel = tk.Label(sumTableFrame, text="SUM:",
                  width=53, height=int(sumTableFrame.winfo_height()*0.96))
    sumTableLabel.pack(side=tk.LEFT)

    sumSale, sumRemain, sumProfit = petShopSV.getSumOfStatisData()

    sumSaleLabel = tk.Label(sumTableFrame, text="{}".format(sumSale),
                  width=14, height=int(sumTableFrame.winfo_height()*0.96), anchor=tk.W)
    sumSaleLabel.pack(side=tk.LEFT)

    sumRemainLabel = tk.Label(sumTableFrame, text="{}".format(sumRemain),
                  width=12, height=int(sumTableFrame.winfo_height()*0.96), anchor=tk.W)
    sumRemainLabel.pack(side=tk.LEFT)

    sumProfitLabel = tk.Label(sumTableFrame, text="{}".format(round(sumProfit, 2)),
                  width=14, height=int(sumTableFrame.winfo_height()*0.96), anchor=tk.W)
    sumProfitLabel.pack(side=tk.LEFT)

def staticSort():
    if radio_val.get() == "Name":
        petShopSV.sortbyName()
    elif radio_val.get() == "Sale":
        petShopSV.sortBySale()
    elif radio_val.get() == "Remain":
        petShopSV.sortByRemain()
    elif radio_val.get() == "Profit":
        petShopSV.sortByProfit()
    else:
        petShopSV.sortByType()

    for i in statisTree.get_children():
        statisTree.delete(i)

    for idx in range(len(petShopSV.statisData)):
        row = petShopSV.statisData[idx]
        statisTree.insert(parent='', index='end', iid=idx,
                      values=(
                          row[0], row[1], row[2], row[3], row[4]
                      ))
        
def EmployeeDisplay():
    for widget in mainFrame.winfo_children():
        widget.destroy()

    mainFrame.config(width=ScreenWidth * 0.825, height=ScreenHeight)
    mainFrame.update()

    employeeFrame = tk.Frame(mainFrame, width=mainFrame.winfo_width() * 0.9,
                         height=mainFrame.winfo_height() * 0.5)
    employeeFrame.pack_propagate(False)
    employeeFrame.pack(side=tk.TOP, pady=10)

    employeeFrame.update()

    employ_scroll = ttk.Scrollbar(employeeFrame)

    # Create The Treeview
    global employeeTable
    employeeTable = ttk.Treeview(employeeFrame, yscrollcommand=employ_scroll.set, selectmode="extended")
    employeeTable.pack(side=tk.LEFT)
    # tree_scroll.pack(side=tk.LEFT)

    # Configure the Scrollbar
    employ_scroll.config(command=employeeTable.yview)

    employeeTable['columns'] = ("ID", "Name", "Sex", "Phone", "Address")

    # Format Our Columns
    employeeTable.column("#0", width=0, stretch=ttk.NO)
    employeeTable.column("ID", anchor=ttk.W, width=40)
    employeeTable.column("Name", anchor=ttk.W, width=140)
    employeeTable.column("Sex", anchor=ttk.W, width=100)
    employeeTable.column("Phone", anchor=ttk.W, width=100)
    employeeTable.column("Address", anchor=ttk.W, width=250)

    # Create Headings
    employeeTable.heading("#0", text="", anchor=ttk.W)
    employeeTable.heading("ID", text="ID", anchor=ttk.W)
    employeeTable.heading("Name", text="Name", anchor=ttk.W)
    employeeTable.heading("Sex", text="Sex", anchor=ttk.W)
    employeeTable.heading("Phone", text="Phone", anchor=ttk.W)
    employeeTable.heading("Address", text="Address", anchor=ttk.W)

    employeeTable.tag_configure('oddrow', background="white")
    employeeTable.tag_configure('evenrow', background="lightblue")

    listEmployee = petShopSV.getEmloyeeList()

    for idx in range(len(listEmployee)):
        row = listEmployee[idx]
        employeeTable.insert(parent='', index='end', iid=idx,
                      values=(row[0], row[1], row[2], row[3], row[4]))
        
    addEmployeeFrame = tk.LabelFrame(mainFrame, width=mainFrame.winfo_width() * 0.9,
                         height=mainFrame.winfo_height() * 0.15, text="Add Employee")
    addEmployeeFrame.pack_propagate(False)
    addEmployeeFrame.pack(side=tk.TOP, padx=10, pady=10)
    addEmployeeFrame.update()

    IDEmployeeFrame = tk.LabelFrame(addEmployeeFrame, width=addEmployeeFrame.winfo_width() * 0.07,
                         height=addEmployeeFrame.winfo_height() * 0.9, text="ID")
    IDEmployeeFrame.pack_propagate(False)
    IDEmployeeFrame.pack(side=tk.LEFT, padx=5)
    
    IDEmployeeFrame.update()
    IDAddInput = tk.Text(IDEmployeeFrame, height = int(IDEmployeeFrame.winfo_width()), 
                         width = int(IDEmployeeFrame.winfo_height() * 0.95))
    IDAddInput.pack(side=tk.LEFT, pady=5)

    nameEmployeeFrame = tk.LabelFrame(addEmployeeFrame, width=addEmployeeFrame.winfo_width() * 0.12,
                         height=addEmployeeFrame.winfo_height() * 0.9, text="Name")
    nameEmployeeFrame.pack_propagate(False)
    nameEmployeeFrame.pack(side=tk.LEFT, padx=5)
    
    nameEmployeeFrame.update()
    nameAddInput = tk.Text(nameEmployeeFrame, height = int(nameEmployeeFrame.winfo_width()), 
                         width = int(nameEmployeeFrame.winfo_height() * 0.95))
    nameAddInput.pack(side=tk.LEFT, pady=5)

    SexEmployeeFrame = tk.LabelFrame(addEmployeeFrame, width=addEmployeeFrame.winfo_width() * 0.10,
                         height=addEmployeeFrame.winfo_height() * 0.9, text="Sex")
    SexEmployeeFrame.pack_propagate(False)
    SexEmployeeFrame.pack(side=tk.LEFT, padx=5)
    
    SexEmployeeFrame.update()
    sexAddInput = tk.Text(SexEmployeeFrame, height = int(SexEmployeeFrame.winfo_width()), 
                         width = int(SexEmployeeFrame.winfo_height() * 0.95))
    sexAddInput.pack(side=tk.LEFT, pady=5)

    phoneEmployeeFrame = tk.LabelFrame(addEmployeeFrame, width=addEmployeeFrame.winfo_width() * 0.17,
                         height=addEmployeeFrame.winfo_height() * 0.9, text="Phone")
    phoneEmployeeFrame.pack_propagate(False)
    phoneEmployeeFrame.pack(side=tk.LEFT, padx=5)
    
    phoneEmployeeFrame.update()
    phoneAddInput = tk.Text(phoneEmployeeFrame, height = int(phoneEmployeeFrame.winfo_width()), 
                         width = int(phoneEmployeeFrame.winfo_height() * 0.95))
    phoneAddInput.pack(side=tk.LEFT, pady=5)

    addressEmployeeFrame = tk.LabelFrame(addEmployeeFrame, width=addEmployeeFrame.winfo_width() * 0.30,
                         height=addEmployeeFrame.winfo_height() * 0.9, text="Address")
    addressEmployeeFrame.pack_propagate(False)
    addressEmployeeFrame.pack(side=tk.LEFT, padx=5)
    
    addressEmployeeFrame.update()
    addressAddInput = tk.Text(addressEmployeeFrame, height = int(addressEmployeeFrame.winfo_width()), 
                         width = int(addressEmployeeFrame.winfo_height() * 0.95))
    addressAddInput.pack(side=tk.LEFT, pady=5)

    addEmployeeButton = tk.Button(addEmployeeFrame, text="ADD", width=10,
                    height=int(addEmployeeFrame.winfo_height()*0.96),
                    command=partial(addEmployee, IDAddInput, nameAddInput, sexAddInput, phoneAddInput, addressAddInput))
    addEmployeeButton.pack(side=tk.RIGHT, pady=5, padx=5)

    delEmployeeFrame = tk.LabelFrame(mainFrame, width=mainFrame.winfo_width() * 0.9,
                         height=mainFrame.winfo_height() * 0.15, text="Delete Employee")
    delEmployeeFrame.pack_propagate(False)
    delEmployeeFrame.pack(side=tk.TOP, padx=10, pady=10)
    delEmployeeFrame.update()

    IDdelFrame = tk.LabelFrame(delEmployeeFrame, width=delEmployeeFrame.winfo_width() * 0.07,
                         height=delEmployeeFrame.winfo_height() * 0.9, text="ID")
    IDdelFrame.pack_propagate(False)
    IDdelFrame.pack(side=tk.LEFT, padx=10)
    
    IDdelFrame.update()
    IDdelInput = tk.Text(IDdelFrame, height = int(IDdelFrame.winfo_width()), 
                         width = int(IDdelFrame.winfo_height() * 0.95))
    IDdelInput.pack(side=tk.LEFT, pady=5)

    delEmployeeButton = tk.Button(delEmployeeFrame, text="DELETE", width=10,
                    height=int(delEmployeeFrame.winfo_height()*0.8),
                    command=partial(deleteEmployee, IDdelInput))
    delEmployeeButton.pack(side=tk.LEFT, padx=10, pady=10)

def CustomterDisplay():
    for widget in mainFrame.winfo_children():
        widget.destroy()

    mainFrame.config(width=ScreenWidth * 0.825, height=ScreenHeight)
    mainFrame.update()

    customerFrame = tk.Frame(mainFrame, width=mainFrame.winfo_width() * 0.9,
                         height=mainFrame.winfo_height() * 0.4)
    customerFrame.pack_propagate(False)
    customerFrame.pack(side=tk.TOP, padx=20)

    customerFrame.update()

    customer_scroll = ttk.Scrollbar(customerFrame)

    # Create The Treeview
    global customerTable
    customerTable = ttk.Treeview(customerFrame, yscrollcommand=customer_scroll.set, selectmode="extended")
    customerTable.pack(side=tk.LEFT)
    # tree_scroll.pack(side=tk.LEFT)

    # Configure the Scrollbar
    customer_scroll.config(command=customerTable.yview)

    customerTable['columns'] = ("ID", "Name", "Sex", "Phone", "Address", "Pet")

    # Format Our Columns
    customerTable.column("#0", width=0, stretch=ttk.NO)
    customerTable.column("ID", anchor=ttk.W, width=40)
    customerTable.column("Name", anchor=ttk.W, width=140)
    customerTable.column("Sex", anchor=ttk.W, width=100)
    customerTable.column("Phone", anchor=ttk.W, width=100)
    customerTable.column("Address", anchor=ttk.W, width=250)
    customerTable.column("Pet", anchor=ttk.W, width=140)

    # Create Headings
    customerTable.heading("#0", text="", anchor=ttk.W)
    customerTable.heading("ID", text="ID", anchor=ttk.W)
    customerTable.heading("Name", text="Name", anchor=ttk.W)
    customerTable.heading("Sex", text="Sex", anchor=ttk.W)
    customerTable.heading("Phone", text="Phone", anchor=ttk.W)
    customerTable.heading("Address", text="Address", anchor=ttk.W)
    customerTable.heading("Pet", text="Pet", anchor=ttk.W)

    customerTable.tag_configure('oddrow', background="white")
    customerTable.tag_configure('evenrow', background="lightblue")

    customerList = petShopSV.getCustomerList()

    for idx in range(len(customerList)):
        row = customerList[idx]
        customerTable.insert(parent='', index='end', iid=idx,
                      values=(row[0], row[1], row[2], row[3], row[4], row[5]))
        
    addCustomerFrame = tk.LabelFrame(mainFrame, width=mainFrame.winfo_width() * 0.9,
                         height=mainFrame.winfo_height() * 0.3, text="Add Employee")
    addCustomerFrame.pack_propagate(False)
    addCustomerFrame.pack(side=tk.TOP, padx=10, pady=10)
    addCustomerFrame.update()

    TextInputCustomerFrame = tk.Frame(addCustomerFrame, width=addCustomerFrame.winfo_width(),
                         height=addCustomerFrame.winfo_height() * 0.4)
    TextInputCustomerFrame.pack_propagate(False)
    TextInputCustomerFrame.pack(side=tk.TOP, padx=10, pady=10)
    TextInputCustomerFrame.update()

    IDCustomerFrame = tk.LabelFrame(TextInputCustomerFrame, width=TextInputCustomerFrame.winfo_width() * 0.07,
                         height=TextInputCustomerFrame.winfo_height() * 0.9, text="ID")
    IDCustomerFrame.pack_propagate(False)
    IDCustomerFrame.pack(side=tk.LEFT, padx=5)
    
    IDCustomerFrame.update()
    IDAddInput = tk.Text(IDCustomerFrame, height = int(IDCustomerFrame.winfo_width()), 
                         width = int(IDCustomerFrame.winfo_height() * 0.95))
    IDAddInput.pack(side=tk.LEFT, pady=5)

    nameCustomerFrame = tk.LabelFrame(TextInputCustomerFrame, width=TextInputCustomerFrame.winfo_width() * 0.12,
                         height=TextInputCustomerFrame.winfo_height() * 0.9, text="Name")
    nameCustomerFrame.pack_propagate(False)
    nameCustomerFrame.pack(side=tk.LEFT, padx=5)
    
    nameCustomerFrame.update()
    nameAddInput = tk.Text(nameCustomerFrame, height = int(nameCustomerFrame.winfo_width()), 
                         width = int(nameCustomerFrame.winfo_height() * 0.95))
    nameAddInput.pack(side=tk.LEFT, pady=5)

    SexCustomerFrame = tk.LabelFrame(TextInputCustomerFrame, width=TextInputCustomerFrame.winfo_width() * 0.10,
                         height=TextInputCustomerFrame.winfo_height() * 0.9, text="Sex")
    SexCustomerFrame.pack_propagate(False)
    SexCustomerFrame.pack(side=tk.LEFT, padx=5)
    
    SexCustomerFrame.update()
    sexAddInput = tk.Text(SexCustomerFrame, height = int(SexCustomerFrame.winfo_width()), 
                         width = int(SexCustomerFrame.winfo_height() * 0.95))
    sexAddInput.pack(side=tk.LEFT, pady=5)

    phoneCustomerFrame = tk.LabelFrame(TextInputCustomerFrame, width=TextInputCustomerFrame.winfo_width() * 0.17,
                         height=TextInputCustomerFrame.winfo_height() * 0.9, text="Phone")
    phoneCustomerFrame.pack_propagate(False)
    phoneCustomerFrame.pack(side=tk.LEFT, padx=5)
    
    phoneCustomerFrame.update()
    phoneAddInput = tk.Text(phoneCustomerFrame, height = int(phoneCustomerFrame.winfo_width()), 
                         width = int(phoneCustomerFrame.winfo_height() * 0.95))
    phoneAddInput.pack(side=tk.LEFT, pady=5)

    addressCustomerFrame = tk.LabelFrame(TextInputCustomerFrame, width=TextInputCustomerFrame.winfo_width() * 0.30,
                         height=TextInputCustomerFrame.winfo_height() * 0.9, text="Address")
    addressCustomerFrame.pack_propagate(False)
    addressCustomerFrame.pack(side=tk.LEFT, padx=5)
    
    addressCustomerFrame.update()
    addressAddInput = tk.Text(addressCustomerFrame, height = int(addressCustomerFrame.winfo_width()), 
                         width = int(addressCustomerFrame.winfo_height() * 0.95))
    addressAddInput.pack(side=tk.LEFT, pady=5)

    petNameCustomerFrame = tk.LabelFrame(TextInputCustomerFrame, width=TextInputCustomerFrame.winfo_width() * 0.13,
                         height=TextInputCustomerFrame.winfo_height() * 0.9, text="Pet")
    petNameCustomerFrame.pack_propagate(False)
    petNameCustomerFrame.pack(side=tk.LEFT, padx=5)
    
    petNameCustomerFrame.update()
    petNameAddInput = tk.Text(petNameCustomerFrame, height = int(petNameCustomerFrame.winfo_width()), 
                         width = int(petNameCustomerFrame.winfo_height() * 0.95))
    petNameAddInput.pack(side=tk.LEFT, pady=5)

    addEmployeeButton = tk.Button(addCustomerFrame, text="ADD", width=30,
                    height=int(addCustomerFrame.winfo_height()*0.96),
                    command=partial(addCustomer, IDAddInput, nameAddInput, sexAddInput, phoneAddInput, addressAddInput, petNameAddInput))
    addEmployeeButton.pack(side=tk.BOTTOM, pady=5, padx=5)

    delCustomerFrame = tk.LabelFrame(mainFrame, width=mainFrame.winfo_width() * 0.9,
                         height=mainFrame.winfo_height() * 0.15, text="Delete Customer")
    delCustomerFrame.pack_propagate(False)
    delCustomerFrame.pack(side=tk.TOP, padx=10, pady=10)
    delCustomerFrame.update()

    IDdelFrame = tk.LabelFrame(delCustomerFrame, width=delCustomerFrame.winfo_width() * 0.07,
                         height=delCustomerFrame.winfo_height() * 0.9, text="ID")
    IDdelFrame.pack_propagate(False)
    IDdelFrame.pack(side=tk.LEFT, padx=10)
    
    IDdelFrame.update()
    IDdelInput = tk.Text(IDdelFrame, height = int(IDdelFrame.winfo_width()), 
                         width = int(IDdelFrame.winfo_height() * 0.95))
    IDdelInput.pack(side=tk.LEFT, pady=5)

    delCustomerButton = tk.Button(delCustomerFrame, text="DELETE", width=10,
                    height=int(delCustomerFrame.winfo_height()*0.8),
                    command=partial(deleteCustomer, IDdelInput))
    delCustomerButton.pack(side=tk.LEFT, padx=10, pady=10)

def addEmployee(ID, name, sex, phone, address):
    petShopSV.addEmployee(ID.get("1.0", "end-1c"),
                          name.get("1.0", "end-1c"),
                          sex.get("1.0", "end-1c"),
                          phone.get("1.0", "end-1c"),
                          address.get("1.0", "end-1c"))

    for i in employeeTable.get_children():
        employeeTable.delete(i)

    listEmployee = petShopSV.getEmloyeeList()


    for idx in range(len(listEmployee)):
        row = listEmployee[idx]
        employeeTable.insert(parent='', index='end', iid=idx,
                      values=(row[0], row[1], row[2], row[3], row[4]))

def deleteEmployee(ID):
    petShopSV.deleteEmployee(ID.get("1.0", "end-1c"))

    for i in employeeTable.get_children():
        employeeTable.delete(i)

    listEmployee = petShopSV.getEmloyeeList()

    for idx in range(len(listEmployee)):
        row = listEmployee[idx]
        employeeTable.insert(parent='', index='end', iid=idx,
                      values=(row[0], row[1], row[2], row[3], row[4]))

def addCustomer(ID, name, sex, phone, address, petName):
    petShopSV.addCustomer(ID.get("1.0", "end-1c"),
                          name.get("1.0", "end-1c"),
                          sex.get("1.0", "end-1c"),
                          phone.get("1.0", "end-1c"),
                          address.get("1.0", "end-1c"),
                          petName.get("1.0", "end-1c"))

    for i in customerTable.get_children():
        customerTable.delete(i)

    customerList = petShopSV.getCustomerList()

    for idx in range(len(customerList)):
        row = customerList[idx]
        customerTable.insert(parent='', index='end', iid=idx,
                      values=(row[0], row[1], row[2], row[3], row[4], row[5]))

def deleteCustomer(ID):
    petShopSV.deleteCustomer(ID.get("1.0", "end-1c"))

    for i in customerTable.get_children():
        customerTable.delete(i)

    customerList = petShopSV.getCustomerList()

    for idx in range(len(customerList)):
        row = customerList[idx]
        customerTable.insert(parent='', index='end', iid=idx,
                      values=(row[0], row[1], row[2], row[3], row[4], row[5]))

def BillDisplay():
    for widget in mainFrame.winfo_children():
        widget.destroy()

    mainFrame.config(width=ScreenWidth * 0.825, height=ScreenHeight)
    mainFrame.update()

    sales_frame = tk.Frame(mainFrame, bd=3, relief=tk.RIDGE)
    sales_frame.pack(side=tk.LEFT, padx=40, pady=20)

    scroll_y = tk.Scrollbar(sales_frame, orient=tk.VERTICAL)
    global sales_list
    sales_list = tk.Listbox(sales_frame, font=("goudy old style", 10), bg="white", yscrollcommand=scroll_y.set)
    scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
    scroll_y.config(command=sales_list.yview)
    sales_list.pack(fill=tk.BOTH, expand=1)
    sales_list.bind("<ButtonRelease-1>", getBillData)

    petShopSV.showBills()

    sales_list.delete(0, tk.END)
    for i in petShopSV.billList:
        sales_list.insert(tk.END, i)

    bill_frame = tk.Frame(mainFrame, bd=3, relief=tk.RIDGE)
    bill_frame.pack(side=tk.LEFT, padx=20)
    bill_frame.place(x=280, y=140, width=470, height=330)

    title_lbl2 = tk.Label(bill_frame, text="Bills", font=('Georgia', 20), bg='orange')
    title_lbl2.pack(side=tk.TOP, fill=tk.X)

    scroll_y2 = tk.Scrollbar(bill_frame, orient=tk.VERTICAL)
    global bill_area
    bill_area = tk.Text(bill_frame, bg="lightyellow", yscrollcommand=scroll_y2.set)
    scroll_y2.pack(side=tk.RIGHT, fill=tk.Y)
    scroll_y2.config(command=bill_area.yview)
    bill_area.pack(fill=tk.BOTH, expand=1)

def getBillData(event):
    index = sales_list.curselection()
    if index:
        file_name = sales_list.get(index)
        bill_area.delete('1.0', tk.END)
        with open(f'bills/{file_name}', 'r', encoding='utf-8') as fp:
            for line in fp:
                bill_area.insert(tk.END, line.encode('utf-8'))
    
def showOrderPage():
    homeButton.config(style="success.Outline.TButton")
    OrderButton.config(style="success.TButton")
    receiptButton.config(style="success.Outline.TButton")
    exitButton.config(style="success.Outline.TButton")
    employeeButton.config(style="success.Outline.TButton")
    customerButton.config(style="success.Outline.TButton")
    BillButton.config(style="success.Outline.TButton")
    petShopSV.mainFrameStatus = 2
    petShopSV.clearListOrder()
    showOrderAndImport()

def showReceiptPage():
    homeButton.config(style="success.Outline.TButton")
    OrderButton.config(style="success.Outline.TButton")
    receiptButton.config(style="success.TButton")
    exitButton.config(style="success.Outline.TButton")
    employeeButton.config(style="success.Outline.TButton")
    customerButton.config(style="success.Outline.TButton")
    BillButton.config(style="success.Outline.TButton")
    petShopSV.mainFrameStatus = 3
    petShopSV.clearListOrder()
    showOrderAndImport()

def showHomePage():
    homeButton.config(style="success.TButton")
    OrderButton.config(style="success.Outline.TButton")
    receiptButton.config(style="success.Outline.TButton")
    exitButton.config(style="success.Outline.TButton")
    employeeButton.config(style="success.Outline.TButton")
    customerButton.config(style="success.Outline.TButton")
    BillButton.config(style="success.Outline.TButton")
    petShopSV.mainFrameStatus = 1
    homePageDisplay()

def showEmployee():
    homeButton.config(style="success.Outline.TButton")
    OrderButton.config(style="success.Outline.TButton")
    receiptButton.config(style="success.Outline.TButton")
    exitButton.config(style="success.Outline.TButton")
    employeeButton.config(style="success.TButton")
    customerButton.config(style="success.Outline.TButton")
    BillButton.config(style="success.Outline.TButton")
    petShopSV.mainFrameStatus = 4
    EmployeeDisplay()

def showCustomer():
    homeButton.config(style="success.Outline.TButton")
    OrderButton.config(style="success.Outline.TButton")
    receiptButton.config(style="success.Outline.TButton")
    exitButton.config(style="success.Outline.TButton")
    employeeButton.config(style="success.Outline.TButton")
    customerButton.config(style="success.TButton")
    BillButton.config(style="success.Outline.TButton")
    petShopSV.mainFrameStatus = 4
    CustomterDisplay()

def showBill():
    homeButton.config(style="success.Outline.TButton")
    OrderButton.config(style="success.Outline.TButton")
    receiptButton.config(style="success.Outline.TButton")
    exitButton.config(style="success.Outline.TButton")
    employeeButton.config(style="success.Outline.TButton")
    customerButton.config(style="success.Outline.TButton")
    BillButton.config(style="success.TButton")
    petShopSV.mainFrameStatus = 4
    BillDisplay()

homeButton = ttk.Button(menuBar, text="Home", style="success.Outline.TButton", command=showHomePage)
OrderButton = ttk.Button(menuBar, text="Order", style="success.Outline.TButton", command=showOrderPage)
receiptButton = ttk.Button(menuBar, text="Receipt", style="success.Outline.TButton", command=showReceiptPage)
employeeButton = ttk.Button(menuBar, text="Employee", style="success.Outline.TButton", command=showEmployee)
customerButton = ttk.Button(menuBar, text="Customer", style="success.Outline.TButton", command=showCustomer)
BillButton = ttk.Button(menuBar, text="Bill", style="success.Outline.TButton", command=showBill)
exitButton = ttk.Button(menuBar, text="Exit", style="success.Outline.TButton", command=root.destroy)

homeButton.pack(side="top", fill=ttk.BOTH, pady=10)
OrderButton.pack(side="top", fill=ttk.BOTH, pady=10)
receiptButton.pack(side="top", fill=ttk.BOTH, pady=10)
employeeButton.pack(side="top", fill=ttk.BOTH, pady=10)
customerButton.pack(side="top", fill=ttk.BOTH, pady=10)
BillButton.pack(side="top", fill=ttk.BOTH, pady=10)
exitButton.pack(side="top", fill=ttk.BOTH, pady=10)

showHomePage()


root.mainloop()

petShopSV.closeService()