# When do we use OOPs in Python?

We use Object-Oriented Programming (OOP) when we develop applications that contain multiple entities, data, and related operations.

OOP helps us organize code, reuse functionality, protect data, and maintain large applications easily.

## 1. Real-Time Applications Where We Use OOPs

| Application | Classes | Objects |
|---|---|---|
| Banking | Bank, Account | SBI, HDFC |
| School Management | Student, Teacher | Student1, Teacher1 |
| E-commerce | Product, Customer, Payment | Mobile, Laptop, Customer1 |
| Hospital | Doctor, Patient | Doctor1, Patient1 |
| Employee Management | Employee, Manager | Employee1, Manager1 |
| Food Delivery | Restaurant, Customer, Delivery | Swiggy, Zomato |
| Online Shopping | Cart, Order | Cart1, Order1 |

## 2. Why Do We Use OOPs?

Imagine developing a banking application.

Without OOP, we might write separate variables and functions for every customer.

For example:

```python
customer1_name = "Veera"
customer1_balance = 10000
customer2_name = "Rahul"
customer2_balance = 20000

def deposit1(amount):
    global customer1_balance
    customer1_balance += amount

def deposit2(amount):
    global customer2_balance
    customer2_balance += amount
```

As the number of customers increases, managing the code becomes difficult.

Using OOPs:

```python
class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print(self.name, self.balance)

b1 = Bank("Veera", 10000)
b2 = Bank("Rahul", 20000)

b1.deposit(5000)
b2.deposit(3000)

b1.show_balance()
b2.show_balance()
```

Output:

```
Veera 15000
Rahul 23000
```

Now we can create 100, 1,000, or more customer objects using the same class.

## 3. Four Main OOP Concepts and Their Uses

| Concept | Why do we use it? | Real-time example |
|---|---|---|
| Encapsulation | Control access to data | Bank account balance |
| Inheritance | Reuse existing code | SavingsAccount inherits Bank |
| Polymorphism | Same method, different behaviour | Google Pay, PhonePe |
| Abstraction | Hide implementation details | ATM operations |

---

## Encapsulation

### Real-time example: Bank ATM

Think about an ATM.

Suppose your bank account has ₹50,000.

Can you go to the ATM and directly change your account balance to ₹1,00,000?

No!

Why?

Because the bank does not provide direct access to its internal database.

Instead, the bank provides operations:

1. Check balance.
2. Deposit money.
3. Withdraw money.
4. Transfer money.

```python
class Bank:

    def __init__(self):
        self.__balance = 50000

    def check_balance(self):
        print("Available Balance:", self.__balance)

    def deposit(self, amount):
        self.__balance += amount
        print("Deposit successful")

    def withdraw(self, amount):
        self.__balance -= amount
        print("Withdrawal successful")


# Customer
customer = Bank()

# Check balance
customer.check_balance()

# Deposit
customer.deposit(10000)

# Withdraw
customer.withdraw(5000)

# Check updated balance
customer.check_balance()

# Direct modification attempt  ##### Encapsulation
customer.__balance = 1000000

customer.check_balance()
```

---

## Inheritance

It allows a child class to reuse the code of a parent class without writing the same code again.

Inheritance allows a child class to reuse parent-class methods and attributes while also defining its own functionality.
```python
class Parent:

    def house(self):
        print("Parent owns a house")

    def car(self):
        print("Parent owns a car")


class Child(Parent): #Here, Child(Parent) means the Child class inherits from the Parent class.

    def bike(self):
        print("Child owns a bike")


# Creating child object
c1 = Child() #The Child class can access both parent-class methods and its own methods.

# Accessing parent methods
c1.house()
c1.car()

# Accessing child method
c1.bike()

```
### example-2

```python

class Bank:

    def __init__(self):
        self.__balance = 1000

    def show_balance(self):
        print("Available Balance:", self.__balance)

    def deposit(self, amount):
        self.__balance = amount + self.__balance
        print("Deposited:", amount)


class SavingsAccount(Bank):

    def interest(self):
        print("Savings account interest: 5%")


class CurrentAccount(Bank):

    def business(self):
        print("Business transactions enabled")


# Savings Account
s1 = SavingsAccount()

s1.show_balance()
s1.deposit(500)
s1.show_balance()
s1.interest()


print("----------------")

# Current Account
c1 = CurrentAccount()

c1.show_balance()
c1.deposit(2000)
c1.show_balance()
c1.business()
```

