#TupleS Are Changeable But One of the Way to change Tuples value It's Conver Tuples into List than Again Convet List into Tuples

x=("apple","amay","banana")
print("==================Before=================")
print(x)

y=list(x)
y[1]="kiwi"
x=tuple(y)
print("==================After==================")
print(x)
