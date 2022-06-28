from apscheduler.schedulers.blocking import BlockingScheduler
import os

def process_file():
	path2file = os.path.join("upload_demo.zip_expanded", "demo", "upload-dir", "somefile.txt")
	if os.path.exists(path2file):
		with open(path2file) as file:
			print(file.read())
	else:
		print("no file somefile.txt")

scheduler = BlockingScheduler()
scheduler.add_job(process_file, 'interval', minutes=1)
scheduler.start()
