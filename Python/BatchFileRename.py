import os
path =input('Input folder path : ')
OldExt = input('Input old extension : ')
Newextension =input('Input new Extension: ')
counter = 0

for file in os.listdir(path):
	split = file.split('.')
	if split[-1] == OldExt:
		counter += 1
		NewName = split[0]+'.'+Newextension
	
		os.rename(
		os.path.join(path,file),os.path.join(path,NewName)
		)
print('%d file writed successfully '%counter)