# log_extractor
#Solutions Considered  
1. **Using Basic File I/O:**  
   - Initially considered reading the log file line by line using basic file I/O operations.  
   - This approach was straightforward but inefficient for large files, as it required reading the entire file into memory.  

2. **Using Regular Expressions:**  
   - Explored using regex to match log lines based on the date pattern.  
   - While regex is powerful, it added unnecessary complexity for the simple task of filtering logs by date.  

3. **Using Memory Mapping (mmap):**  
   - Final approach used `mmap` to map the file into memory, allowing efficient reading without loading the entire file into memory.  
   - This solution is optimal for handling large log files and reduces memory overhead.  

### Final Solution Summary  
- The chosen solution uses Python’s `mmap` module to efficiently read and filter large log files by date.  
- This approach minimizes memory usage and allows for fast processing, making it suitable for large-scale log extraction tasks.  

### Steps to Run  
1. Place the log file in the same directory as the script or provide its full path.  
2. Run the script from the terminal:  
   ```bash  
   python extract_logs.py log_2024.log <YYYY-MM-DD>

### **4. Add Your Source Code**  
- Create a `src/` directory in the repository if it doesn’t already exist:  
  ```bash  
  mkdir src
