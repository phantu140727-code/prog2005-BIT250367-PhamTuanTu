import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 100)
y1 = x**2
y2 = x**3

plt.figure(figsize=(8, 5))
plt.plot(x, y1, color='blue', label='$y = x^2$')
plt.plot(x, y2, color='red', label='$y = x^3$')

plt.title('So sánh đồ thị hàm số $y=x^2$ và $y=x^3$')
plt.xlabel('Giá trị x')
plt.ylabel('Giá trị y')
plt.axhline(0, color='black', linewidth=0.5) # Đường trục hoành
plt.axvline(0, color='black', linewidth=0.5) # Đường trục tung
plt.legend()
plt.grid(True, linestyle='--')

plt.show()
