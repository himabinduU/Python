# Title : Bank_account for multiple users.

import math

list = []
#Bank_account fields
dict = {'name':'none', 'balance':0, 'account_no': 0}
g = 0

#Creating an account
def make_account(name, account):
	seq = ('name', 'balance', 'account_no')
	list.append(dict.fromkeys(seq))
	global g
	list[g]['account_no'] = account
	list[g]['name'] = name
	list[g]['balance'] = 0
	g = g + 1

#If the account number exist than entered money will get deposit, otherwise asks to enter the valid account number.
def deposit(account, amount) :
	i = 0
	while (i < len(list)) :
		if list[i]['account_no'] == account :
			list[i]['balance'] +=  amount
			print "balance: ",list[i]['balance']
			return
		i = i + 1
	print "enter the valid account number orelse create an account"

#If the account number exist than entered money will get withdrawn, otherwise asks to enter the valid account number.
def withdraw(account, amount) :
	i = 0
	while (i < len(list)) :
		if list[i]['account_no'] == account :
			list[i]['balance'] -=  amount
			print list[i]
			return
		i = i + 1
	print "enter the valid account number orelse create an account"

#If the account number exist than it will show the account details along with balance, otherwise asks to enter the valid account number.
def balance_enquiry(account) :
	i = 0
	while (i < len(list)) :
		if list[i]['account_no'] == account :
			print list[i]
			return
		i = i + 1
	print "enter the valid account number orelse create an account"

#User Interface program
def user_interface():
	print ("---------------User Interface---------------")
	print ("|       1. creating an new account         |")
	print ("|	2. depositing the amount           |")
	print ("|	3. withdrawing the amount          |")
	print ("|	4. balance enquiry                 |")
	print ("|	5. exit                            |")
	print ("--------------------------------------------")
	return int(input())

key = user_interface()

#This loop runs until user selects exit option.
while (1) :
		
	if (key == 1):
		print "enter the name"
		name = raw_input()
		print "enter the account number"
		account = int(raw_input())
		make_account(name, account)

	elif (key == 2) :
		print "enter the account number"
		account = int(raw_input())
		print "enter the amount to be deposited"
		amount = int(raw_input())
		print deposit(account, amount)

	elif (key == 3) :
		print "enter the account number"
		account = int(raw_input())
		print "enter the amount to be withdrawn"
		amount = int(raw_input())
		print withdraw(account, amount)

	elif (key == 4) :
		print "enter the account number"
		account = int(raw_input())
		balance_enquiry(account)
	
	elif (key == 5) :
		exit(0)

	else :
		print "Please enter the valid choice"

	key = user_interface()
