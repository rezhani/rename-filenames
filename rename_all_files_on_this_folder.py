import os

folder_path = os.getcwd()  # Ubah sesuai dengan path ke folder yang ingin Anda ubah

# Mencari semua file di dalam folder
files = os.listdir(folder_path)

# Melakukan pengubahan nama file
for filename in files:
    if filename.endswith('.mp3'):
        # Menghapus bagian "spotifydown.com - " dari nama file
        new_filename = filename.replace('spotifydown.com - ', '')

        # Mengubah nama file
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

print("Pengubahan nama file selesai.")
