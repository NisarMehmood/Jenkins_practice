from practice import ATM


def test1():
  atm = ATM(100)
  assert atm.withdraw() == 0
  
def test2():
  atm = ATM(100)
  assert atm.deposit(100) == 200  



