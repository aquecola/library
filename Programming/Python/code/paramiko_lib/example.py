import paramiko

# create and connect
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("79.137.196.193", username="root", port="5500")

# execute and show results functions
def uptime_call():
    stdin, stdout, stderr = ssh.exec_command("uptime")
    return(stdout.read().decode())

def docker_ps():
    stdin, stdout, stderr = ssh.exec_command("docker ps")
    return(stdout.read().decode())

# call functions
print (uptime_call())
print (docker_ps())

# close connection
ssh.close()