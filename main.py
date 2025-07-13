import qrcode, webbrowser
categories = [
    ("STARTERS",
     ["Garlic Bread","Veg Spring Rolls","Chicken Spring Rolls","French fries","Nachos with Cheese","Soup"],
     [50,40,60,60,120,80]),
    ("INDIAN FOOD",
     ["Butter Chicken","Paneer Butter Masala","Dal Makhani","Chicken chilli","Veg Biryani","Mutton Biriyani",
      "Chicken Biriyani","Salad","Naan","Roti","Paratha","Rajma Chawal"],
     [220,180,150,80,120,180,160,20,10,10,10,60]),
    ("CHINESE FOOD",
     ["Hakka Noodles","Manchurian","Chowmien","Fried Momos","Chicken Lollipop","Fried Rice"],
     [50,50,40,30,70,100]),
    ("FASTFOOD",
     ["Veg Burger","Chicken Burger","Cheese Sandwich","Hotdog","Pizza","Pasta"],
     [45,60,50,30,85,40]),
    ("DESSERT",
     ["Chocolate Brownie","Gulabjamun","Ice‑cream","Cheesecake","Donut","Rasmalai","Cupcake"],
     [90,15,20,120,50,15,40]),
    ("DRINKS & BEVERAGES",
     ["Cold Drink","Lemonade","Lassi","Milkshake","Tea","Coffee","Fresh Fruit Juice"],
     [45,15,20,40,10,30,50]),
]   # You can customize it as per your own choice.

total = 0
for title, items, prices in categories:
    print(f"\n*{title}\n" + "-"*(1+len(title)))
    for i, (name, price) in enumerate(zip(items, prices), 1):
        print(f"{i}. {name} -> ₹{price}")
    if input(f"\nOrder {title.lower()}? (Yes(y) / No(n): ").strip().lower() == "y":
        idx = list(map(int, input("Serial nos: ").split()))
        qty = list(map(int, input("Quantities (same order): ").split()))
        for n, i in enumerate(idx):
            cost = prices[i-1] * qty[n]
            print(f"{items[i-1]} x{qty[n]} => ₹{cost}")
            total += cost

upi_name = "Inogoosh"
upi_id = "xyz@okbank"
# REPLACE WITH YOUR OWN INFO

if total:
    print(f"\n=====================\nTotal Bill: ₹{total}\n=====================")
    upi = f"upi://pay?pa={upi_id}&pn={upi_name}&am={total}&cu=INR"
    qrcode.make(upi).save("upi_qr.png")
    qrcode.make(upi).show()
    print("📲 Scan the displayed QR in any UPI app to pay.")
else:
    print("\nLooks like you just checked the menu!")