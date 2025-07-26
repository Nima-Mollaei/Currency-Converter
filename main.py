import tkinter as tk
from tkinter import ttk
import requests

# Dictionary mapping currency codes to their full names
currency_names = {
    "USD": "United States Dollar", "EUR": "Euro", "GBP": "British Pound",
    "JPY": "Japanese Yen", "CNY": "Chinese Yuan", "TRY": "Turkish Lira",
    "AED": "UAE Dirham", "CAD": "Canadian Dollar", "AUD": "Australian Dollar",
    "CHF": "Swiss Franc", "SEK": "Swedish Krona", "NOK": "Norwegian Krone",
    "DKK": "Danish Krone", "INR": "Indian Rupee", "RUB": "Russian Ruble",
    "KRW": "South Korean Won", "SGD": "Singapore Dollar", "HKD": "Hong Kong Dollar"
}

# Function to convert currency using exchangerate-api
def convert_currency():
    try:
        # Get input amount and selected currencies
        amount = float(entry_amount.get())
        from_currency = combo_from.get().upper()
        to_currency = combo_to.get().upper()

        # Send request to exchangerate-api
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()

        # Check if target currency is in the response
        if to_currency not in data['rates']:
            label_result.config(text="❌ Invalid currency code", fg="red")
            return

        # Calculate converted amount
        rate = data['rates'][to_currency]
        converted = amount * rate

        # Get full currency names
        from_name = currency_names.get(from_currency, from_currency)
        to_name = currency_names.get(to_currency, to_currency)

        # Show result
        label_result.config(
            text=f"{amount:,.2f} {from_currency} ({from_name})\n= {converted:,.2f} {to_currency} ({to_name})",
            fg="#0f5132"
        )
    except:
        # Error handling
        label_result.config(text="❌ Please enter a valid amount", fg="red")

# List of currency codes for the dropdowns
currencies = list(currency_names.keys())

# Configure main window
window = tk.Tk()
window.title("💱 Currency Converter")
window.geometry("480x450")
window.config(bg="#e3f2fd")

# Base font
FONT = ("Segoe UI", 12)

# Main frame to hold all widgets
frame = tk.Frame(window, bg="white", bd=2, relief="groove")
frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=400)

# Title label
tk.Label(frame, text="💵 Currency Converter", font=("Segoe UI", 16, "bold"), bg="white", fg="#0d47a1").pack(pady=15)

# Amount input
tk.Label(frame, text="Amount", font=FONT, bg="white").pack()
entry_amount = tk.Entry(frame, font=FONT, justify="center", bg="#f1f8e9", relief="solid")
entry_amount.pack(pady=8)

# From currency selection
tk.Label(frame, text="From Currency", font=FONT, bg="white").pack()
combo_from = ttk.Combobox(frame, values=currencies, font=FONT, justify="center")
combo_from.set("USD")
combo_from.pack(pady=5)

# To currency selection
tk.Label(frame, text="To Currency", font=FONT, bg="white").pack()
combo_to = ttk.Combobox(frame, values=currencies, font=FONT, justify="center")
combo_to.set("EUR")
combo_to.pack(pady=5)

# Convert button
convert_btn = tk.Button(frame, text="🔁 Convert", font=FONT, bg="#2196f3", fg="white", activebackground="#1976d2", relief="flat", command=convert_currency)
convert_btn.pack(pady=15)

# Result display
label_result = tk.Label(frame, text="", font=("Segoe UI", 13, "bold"), bg="white", fg="#0f5132", justify="center")
label_result.pack(pady=10)


# Start the GUI event loop
window.mainloop()
