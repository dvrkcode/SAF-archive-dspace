import os
import zipfile

def ZipCompressor():
  def zipdir(path, ziph, file_counter):
    # Creamos una lista de todas las rutas de archivos
    all_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            all_files.append(os.path.join(root, file))

    # Ordenamos la lista de rutas de archivos alfabéticamente
    all_files.sort()

    # Procesamos cada archivo uno por uno
    for filepath in all_files:
      new_root = filepath.split('/')[2]
      file = filepath.split('/')[-1]
      ziph.write(filepath, os.path.relpath(os.path.join(new_root, file), os.path.join(path, '..')))
      if os.path.getsize(ziph.filename) > 480 * 1024 * 1024:
        ziph.close()
        file_counter += 1
        ziph = zipfile.ZipFile(f'./dspace_data_part{file_counter}.zip', 'w', zipfile.ZIP_DEFLATED)

    return ziph, file_counter

  file_counter = 1
  zipf = zipfile.ZipFile(f'./dspace_data_part{file_counter}.zip', 'w', zipfile.ZIP_DEFLATED)

  zipf, file_counter = zipdir('./output', zipf, file_counter)

  zipf.close()

