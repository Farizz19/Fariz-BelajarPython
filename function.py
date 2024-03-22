# FUNCTION (FUNGSI DALAM PYTHON)
def nama():
    print('Fariz')
    
# MENAMPILKAN FUNCTION (FUNGSI) DALAM PYTHON 
nama()

# MENGIRIM PARAMETER
def delete(id, table):
    print(f'DELETE FROM {table} WHERE id=', id)
    
delete(10, 'toko')