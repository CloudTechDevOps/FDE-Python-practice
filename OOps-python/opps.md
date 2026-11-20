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

## Example: Encapsulation

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

```python
class Payment:
    def pay(self, amount):
        print("Processing payment")


class GooglePay(Payment):
    def pay(self, amount):
        print("Paid through Google Pay")


class PhonePe(Payment):
    def pay(self, amount):
        print("Paid through PhonePe")
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

---

## Abstraction

Hides implementation details and exposes essential operations.

### Real-time scenario

Imagine you visit an ATM and withdraw ₹2,000.

**What the customer is allowed to do**

1. Insert ATM card.
2. Enter PIN.
3. Select Withdraw.
4. Enter amount.
5. Receive cash.

**What is hidden from the customer?**

1. How the bank verifies the PIN.
2. How the bank connects to its database.
3. How the account balance is checked.
4. How the transaction is processed.
5. How the bank updates the balance.

The customer uses the functionality without needing to know the internal implementation.

---

## Task: Student Marks

Create a `Student` class.

Requirements:

1. Create private variable `__marks = 85`.
2. Create `show_marks()` method.
3. Create `update_marks(new_marks)` method.
4. Try modifying marks directly from outside.
