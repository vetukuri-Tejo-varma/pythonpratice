#ATMOperation.py---file name and module name
from ATMExceptpt import DepositError,WithdrawError, InSuffFundError
bal=500 # Global Variable
def  deposit():
	damt=float(input("Enter the amout for depositing:")) # implcitly ValueError is raising
	if(damt<=0):
		raise DepositError
	else:
		global bal
		bal=bal+damt
		print("Ur Account xxxxxxxxx123 Crediated with INR:{}".format(damt))
		print("Now Ur Bal:{}".format(bal))


def  withdraw():
	global bal
	wamt=float(input("Enter the amout for Withdraw:")) # implcitly ValueError is raising
	if(wamt<=0):
		raise WithdrawError
	elif(wamt+500>bal):
		raise InSuffFundError
	else:
		bal=bal-wamt
		print("Ur Account xxxxxxxxx123 debited by INR:{}".format(wamt))
		print("Now Ur Bal:{}".format(bal))


def  balenq():
	print("Ur Account xxxxxxxxx123 Bal INR :{}".format(bal))