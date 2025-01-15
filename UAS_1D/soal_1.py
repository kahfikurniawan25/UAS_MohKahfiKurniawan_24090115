while True:
  nama = input("masukkan nama: ")
  nim = input("masukkan nim: ")

  print ("Mahasiswa bernama",nama,"dengan nim",nim)

  ulangi = input("Apakah anda ingin melanjutkan? y/t?")

  if ulangi == "y":
    continue
  elif ulangi == "t":
    print("terimakasih")
  else:
      print("maaf, inputan yang kamu masukkan tidak sesuai!")
      ulangi = input("Apakah anda ingin melanjutkan? y/t?")
  if ulangi == "y":
    continue
  elif ulangi == "t":
    print("terimakasih")
