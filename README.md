# SwapEat 🍽️

SwapEat is a Django-based web platform that allows users to swap and share food efficiently.

## 🌍 Live Website
👉 [Visit SwapEat](https://grieving-timmie-swapeat-5e816b1d.koyeb.app)

## 🚀 Features
- User authentication and profile management
- Food listing with images and descriptions
- Live chat using Django Channels
- Secure payment integration

## 🛠️ Installation
To set up the project locally, follow these steps:

```sh
git clone <https://github.com/Naved20/swapeat>
cd <swapeat>
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
