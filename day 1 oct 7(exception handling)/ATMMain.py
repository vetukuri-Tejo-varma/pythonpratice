#ATMMain.py--main program
import sys
from ATMMenu import menu
from ATMExceptpt import DepositError,WithdrawError, InSuffFundError
from ATMOperation import deposit,withdraw,balenq
while(True):
	try:
		menu()
		ch=int(input("Enter Ur Choice:"))
		match(ch):
			case 1:
				try:
					deposit()
				except ValueError:
					print("Don't Enter Strs , Symbols and ALNUms for Deposits:")
				except DepositError:
					print("Don't Enter -ve / zero for Deposits")

			case 2: 
				try:
					withdraw()
				except ValueError:
					print("Don't Enter Strs , Symbols and ALNUms for Withdraw:")
				except WithdrawError:
					print("Don't Enter -ve / zero for Withdraw")
				except InSuffFundError:
					print("Ur Account does not have sufficient Funds:")
				
			case 3:
				balenq()

			case 4:
				print("\tThx for using this program")
				sys.exit()
			case _:
				print("Ur Selection of Operation is Wrong-Try again")
	except ValueError:
		print("Don't enter strs / symbols and alnums for choice Value:")