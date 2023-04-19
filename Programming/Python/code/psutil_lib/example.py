import psutil

# Get list of process by name, id
for proc in psutil.process_iter():
    print("Name of process:", proc.name(), "\tID process:", proc.pid)