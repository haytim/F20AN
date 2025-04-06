import sys, time, subprocess

# mapping server name to the respective IP
victims = {
    "apache": "http://10.9.0.5",
    "nginx": "http://10.9.0.8",
    "caddy": "http://10.9.0.9",
}

# detecting invalid args
if len(sys.argv) != 4 or sys.argv[1] not in victims:
    print("Usage: python3 benchmark.py <apache|nginx|caddy> output.txt <iterations>")
    sys.exit(1)

# assigning & validating args
url, output = victims[sys.argv[1]], sys.argv[2]

try:
    iterations = int(sys.argv[3])
except ValueError:
    print("invalid no of iteratinos")
    sys.exit(1)

# benchmarking connection times 
with open(output, "a") as f:
    for x in range(iterations): 
        cmd = ["curl", "-o", "/dev/null", "-s", "-w", "Time Total: %{time_total}\\n", url]
        result = subprocess.run(cmd, capture_output=True, text=True) # executing curl in subprocess
        f.write(result.stdout) # writing to file
        time.sleep(2) # 2 second interval between connectinons