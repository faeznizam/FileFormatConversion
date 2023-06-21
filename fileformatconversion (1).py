# -*- coding: utf-8 -*-
"""FileFormatConversion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hOX9Qz9puhhGdNB7Hb1Wn1FxVIaMEBwe
"""

from google.colab import files
import pandas as pd
import os

#feature to implement - error handling when selecting invalid file

print('Please upload your file: ')
uploaded_file = files.upload()
file_name = next(iter(uploaded_file))

file_format = os.path.splitext(file_name)[1]

# csv to excel
if file_format.lower() == '.csv':
  output_file = input("Enter new file name: \n")
  data = pd.read_csv(file_name)
  data.to_excel(output_file, index = False)
  print("Conversion completed.")
  files.download(output_file)

# excel to csv
elif file_format.lower() in ['.xls', '.xlsx']:
  output_file = input("Enter new file name: \n")
  data = pd.read_excel(file_name)
  data.to_csv(output_file, index = False)
  print("Conversion completed.")
  files.download(output_file)

else:
  print("Invalid Choice!")