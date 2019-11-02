# Penentuan pengeluaran terbesar pada bulan Januari ,Februari ,Maret.
# Diantara 3 bilangan

print('Penentuan pengeluaran terbesar pada bulan Januari ,Februari ,Maret.')
print('Diantara 3 pengeluaran')
print('-----------------------')

pengeluaranA = int(input('pengeluaran terbesar januari   = '))
pengeluaranB = int(input('pengeluaran terbesar februari  = '))
pengeluaranC = int(input('pengeluaran terbesar maret     = '))

# Penentuan pengeluaran terbesar pada bulan Januari ,Februari ,Maret.
terbesar = pengeluaranA
if pengeluaranB > terbesar:
    terbesar = pengeluaranB
if pengeluaranC > terbesar:
    terbesar = pengeluaranC

# Tampilkan hasilnya
print('pengeluaran terbesar  = ', terbesar)

