import subprocess
import sys
import time
import os

print("Starting background worker process...", flush=True)
# Start worker.py as a subprocess
worker_process = subprocess.Popen(
    [sys.executable, "worker.py"],
    stdout=sys.stdout,
    stderr=sys.stderr,
    bufsize=1,
    universal_newlines=True
)

print("Starting API process...", flush=True)
# Start uvicorn as a subprocess
api_command = [
    "uvicorn", "main:app",
    "--host", "0.0.0.0",
    "--port", "8001",
    "--workers", "1",
    "--log-level", "info",
    "--proxy-headers",
    "--forwarded-allow-ips", "*"
]

try:
    api_process = subprocess.Popen(
        api_command,
        stdout=sys.stdout,
        stderr=sys.stderr,
        bufsize=1,
        universal_newlines=True
    )
    
    # Monitor both processes. If either crashes, exit the entrypoint script
    while True:
        time.sleep(2)
        
        # Check worker process
        worker_status = worker_process.poll()
        if worker_status is not None:
            print(f"Worker process exited with code {worker_status}!", flush=True)
            api_process.terminate()
            sys.exit(worker_status or 1)
            
        # Check API process
        api_status = api_process.poll()
        if api_status is not None:
            print(f"API process exited with code {api_status}!", flush=True)
            worker_process.terminate()
            sys.exit(api_status or 1)
            
except KeyboardInterrupt:
    print("Shutting down processes gracefully...", flush=True)
    worker_process.terminate()
    api_process.terminate()
    sys.exit(0)
