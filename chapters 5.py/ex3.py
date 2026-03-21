import matplotlib.pyplot as plt

labels = ['Sản phẩm A', 'Sản phẩm B', 'Sản phẩm C', 'Sản phẩm D', 'Sản phẩm E']
sizes = [30, 25, 15, 20, 10]

plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])

plt.title('Tỷ trọng doanh số theo sản phẩm')
plt.show()
