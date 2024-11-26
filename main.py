import os
import mimetypes
import shutil
from datetime import datetime

def check():
	print('-'*10)
	print('Start new check!')
	dir_to_check = input('Enter directory: ')
	# make_zip = input('Create ZIP? (1 - Yes, 2 - No): ')

	# try:
	# 	choice = int(make_zip)
	# except:
	# 	return print('Error: Enter 1 or 2')

	if not os.path.exists(dir_to_check):
		return print('Error: Directory not found')

	time = datetime.now().strftime("%m-%d-%Y, %H-%M-%S")
	directs = os.listdir(os.getcwd())
	dir_for_save = f'{os.getcwd()}\\Instagram ({time})'
	os.mkdir(dir_for_save)

	for root, dirs, files in os.walk(dir_to_check):
		for file in files:
			try:
				Type = mimetypes.guess_type(file)[0]
				if (not Type == None) and (file.endswith('.txt')) and ('text' in Type):
					filename = os.path.join(root, file)
					if (os.path.isfile(filename)):
						f = open(filename,'r',errors = 'ignore', encoding='utf-8')
						lines = f.read().split('\n')
						for line in lines:
							if ('instagram' in line) and ('sessionid' in line):
								if not os.path.exists(dir_for_save):
									dir_for_save = os.mkdir(f'{os.getcwd()}\\Instagram ({time})')
								files_count = str(len(os.listdir(dir_for_save)) + 1)
								new_file = f'{dir_for_save}\\instagram_cookie ({files_count}).txt'
								with open(new_file, 'a+', errors='ignore', encoding='utf-8') as file:
									file.write(line)
									file.write('\n')
						f.close()
			except Exception as e:
				print(e)
	try:
		shutil.make_archive(f'{dir_for_save}', 'zip', f'{dir_for_save}')
	except:
		print(e)
		print('Error while creating ZIP')
	print('-'*10)
	print('Work finished!')
	print(f'Results saved: {dir_for_save}')

while True:
	check()