---
## super method

##### First example 
```python
class Parent:

    def display(self):
        print("Parent method")


class Child(Parent):

    def show(self):
        print("Child method")


c1 = Child()

c1.display()  # Parent method
c1.show()     # Child method

#display() belongs to Parent.
#show() belongs to Child.
#Child inherits display() from Parent.
#Both methods have different names, so there is no method overriding.
#We can call both methods directly using the Child object.
```
#### so no need super method ###

===================================================
## Second example – Same method name both using display Child overrides the parent's method (Method Overriding)##
```python
class Parent:

    def display(self):
        print("Parent method")


class Child(Parent):

    def display(self):
        super().display()  # Calls Parent method
        print("Child method")  # Executes Child method


c1 = Child()
c1.display()

#display() belongs to Parent.
#Child also defines display().
#Child overrides the parent's method.
#When we call c1.display(), Python executes the Child method.
```

===================================================================
 
##Second example – Same method name (Method Overriding)##
                ##Super method##
```python
 class Parent:

    def display(self):
        print("Parent method")


class Child(Parent):

    def display(self):
        super().display()
        print("Child method")


c1 = Child()
c1.display()

#display() belongs to Parent.
#Child also defines display().
#Child overrides the parent's method.
#When we call c1.display(), Python executes the Child method.
#super().display() explicitly calls the next implementation, which is Parent's method here.
```

1. Inheritance – Parent and Child classes.
2. Accessing parent methods through child objects.
3. Additional methods in child classes.
4. Method overriding – Same method name in Parent and Child.
5. super() – Reusing the parent's implementation.
6. super().__init__() – Calling the parent constructor.
---
## Polymorphism

### E-commerce Applications

Use case: Amazon, Flipkart.

When customers make payments, they can select different payment methods.

- Google Pay
- PhonePe
- Credit Card
- Cash on Delivery

All use a common `pay()` method but have different implementations.

- Customer selects one payment method.
- Based on the selection, the corresponding object is created.
- The common `pay()` method is called.
- Python executes the method belonging to that object.

```python
class Payment:

    def pay(self, amount):
        print("Processing payment")


class GooglePay(Payment):

    def pay(self, amount):
        print("Paid", amount, "through Google Pay")


class PhonePe(Payment):

    def pay(self, amount):
        print("Paid", amount, "through PhonePe")


class CreditCard(Payment):

    def pay(self, amount):
        print("Paid", amount, "through Credit Card")


class CashOnDelivery(Payment):

    def pay(self, amount):
        print("Cash will be collected on delivery:", amount)


# Customer selects payment method

g = GooglePay()
p = PhonePe()
c = CreditCard()
cod = CashOnDelivery()

g.pay(5000)
p.pay(3000)
c.pay(10000)
cod.pay(2000)

```

---

## Abstraction

The college says every student must submit:
1. Assignment 1
2. Assignment 2
3. Assignment 3
If a student misses Assignment 2, the college doesn't accept the submission.

Similarly:

Abstract class = College rules

Abstract methods = Mandatory assignments

Child class = Student

Creating child object = Accepting the submission
Final concept
Without abstraction, Python doesn't force child classes to implement particular methods.

With abstraction, Python enforces the required methods before allowing an object of the concrete child class to be created.

This is the main benefit of Abstraction


| Without Abstraction                                                            | With Abstraction |

| Developer can forget required methods                                          | Python forces implementation |
| Object can be created even with missing methods                                | Object creation is prevented |
| No common enforced structure                                                   | Common structure is enforced |
| Errors may occur later | Missing implementation is detected at object creation |


```python
from abc import ABC, abstractmethod


class ATM(ABC):

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass


class SBI(ATM):

    def __init__(self):
        self.balance = 10000

    def withdraw(self, amount):
        self.balance -= amount
        print("Withdrawn:", amount)

    def check_balance(self):
        print("Available Balance:", self.balance)

# Creating object
a = SBI()
a.withdraw(2000)
a.check_balance()

```

