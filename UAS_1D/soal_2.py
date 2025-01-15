import pandas as pd
data = pd.DataFrame([
    [65,90,80],
    [50,80,70],
], columns=['Mahasiswa 1','Mahasiswa 2','Mahasiswa 3'], index=['algoritma dan struktur data 2','matematika numerik'])
data['total_nilai'] = data.sum(axis=1)
print('')
print(data)

df = pd.DataFrame(data)

rata_rata_matkul = df.sum(axis=0)
df['Rata-rata'] = df.sum(axis=1)

print("Rata-rata nilai untuk setiap mata kuliah:")
print(rata_rata_matkul)
print("\nRata-rata nilai untuk setiap mahasiswa:")
print(df)