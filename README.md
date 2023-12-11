# e-commerce
An online shop for providing and selling products to customers which consists of user profiles, product details, comments and other features.

* The shop is connected to Iranian banks gateway and the user can make online purchases
* Admin can check the buy process and tracking code with additional model(Payment) and default Iranian bank gateway model
* With custom user model(Account) user can create, sign-in and sign-out his/her account
* Profile
  * Edit information
  * Profile image
  * Change password
  * Revceive the reset paswword email
* Sort products by category

* The Cart model handle products that user selected to buy
  * Show number of items in a badget
  * Increase and decrease quantity
  * Total price


## Installation
To use IranianBankGateWay you should use python version 3.8 or higher.

You can write your own favorite name instead of 'env'.

Install the virtual environment:
```
python3.9 -m venv env
```
Also you can use this for install the virtual environment:
```
pip install virtualenv
virtualenv env
```

Now active your virtual environment:
```
env\Scripts\activate
```

Clone the project:
```
https://github.com/alijdst/e-commerce.git
```

First check you are in the project directory:
```
cd e-commerce
```
then install packages you need for this project from requirements.txt on your own virtual environment:
```
pip install -r requirements.txt
```
If your default python version is lower than 3.8 use this:
```
py -3.9 -m pip install -r requirements.txt
```

Now run the project:
```
python manage.py runserver
```
