from tkinter import *
from tkinter import messagebox

#This is essentially the header
pizza = Tk()
pizza.geometry("600x500")
pizza.title("Bay's pizza app")

#first button for name
name_label = Label(pizza, text="What is your first and last name? ")
name_label.grid(row=0, column=0)

name_entry = Entry(pizza, width=50)
name_entry.grid(row=0, column=1)

#second button for address
address_label = Label(pizza, text="What is your delivery address? ")
address_label.grid(row=1, column=0)

address_entry = Entry(pizza, width=50)
address_entry.grid(row=1, column=1)
#third button for phone number
phone_label = Label(pizza, text="What is your phone number? ")
phone_label.grid(row=2, column=0)

phone_entry = Entry(pizza, width=50)
phone_entry.grid(row=2, column=1)
#various toppings in the list 
my_pizza_list = ["pepperoni", "bacon", "cheese", "mushroom", "olives", "green peppers"]
    #choosing color for toppings box
pizza_list = Listbox(pizza, selectmode=MULTIPLE, bg="White", fg="Black")
pizza_list.grid(row=4,column=1)

for item in my_pizza_list:
    pizza_list.insert(0, item)

def add_pizza():
    result = ""
    for item in pizza_list.curselection():
        result = result + str(pizza_list.get(item)) + "\n"
#this shows under the topping box for what toppings they chose
        add_lbl.config(text="Your Pizza Selection: " + "\n" + result)

add_lbl = Label(pizza, text="")
add_lbl.grid(row=5, column=1)
#button to add pizza once topping selected
add_button = Button(pizza, text="Add Pizza", command= add_pizza)
add_button.grid(row=5, column=0)

def check():
    text1= name_entry.get()
    new_lbl = Label(pizza, text= "Name: " + text1)
    new_lbl.grid(row=5,column=2)

    text2 = address_entry.get()
    new_lbl2 = Label(pizza, text= "Address " + text2)
    new_lbl2.grid(row=6, column=2)

    text3 = phone_entry.get()
    new_lbl3 = Label(pizza, text= "Phone Number: " +text3)
    new_lbl3.grid(row=7,column=2)
    
def delete ():
    pizza_list.delete(0,5)

check_button = Button(pizza, text="Checkout", command=check)
check_button.grid(row=6,column=0)
#delete everything
del_button= Button(pizza, text="Delete Your Order", command=delete)
del_button.grid(row=7,column=0)

drinks = StringVar()
drinks.set("Choose your drink")
#widget to choose various drinks
drink = OptionMenu(pizza, drinks, "Soda", "Beer", "Water")
drink.grid(row=8, column=0)
#button that asks if you want to exit the app and kills it if true
def exitme():
    answer = messagebox.askyesno("Hi", "Are you sure you want to exit? ")
    if answer == 1:
        pizza.destroy()
    else:
        return
        

exit_button = Button(pizza, text="Exit Ordering App",command=exitme)
exit_button.grid(row=4, column=7)














pizza.mainloop()
