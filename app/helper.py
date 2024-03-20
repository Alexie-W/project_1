import os

def get_uploaded_images():
    uploads = [] 
    
    rootdir = os.getcwd()
    uploads_dir = os.path.join(rootdir, 'uploads')
    #print(uploads_dir)
    
    for subdir, dirs, files in os.walk(rootdir + '/uploads/'):
        for file in files:
            uploads.append(os.path.join('uploads', file))
    return uploads



