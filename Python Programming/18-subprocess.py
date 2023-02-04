import subprocess

# Run a simple command and get the output as a string
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)

# Run a command and check the return code
result = subprocess.run(["ls", "-l", "/nonexistent"], capture_output=True, text=True)
if result.returncode == 0:
    print("Command successful.")
else:
    print("Command failed.")

# Run a command and get the output as byte strings
result = subprocess.run(["ls", "-l"], capture_output=True, text=False)
print(result.stdout)

# Run a command with input
p1 = subprocess.Popen(["cat"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "hello"], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdin.write(b"hello\ngoodbye\n")
p1.stdin.close()
print(p2.communicate()[0].decode())

# Run a command in the background
process = subprocess.Popen(["sleep", "10"])
print(f"Process ID: {process.pid}")

# Kill a running process
process = subprocess.Popen(["sleep", "10"])
process.kill()
