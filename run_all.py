import subprocess
import sys
import signal
from dotenv import load_dotenv

load_dotenv()
processes = []

def shutdown(sig, frame):
    print("\n서버 종료 중")
    for p in processes:
        p.terminate()
    sys.exit(0)

signal.signal(signal.SIGINT, shutdown)
signal.signal(signal.SIGTERM, shutdown)

if __name__ == "__main__":
    print("Fast API 서버 실행")
    processes.append(
        subprocess.Popen([
            "uvicorn",
            "main:app",
            "--host", "0.0.0.0",
            "--port", "8040"
        ])
    )
    print("Dash 서버 실행")
    processes.append(
        subprocess.Popen([
            sys.executable,
            "ploter.py"
        ])
    )

    for p in processes:
        p.wait()
