from enum import Enum

class JenisKelamin(Enum):
    LAKI_LAKI = 1
    PEREMPUAN = 2
    
print(JenisKelamin.LAKI_LAKI) ## Value of Enum => JenisKelamin.LAKI_LAKI
print(JenisKelamin.LAKI_LAKI.value) ## value dari lAKI_LAKI => 1
print(JenisKelamin.LAKI_LAKI.name) #3 Nama Enum => LAKI_LAKI

# Dart Programing
# enum Status {ONLINE, OFFLINE, BUSY}