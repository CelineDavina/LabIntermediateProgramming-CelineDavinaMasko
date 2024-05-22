class Counter:
    def __init__(self):
        self.count = 0
    
    def reset(self):
        self.count = 0
        
    def click(self):
        self.count += 1

    def getValue(self):
        return self.count

tally = Counter()
tally.reset()
tally.click()
tally.click()
result = tally.getValue() # Result is 2
print(result)
tally.click()
result = tally.getValue() # Result is 3
print(result)

# Mengapa jika perintah tally.reset (line 2 di atas) tidak dijalakan (dihapus), menyebabkan error?
# = karena local value belum diciptakan, sehingga saat tally.click() dijalankan, dia tidak akan tahu value apa yang akan ditambah +1. 


class CashRegister:
    def __init__(self):
        self.itemCount = 0
        self.total = 0.00

    def addItem(self, price):
        self.itemCount += 1
        self.total += price

    def getCount(self):
        return self.itemCount

    def getTotal(self):
        return self.total

# Test the CashRegister class
register1 = CashRegister()
register1.addItem(1.95)
register1.addItem(0.95)
register1.addItem(2.50)

register2 = CashRegister()
register2.addItem(3.75)
register2.addItem(0.15)
register2.addItem(2.25)
register2.addItem(1.80)

print("Register 1 sells", register1.getCount(), "items, with the total amount of $", register1.getTotal())
print("Register 2 sells", register2.getCount(), "items, with the total amount of $", register2.getTotal())


class Fraction:
  def __init__(self, pembilang, penyebut):

    if penyebut == 0:
      raise ValueError("masukkan angka selain 0")

    self.pembilang = pembilang
    self.penyebut = penyebut

    gcd = self._gcd(self.pembilang, self.penyebut)
    self.pembilang //= gcd
    self.penyebut //= gcd

  def _gcd(self, a, b):
    while b != 0:
      a, b = b, a % b
    return a

  def __str__(self):
    return f"{self.pembilang}/{self.penyebut}"

  def to_float(self):
    return self.pembilang / self.penyebut

fraction1 = Fraction(1, 3)
fraction2 = Fraction(7, 2)

print("Fraction 1:", fraction1)
print("Fraction 1 as desimal:", fraction1.to_float()) 
print("Fraction 2:", fraction2) 
print("Fraction 2 as desimal:", fraction2.to_float())