from ftplib import FTP

ftp_host = '192.168.1.4'
ftp_port = 2121
ftp_username = 'anonymous'
ftp_password = ''
ftp_folder = '/musik'  # Folder di server FTP yang ingin Anda ubah nama file-nya

# Membuat koneksi FTP
ftp = FTP()
ftp.connect(ftp_host, ftp_port)
ftp.login(ftp_username, ftp_password)

# Pindah ke folder yang diinginkan
ftp.cwd(ftp_folder)

# Mendapatkan daftar file di folder FTP
files = ftp.nlst()

# Melakukan pengubahan nama file
for filename in files:
    if filename.endswith('.mp3'):
        # Menghapus bagian "spotifydown.com - " dari nama file
        new_filename = filename.replace('spotifydown.com - ', '')

        # Mengubah nama file
        ftp.rename(filename, new_filename)

# Menutup koneksi FTP
ftp.quit()

print("Pengubahan nama file selesai.")
