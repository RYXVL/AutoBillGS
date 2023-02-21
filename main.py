import  os
from tkinter import *
from reportlab.pdfgen import canvas
from tkinter import filedialog
import random


# main class
class AutoBillGS:
   serial = 1

   lst = [[]]
   # lst = [[1, 'Paper', 10, 2],
   #        [2, 'Coffee', 100, 1],
   #        [3, 'Salt', 50, 1],
   #        [4, 'Sugar', 25, 3],
   #        [5, 'Cookies', 200, 10]]

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

       # creating the company name label and the corresponding entry to get data from user
       Label(self.frame, text="Company Name", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(x=50, y=80)
       self.company_name=Entry(self.frame,font=("times new roman", 15), bg="white", fg="black")
       self.company_name.place(x=270, y=80, width=300, height=35)

       # creating the address label and the corresponding entry to get data from user
       Label(self.frame, text="Address", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(x=50, y=140)
       self.address= Entry(self.frame, font=("times new roman", 15), bg="light grey")
       self.address.place(x=270, y=140, width=300,height=35)

       Label(self.frame, text="City", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(x=50, y=200)
       self.city = Entry(self.frame, font=("times new roman", 15), bg="light grey")
       self.city.place(x=270, y=200, width=300, height=35)

       Label(self.frame, text="Company Number", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(
           x=50, y=260)
       self.compno = Entry(self.frame, font=("times new roman", 15), bg="light grey")
       self.compno.place(x=270, y=260, width=300, height=35)

       Label(self.frame, text="Date", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(
           x=50, y=320)
       self.date = Entry(self.frame, font=("times new roman", 15), bg="light grey")
       self.date.place(x=270, y=320, width=300, height=35)

       Label(self.frame, text="Contact", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(
           x=50, y=380)
       self.contact = Entry(self.frame, font=("times new roman", 15), bg="light grey")
       self.contact.place(x=270, y=380, width=300, height=35)

       Label(self.frame, text="Customer Name", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(
           x=50, y=440)
       self.c_name = Entry(self.frame, font=("times new roman", 15), bg="light grey")
       self.c_name.place(x=270, y=440, width=300, height=35)

       Label(self.frame, text="Authorized Signatory", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(
           x=50, y=500)
       self.aus = Entry(self.frame, font=("times new roman", 15), bg="light grey")
       self.aus.place(x=270, y=500, width=300, height=35)

       Label(self.frame, text="Company Image", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(
           x=50, y=560)

       # browse File
       Button(self.frame, text="Browse Files", font=("times new roman", 14), command=self.browse).place(x=270, y=560)

       # submit details
       Button(self.frame, text="Submit Details", command=self.enterItemDetails, font=("times new roman", 14), fg="white",cursor = "hand2", bg = "#B00857").place(x = 50, y = 640, width = 180, height = 40)

   def enterItemDetails(self):
       self.lst.clear()
       self.root.geometry("750x800")

       # creating frame in the window
       self.frame=Frame(self.root, bg="#121212")
       self.frame.place(x=80, y=20, width=600, height=700)

       # creating the heading label with appropriate style
       Label(self.frame, text="Purchase Enteries", font=("times new roman", 30, "bold"), bg="#4d4988", fg="white", bd=0).place(width=600, height=75)

       # creating the company name label and the corresponding entry to get data from user
       Label(self.frame, text="Item Name", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(x=50, y=80)
       self.item_name=Entry(self.frame,font=("times new roman", 15), bg="white", fg="black")
       self.item_name.place(x=270, y=80, width=300, height=35)

       # creating the address label and the corresponding entry to get data from user
       Label(self.frame, text="Item Price", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(x=50, y=140)
       self.item_price= Entry(self.frame, font=("times new roman", 15), bg="light grey")
       self.item_price.place(x=270, y=140, width=300,height=35)

       Label(self.frame, text="Item Quantity", font=("times new roman", 15, "bold"), bg="#121212", fg="white").place(x=50, y=200)
       self.item_qty = Entry(self.frame, font=("times new roman", 15), bg="light grey")
       self.item_qty.place(x=270, y=200, width=300, height=35)

       Button(self.frame, text="Make Entry", command=self.insertElement, font=("times new roman", 14),
              fg="white", cursor="hand2", bg="#B00857").place(x=50, y=540, width=180, height=40)

       Button(self.frame, text="Submit Entries", command=self.generate_invoice, font=("times new roman", 14), fg="white",cursor = "hand2", bg = "#B00857").place(x = 50, y = 640, width = 180, height = 40)


   def insertElement(self):
       templst = []
       templst.append(self.serial)
       self.serial = self.serial + 1
       templst.append(self.item_name.get())

       templst.append(int(self.item_price.get()))
       templst.append(int(self.item_qty.get()))
       templst.append(int(self.item_price.get()) * int(self.item_qty.get()))
       self.lst.append(templst)
       # self.item_name.em


   def browse(self):
      self.file_name = filedialog.askopenfilename(title="Select a File")
      Label(self.frame, text=os.path.basename(self.file_name), font=("times new roman", 15)).place(x=270, y=600)


   def generate_invoice(self):
        HEIGHT = 130
        WIDTH = [25, 75, 125, 148, 173]
        c = canvas.Canvas("Bill.pdf", pagesize=(200, 250), bottomup=0)
        c.setFillColorRGB(0, 0, 0) # set color of text of the entire pdf
        # all lines drawn are considered from top to bottom & from right to left
        c.line(5, 45, 195, 45) # line horizontal 1
        c.line(15, 120, 185, 120) # line horizontal 3
        c.setFont("Times-Bold", 5)
        for i in range(len(self.lst)):
            for j in range(len(self.lst[0])):
                c.drawCentredString(WIDTH[j], HEIGHT, str(self.lst[i][j]))
                # WIDTH = WIDTH + 20
            HEIGHT = HEIGHT + 10
        c.line(35, 108, 35, 220) # line vertical 2
        c.line(115, 108, 115, 220) # line vertical 3
        c.line(135, 108, 135, 220) # line vertical 4
        c.line(160, 108, 160, 220) # line vertical 5
        c.line(15, 220, 185, 220) # line horizontal 4
        c.translate(10, 40)
        c.scale(1, -1)
        # drawing the image below
        c.drawImage(self.file_name, 0, 0, width=50, height=30)
        c.scale(1, -1)
        c.translate(-10, -40)
        # drawing the entered company name at a position
        c.setFont("Times-Bold", 10)
        c.drawRightString(180, 20, self.company_name.get())
        # drawing the entered company address at a position
        c.setFont("Times-Bold", 5)
        c.drawRightString(180, 25, self.address.get())
        # drawing the entered company city at a position
        c.drawRightString(180, 30, self.city.get() + ", India")
        # drawing the entered company phone number at a position
        c.setFont("Times-Bold", 6)
        c.drawRightString(180, 35, "Ph: " + self.compno.get())

        c.setFont("Times-Bold", 8)
        c.drawCentredString(100, 55, "INVOICE")

        c.setFont("Times-Bold", 5)
        c.drawRightString(70, 70, "Invoice No. :")
        c.drawRightString(100, 70, f"{random.randint(1000000, 9999999)}")
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
        # c.drawRightString(180, 228, self.aus.get())
        # c.drawRightString(180, 235, "Signature"
        c.showPage()
        c.save()
        os.startfile("Bill.pdf")

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
