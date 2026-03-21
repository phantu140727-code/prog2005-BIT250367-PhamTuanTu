import matplotlib.pyplot as plt
import pandas as pd

# Giả lập dữ liệu diện tích các thành phố tại California (km2)
data = {
    'city': ['Los Angeles', 'San Diego', 'San Jose', 'San Francisco', 'Fresno', 
             'Sacramento', 'Long Beach', 'Oakland', 'Bakersfield', 'Anaheim', 'Riverside', 'Stockton'],
    'area_total_km2': [1302, 964, 466, 600, 290, 259, 210, 202, 396, 131, 210, 167]
}
df = pd.DataFrame(data)

df_top10 = df.sort_values(by='area_total_km2', ascending=False).head(10)

# Đảo ngược thứ tự để thành phố lớn nhất nằm ở trên cùng khi dùng barh
df_top10 = df_top10.iloc[::-1]

plt.figure(figsize=(10, 6))
plt.barh(df_top10['city'], df_top10['area_total_km2'], color='teal')

plt.title('Top 10 thành phố lớn nhất California theo diện tích')
plt.xlabel('Diện tích (km2)')
plt.ylabel('Thành phố')
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
