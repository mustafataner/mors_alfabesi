mors_kodu={'A':'• –',
'B':'– • • •',
'C':'– • – •',
'D':'– • •',
'E':'•',
'F':'• • – •',
'G':'– – •',
'H':'• • • •',
'I':'• •',
'J':'• – – –',
'K':'– • –',
'L':'• – • •',
'M':'– –',
'N':'– •',
'O':'– – –',
'P':'• – – •',
'Q':'– – • –',
'R':'• – •',
'S':'• • •',
'T':'–',
'U':'• • –',
'V':'• • • –',
'W':'• – –',
'X':'– • • –',
'Y':'– • – –',
'Z':'– – • •',
'Ö':'–––•',
'Ü':'••––',
'Ç':'––––',
'Ş':'•••–•',
}


kelime=input("lütfen çevirmek istediğiniz kelimeyi yazınız: ").upper()


for i in range(0,len(kelime)):
    indeks=kelime[i]
    sonuc=mors_kodu.get(indeks)
    print(sonuc, end=" ")