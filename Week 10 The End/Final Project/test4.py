from datetime import date, datetime, timedelta

a  = date.today()
b = date.today().strftime("%Y-%m-%d")
c = datetime.strptime(b, "%Y-%m-%d").date()

e = b.strftime("%A, %B %d, %Y")

d = a + timedelta(days = 6)

print(a)
print(b)
print(c)
print(d)

print(e)
