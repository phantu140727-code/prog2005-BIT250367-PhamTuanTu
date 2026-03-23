import csv

nv = {"tên": input("Tên: "), "tuổi": input("Tuổi: "), "id": input("ID: ")}

with open("nv.txt", "w", encoding="utf-8") as f:
    f.write(str(nv))

with open("nv.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=nv.keys())
    writer.writeheader()
    writer.writerow(nv)
