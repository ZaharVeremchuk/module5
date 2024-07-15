import shutil # Модуль для роботи з архівами
# 1 parameter -> way to archive
# 2 parameter -> format
# 3 parameter -> the directory from which the archive will be created.
# 4 parameter -> dir into archive, from which will start archivation
shutil.make_archive('example', 'zip', root_dir=None , base_dir=None)

# 1 parameter -> file name
# 2 parameter -> extract directory
# 3 parameter -> archive format
shutil.unpack_archive('example', extract_dir=None, format='zip')