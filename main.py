import  os
from tkinter import *
from reportlab.pdfgen import canvas
from tkinter import filedialog
import random

import mysql.connector

# connecting to abgs database in localhost
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="abgs"
    )

# getting a cursor in the database
mycursor = db.cursor()

# main class
class AutoBillGS:
   # serial is the variable that counts the number of items in the bill and does their indexing
   serial = 1

   # lst is the main list that will contain five attributes that are [serial], [item name], [item price], [item quantity] and [item price * item quantity]
   lst = [[]]

   def __init__(self, root):
       self.root = root
       # set the title for the tkinter window
       self.root.title("Automatic Bill Generation System")
       # setting the dimensions of the tkinter window
       self.root.geometry("750x800")

       # creating frame in the window
       self.frame=Frame(self.root, bg="#121212")
       self.frame.place(x=80, y=20, width=600, height=700)

       # creating the heading label with appropriate style
       Label(self.frame, text="Enter Your Company Details", font=("times new roman", 30, "bold"), bg="#4d4988", fg="white", bd=0).place(width=600, height=75)

       # creating the company name label and the corresponding entry to get company name from the user
       Label(self.frame, text="Company Name", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(x=50, y=80)
       self.company_name=Entry(self.frame,font=("times new roman", 15), bg="white", fg="black")
       self.company_name.place(x=270, y=80, width=300, height=35)

       # creating the company address label and the corresponding entry to get company address from the user
       Label(self.frame, text="Company Address", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(x=50, y=140)
       self.address= Entry(self.frame, font=("times new roman", 15), bg="light grey")
       self.address.place(x=270, y=140, width=300,height=35)

       # creating the company city label and the corresponding entry to get company city from the user
       Label(self.frame, text="Company City", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(x=50, y=200)
       self.city = Entry(self.frame, font=("times new roman", 15), bg="light grey")
       self.city.place(x=270, y=200, width=300, height=35)

       # creating the company phone number label and the corresponding entry to get company phone number from the user
       Label(self.frame, text="Company Number", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(x=50, y=260)
       self.compno = Entry(self.frame, font=("times new roman", 15), bg="light grey")
       self.compno.place(x=270, y=260, width=300, height=35)

       # creating the company date of transaction label and the corresponding entry to get date of transaction from the user
       Label(self.frame, text="Date of Transaction\n(DD/MM/YYYY)", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(x=50, y=320)
       self.date = Entry(self.frame, font=("times new roman", 15), bg="light grey")
       self.date.place(x=270, y=320, width=300, height=35)

       # creating the customer phone number label and the corresponding entry to get customer phone number from the user
       Label(self.frame, text="Customer Contact", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(x=50, y=380)
       self.contact = Entry(self.frame, font=("times new roman", 15), bg="light grey")
       self.contact.place(x=270, y=380, width=300, height=35)

       # creating the customer name label and the corresponding entry to get customer name from the user
       Label(self.frame, text="Customer Name", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(x=50, y=440)
       self.c_name = Entry(self.frame, font=("times new roman", 15), bg="light grey")
       self.c_name.place(x=270, y=440, width=300, height=35)

       # creating the authorized signatory label and the corresponding entry to get authorized signature in words from the user
       Label(self.frame, text="Authorized Signatory", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(x=50, y=500)
       self.aus = Entry(self.frame, font=("times new roman", 15), bg="light grey")
       self.aus.place(x=270, y=500, width=300, height=35)

       # creating the company image label
       Label(self.frame, text="Company Image", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(
           x=50, y=560)

       # browse file to get the company logo
       Button(self.frame, text="Browse Files", font=("times new roman", 14), command=self.browse).place(x=270, y=560)

       # to retrieve an already existing invoice
       Button(self.frame, text="Get Existing Invoice", command=self.getExistingInvoice, font=("times new roman", 14), fg="white", cursor="hand2", bg="#B00857").place(x=350, y=640, width=180, height=40)

       # submit new details
       Button(self.frame, text="Submit Details", command=self.enterItemDetails, font=("times new roman", 14), fg="white",cursor = "hand2", bg = "#B00857").place(x = 50, y = 640, width = 180, height = 40)

   def enterItemDetails(self):
       self.lst.clear()
       self.root.geometry("750x800")

       # creating frame in the window
       self.frame=Frame(self.root, bg="#121212")
       self.frame.place(x=80, y=20, width=600, height=700)

       # creating the heading label with appropriate style
       Label(self.frame, text="Purchase Enteries", font=("times new roman", 30, "bold"), bg="#4d4988", fg="white", bd=0).place(width=600, height=75)

       # creating the item name label and the corresponding entry to get item names from user
       Label(self.frame, text="Item Name", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(x=50, y=80)
       self.item_name=Entry(self.frame,font=("times new roman", 15), bg="white", fg="black")
       self.item_name.place(x=270, y=80, width=300, height=35)

       # creating the item price label and the corresponding entry to get item prices from user
       Label(self.frame, text="Item Price", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(x=50, y=140)
       self.item_price= Entry(self.frame, font=("times new roman", 15), bg="light grey")
       self.item_price.place(x=270, y=140, width=300,height=35)

       # creating the item quantity label and the corresponding entry to get item quantities from user
       Label(self.frame, text="Item Quantity", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(x=50, y=200)
       self.item_qty = Entry(self.frame, font=("times new roman", 15), bg="light grey")
       self.item_qty.place(x=270, y=200, width=300, height=35)

       # to push the entered item names and their corresponding to the database and get ready to create the pdf
       Button(self.frame, text="Make Entry", command=self.insertElement, font=("times new roman", 14), fg="white", cursor="hand2", bg="#B00857").place(x=50, y=540, width=180, height=40)

       # to generate the invoice using all the data entered by the user
       Button(self.frame, text="Submit Entries", command=self.generate_invoice, font=("times new roman", 14), fg="white",cursor = "hand2", bg = "#B00857").place(x = 50, y = 640, width = 180, height = 40)

   def getExistingInvoice(self):

       # creating frame in the window
       self.frame = Frame(self.root, bg="#121212")
       self.frame.place(x=80, y=20, width=600, height=700)

       # creating the heading label with appropriate style
       Label(self.frame, text="Existing Invoice", font=("times new roman", 30, "bold"), bg="#4d4988", fg="white", bd=0).place(width=600, height=75)

       # creating the customer label and the corresponding entry to get customer name from the user
       Label(self.frame, text="Customer Name", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(x=50, y=80)
       self.get_customer_name = Entry(self.frame, font=("times new roman", 15), bg="white", fg="black")
       self.get_customer_name.place(x=270, y=80, width=300, height=35)

       # creating the date of purchase label and the corresponding entry to get date of purchase from the user
       Label(self.frame, text="Date of Purchase\n(DD/MM/YYYY)", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(x=50,                                                                   y=140)
       self.dop = Entry(self.frame, font=("times new roman", 15), bg="light grey")
       self.dop.place(x=270, y=140, width=300, height=35)

       # to search for already existing invoices using the details entered by the user
       Button(self.frame, text="Search", command=self.search, font=("times new roman", 14), fg="white", cursor="hand2", bg="#B00857").place(x=50, y=540, width=180, height=40)

   def search(self):
       # following mysql statement gets all the details of the existing invoice using the entered details
       mycursor.execute(f'select * from company natural join customer natural join purchase where customer_name = "{self.get_customer_name.get()}" and date = "{self.dop.get()}";')

       # following are the variables used to contain the data that will be used to fill the pdf
       self.lst.clear()
       generated_invoice_no = -1
       c_name = ""
       file_name = ""
       company_name = ""
       address = ""
       city = ""
       compno = -1
       date = ""
       contact = -1

       # after getting the data using a for loop and iterating over all the entries and pushing them in to the main list which will be the pdf input
       for x in mycursor:
           generated_invoice_no = x[0]
           self.c_name = x[6]
           self.file_name = f"{x[5]}"
           self.company_name = f"{x[1]}"
           self.address = f"{x[2]}"
           self.city = f"{x[3]}"
           self.compno = x[4]
           self.date = f"{x[8]}"
           self.contact = x[7]
           templst = []
           templst.append(self.serial)
           self.serial = self.serial + 1
           templst.append(x[9])
           templst.append(int(x[10]))
           templst.append(int(x[11]))
           templst.append(int(x[10]) * int(x[11]))
           self.lst.append(templst)

       # HEIGHT and WIDTH are just the postion coordinates of item details on the pdf
       HEIGHT = 130
       WIDTH = [25, 75, 125, 148, 173]

       # creating a new canvas of customer name and custome size
       c = canvas.Canvas(f'{generated_invoice_no}_{self.c_name}.pdf', pagesize=(200, 250), bottomup=0)

       # setting the color of the text on the pdf
       c.setFillColorRGB(0, 0, 0)  # set color of text of the entire pdf

       # all lines drawn are considered from top to bottom & from right to left

       # line horizontal 1
       c.line(5, 45, 195, 45)

       # line horizontal 3
       c.line(15, 120, 185, 120)

       # setting the font style and size
       c.setFont("Times-Bold", 5)

       # iterating over the main list and putting the data to their respective postions on the pdf
       for i in range(len(self.lst)):
           for j in range(len(self.lst[0])):
               c.drawCentredString(WIDTH[j], HEIGHT, str(self.lst[i][j]))
           HEIGHT = HEIGHT + 10

       # line vertical 2
       c.line(35, 108, 35, 210)

       # line vertical 3
       c.line(115, 108, 115, 210)

       # line vertical 4
       c.line(135, 108, 135, 210)

       # line vertical 5
       c.line(160, 108, 160, 210)

       # line horizontal 5
       c.line(15, 220, 185, 220)

       # line horizontal 4
       c.line(15, 210, 185, 210)

       # sum is the variable the will contain the subtotal after the for loop executes
       sum = 0
       for x in self.lst:
           sum += x[4]

       # following lines contain placing entered data to their respective positions
       c.drawCentredString(148, 218, "Subtotal: ")
       c.drawCentredString(173,218, str(sum))
       c.translate(10, 40)
       c.scale(1, -1)

       # drawing the image below
       c.drawImage(f'{self.file_name}', 0, 0, width=50, height=30)
       c.scale(1, -1)
       c.translate(-10, -40)

       # drawing the entered company name at a position
       c.setFont("Times-Bold", 10)
       c.drawRightString(180, 20, self.company_name)

       # drawing the entered company address at a position
       c.setFont("Times-Bold", 5)
       c.drawRightString(180, 25, self.address)

       # drawing the entered company city at a position
       c.drawRightString(180, 30, self.city)

       # drawing the entered company phone number at a position
       c.setFont("Times-Bold", 6)
       c.drawRightString(180, 35, "Ph: " + str(self.compno))

       c.setFont("Times-Bold", 8)
       c.drawCentredString(100, 55, "INVOICE")
       c.setFont("Times-Bold", 5)
       c.drawRightString(70, 70, "Invoice No. :")
       c.drawRightString(100, 70, f"{generated_invoice_no}")
       c.drawRightString(70, 80, "Date :")
       c.drawRightString(100, 80, self.date)
       c.drawRightString(70, 90, "Customer Name :")
       c.drawRightString(100, 90, self.c_name)
       c.drawRightString(70, 100, "Phone No. :")
       c.drawRightString(100, 100, str(self.contact))
       c.roundRect(15, 108, 170, 130, 10, stroke=1, fill=0)
       c.drawCentredString(25, 118, "S.No.")
       c.drawCentredString(75, 118, "Item")
       c.drawCentredString(125, 118, "Price")
       c.drawCentredString(148, 118, "Qty.")
       c.drawCentredString(173, 118, "Total")
       c.drawString(30, 230, "This is system generated invoice and does not require a signature.")
       c.showPage()
       c.save()
       os.startfile(f'{generated_invoice_no}_{self.c_name}.pdf')

   # following function is used to enter the item details into the main list
   def insertElement(self):
       templst = []
       templst.append(self.serial)
       self.serial = self.serial + 1
       templst.append(self.item_name.get())
       templst.append(int(self.item_price.get()))
       templst.append(int(self.item_qty.get()))
       templst.append(int(self.item_price.get()) * int(self.item_qty.get()))
       self.lst.append(templst)
       self.item_name.delete(0, END)
       self.item_price.delete(0, END)
       self.item_qty.delete(0, END)

   # following function is used to browse the local storage and get the company logo and set the corresponding label to its name
   def browse(self):
      self.file_name = filedialog.askopenfilename(title="Select a File")
      Label(self.frame, text=os.path.basename(self.file_name), font=("times new roman", 15)).place(x=270, y=600)

   # following code contains generating invoice pdf
   def generate_invoice(self):
        # getting a random invoice number within the specified range
        generated_invoice_no = random.randint(1000000, 9999999)

        # following mysql codes enter the company and customer values into their corresponding tables and commits the new changes
        mycursor.execute(f'insert into company values({generated_invoice_no}, "{self.company_name.get()}", "{self.address.get()}", "{self.city.get()}", {self.compno.get()}, "{self.file_name}");')
        db.commit()
        mycursor.execute(f'insert into customer values({generated_invoice_no}, "{self.c_name.get()}", {self.contact.get()}, "{self.date.get()}");')
        db.commit()

        # HEIGHT and WIDTH are just the coordinates of the item details on the pdf
        HEIGHT = 130
        WIDTH = [25, 75, 125, 148, 173]

        # creating a canvas with a custom name and custom size
        c = canvas.Canvas(f'{generated_invoice_no}_{self.c_name.get()}.pdf', pagesize=(200, 250), bottomup=0)

        # setting the font color of the canvas
        c.setFillColorRGB(0, 0, 0) # set color of text of the entire pdf

        # all lines drawn are considered from top to bottom & from right to left

        # line horizontal 1
        c.line(5, 45, 195, 45)

        # line horizontal 3
        c.line(15, 120, 185, 120)

        # setting the font style and size
        c.setFont("Times-Bold", 5)

        # following for loop iterates over the main list and puts the item details at their respective positions on the pdf
        # it also enters the item details into the corresponding table in the database and commits the changes
        for i in range(len(self.lst)):
            for j in range(len(self.lst[0])):
                c.drawCentredString(WIDTH[j], HEIGHT, str(self.lst[i][j]))
            mycursor.execute(f'insert into purchase values({generated_invoice_no}, "{self.lst[i][1]}", {self.lst[i][2]}, {self.lst[i][3]});')
            db.commit()
            HEIGHT = HEIGHT + 10

        # following lines are drawing the look of the bill on the canvas

        # line vertical 2
        c.line(35, 108, 35, 210)

        # line vertical 3
        c.line(115, 108, 115, 210)

        # line vertical 4
        c.line(135, 108, 135, 210)

        # line vertical 5
        c.line(160, 108, 160, 210)

        # line horizontal 5
        c.line(15, 220, 185, 220)

        # line horizontal 4
        c.line(15, 210, 185, 210)

        # sum is the variable that will contain the subtotal after the for loop executes
        sum = 0
        for x in self.lst:
            sum += x[4]

        c.drawCentredString(148, 218, "Subtotal: ")
        c.drawCentredString(173, 218, str(sum))
        c.translate(10, 40)
        c.scale(1, -1)

        # drawing the image below
        c.drawImage(f'{self.file_name}', 0, 0, width=50, height=30)
        c.scale(1, -1)
        c.translate(-10, -40)

        # drawing the entered company name at a position
        c.setFont("Times-Bold", 10)
        c.drawRightString(180, 20, self.company_name.get())

        # drawing the entered company address at a position
        c.setFont("Times-Bold", 5)
        c.drawRightString(180, 25, self.address.get())

        # drawing the entered company city at a position
        c.drawRightString(180, 30, self.city.get())

        # drawing the entered company phone number at a position
        c.setFont("Times-Bold", 6)
        c.drawRightString(180, 35, "Ph: " + self.compno.get())

        c.setFont("Times-Bold", 8)
        c.drawCentredString(100, 55, "INVOICE")

        # following codes just put the entered details by the user into their respective positions on the pdf
        c.setFont("Times-Bold", 5)
        c.drawRightString(70, 70, "Invoice No. :")
        c.drawRightString(100, 70, f"{generated_invoice_no}")
        c.drawRightString(70, 80, "Date :")
        c.drawRightString(100, 80, self.date.get())
        c.drawRightString(70, 90, "Customer Name :")
        c.drawRightString(100, 90, self.c_name.get())
        c.drawRightString(70, 100, "Phone No. :")
        c.drawRightString(100, 100, self.contact.get())
        c.roundRect(15, 108, 170, 130, 10, stroke=1, fill=0)
        c.drawCentredString(25, 118, "S.No.")
        c.drawCentredString(75, 118, "Item")
        c.drawCentredString(125, 118, "Price")
        c.drawCentredString(148, 118, "Qty.")
        c.drawCentredString(173, 118, "Total")
        c.drawString(30, 230, "This is system generated invoice and does not require a signature.")
        c.showPage()
        c.save()
        os.startfile(f'{generated_invoice_no}_{self.c_name.get()}.pdf')

def main():
   # create tkinter window
   root = Tk()
   # creating object for class AutoBillGS
   obj = AutoBillGS(root)
   # start the GUI
   root.mainloop()
if __name__ == "__main__":
   # calling main function
   main()
