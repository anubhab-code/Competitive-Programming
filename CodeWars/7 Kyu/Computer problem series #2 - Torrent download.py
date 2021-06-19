def torrent(files): 
    files = sorted((file['size_GB'] / file['speed_Mbps'] * 8000, file['name']) for file in files)
    return [file[1] for file in files], max(files)[0]