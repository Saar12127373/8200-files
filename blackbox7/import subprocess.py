import subprocess

exe_path = r"C:\8200\blackbox7\secret2.exe"

for i in range(1, 301):
    print(f"Trying {i}")
    result = subprocess.run([exe_path],input=f"{i}\n",text=True,capture_output=True)

    output = result.stdout.strip()
    print(output)

    if "wrong checksum" not in output.lower():
        print(f"✅ Success with checksum: {i}")
        break