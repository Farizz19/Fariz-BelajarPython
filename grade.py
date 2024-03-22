# VARIABEL
nilai = 90

# ARRAY
grade = ['A', 'B', 'C']

# PROGRAM MENENTUKAN GRADE SESUAI DENGAN NILAI
if nilai >= 90:
    print('Nilai Anda : ', nilai)
    print('Grade : ', grade[0])
elif nilai >= 80 and nilai < 90:
    print('Nilai Anda : ', nilai)
    print('Grade : ', grade[1])
else:
    print('Nilai Anda : ', nilai)
    print('Grade : ', grade[2])