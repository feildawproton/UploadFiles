from apscheduler.schedulers.blocking import BlockingScheduler
import os
import glob

def check_files():
	path2filefolder = os.path.join("upload_demo.zip_expanded", "demo", "upload-dir", "*.txt")
	for filename in glob.glob(path2filefolder):
		print(filename)

scheduler = BlockingScheduler()
scheduler.add_job(check_files, 'interval', minutes=1)
scheduler.start()
