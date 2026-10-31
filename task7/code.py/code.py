
# Retail Billing with Multiple Discount Rules

subtotal = 0
total_tax = 0
items = []

n = int(input("Enter number of products: "))

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category (electronics/clothing/grocery): ").lower()
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    item_total = price * quantity
    if category == "electronics":
        tax_rate = 10
    elif category == "clothing":
        tax_rate = 5
    elif category == "grocery":
        tax_rate = 2
    else:
        tax_rate = 0

    tax = item_total * tax_rate / 100

    subtotal += item_total
    total_tax += tax

    items.append([
        name, quantity, price, item_total, tax_rate, tax
    ])
if subtotal >= 5000:
    discount_rate = 10
elif subtotal >= 2000:
    discount_rate = 5
else:
    discount_rate = 0

discount = subtotal * discount_rate / 100

if discount > 500:
    discount = 500
final_amount = subtotal + total_tax - discount
print("\n========== RETAIL INVOICE ==========")
print("Product      Qty   Price   Total    Tax%   Tax")

for item in items:
    print(
        f"{item[0]:12} {item[1]:3} "
        f"{item[2]:7.2f} {item[3]:8.2f} "
        f"{item[4]:5}% {item[5]:7.2f}"
    )

print("------------------------------------")
print(f"Subtotal        : Rs. {subtotal:.2f}")
print(f"Total Tax       : Rs. {total_tax:.2f}")
print(f"Discount        : Rs. {discount:.2f}")
print(f"Final Amount    : Rs. {final_amount:.2f}")
print("====================================")
