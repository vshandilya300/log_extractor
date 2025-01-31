import sys
import os
import mmap

def extract_logs(log_file, date):
    output_dir = "output"
    output_file = os.path.join(output_dir, f"output_{date}.txt")

    os.makedirs(output_dir, exist_ok=True)

    try:
        with open(log_file, "r") as f:
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                with open(output_file, "w") as out_f:
                    for line in iter(mm.readline, b""):
                        line = line.decode()
                        if line.startswith(date):
                            out_f.write(line)
        print(f"Logs for {date} saved in {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_logs.py <log_file> <YYYY-MM-DD>")
        sys.exit(1)

    log_file = sys.argv[1]
    date = sys.argv[2]
    extract_logs(log_file, date)
