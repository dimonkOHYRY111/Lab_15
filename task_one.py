import matplotlib.pyplot as plt

journals = [
    {"name": "Journal A", "price": 25.50, "circulation": 8000},
    {"name": "Journal B", "price": 35.00, "circulation": 12000},
    {"name": "Journal C", "price": 15.75, "circulation": 5000},
    {"name": "Journal D", "price": 40.20, "circulation": 15000},
    {"name": "Journal E", "price": 18.90, "circulation": 7000}
]

labels = [journal["name"] for journal in journals]
sizes = [journal["circulation"] for journal in journals]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, wedgeprops={'edgecolor': 'black'})

plt.title('Розподіл тиражів журналів', fontsize=14)

plt.axis('equal')
plt.tight_layout()
plt.show()