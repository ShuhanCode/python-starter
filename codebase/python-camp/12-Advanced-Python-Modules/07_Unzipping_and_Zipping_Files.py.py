"""   
import zipfile

# slashes may need to change for MacOS or Linux
f = open("new_file.txt",'w+')
f.write("Here is some text")
f.close()

# slashes may need to change for MacOS or Linux
f = open("new_file2.txt",'w+')
f.write("Here is some text")
f.close()

comp_file = zipfile.ZipFile('comp_file.zip','w')

comp_file.write("new_file.txt",compress_type=zipfile.ZIP_DEFLATED)

comp_file.write('new_file2.txt',compress_type=zipfile.ZIP_DEFLATED)

comp_file.close()

zip_obj = zipfile.ZipFile('comp_file.zip','r')

zip_obj.extractall("extracted_content")

"""

import shutil

dir_to_zip = '/Users/rfnoc/tmp/python-starter/codebase/python-camp/12-Advanced-Python-Modules/extracted_content'

output_filename = 'example'

# Note this won't run as is because the variable are undefined
shutil.make_archive(output_filename,'zip',dir_to_zip)

# Extracting a zip archive
# Notice how the parameter/argument order is slightly different here
shutil.unpack_archive ('example.zip', 'final_unzip','zip')
