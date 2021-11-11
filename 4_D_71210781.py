#program perhitungan deret geometri untuk menghitung 
#jumlah suku ke-11 dari deret 1, 3, 9, 27, 81, ….!
# Un = ar^n-1

#identifikasi
a = 1
r = 3
n = 11

#penyelesaian
Un = (a*r)**(n-1)

print(f"\nMaka nilai dari suku ke-{n} adalah {Un}")