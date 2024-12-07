
# Log Analysis Tool

### Author: Tharun Kota Sreekanth

---

## Overview

This repository contains a Python-based **Log Analysis Tool** designed to process and analyze web server log files. The tool extracts key insights such as request counts per IP, the most frequently accessed endpoints, and suspicious activity like brute force login attempts. It outputs the results to the terminal and saves them in a structured CSV file.

---

## Features

1. **Count Requests per IP Address**:
   - Parses log files to count the number of requests made by each IP address.
   - Displays results sorted by the request count in descending order.

2. **Identify the Most Frequently Accessed Endpoint**:
   - Extracts endpoints (URLs or resource paths) and identifies the one accessed the most.

3. **Detect Suspicious Activity**:
   - Flags IP addresses with failed login attempts exceeding a configurable threshold (default: 10 attempts).

4. **CSV Export**:
   - Saves results in a CSV file (`log_analysis_results.csv`) with structured sections for all analysis outputs.

---

## Getting Started

### Prerequisites

- Python 3.6 or later

### Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/log-analysis-tool.git
   cd log-analysis-tool
   ```

2. Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).

---

## Usage

1. **Prepare the Log File**:
   - Save your log file in the repository folder. Use the provided `sample.log` file as an example.

2. **Run the Script**:
   ```bash
   python log_analysis.py
   ```

3. **View the Output**:
   - Results will be displayed in the terminal.
   - A CSV file (`log_analysis_results.csv`) will be created with all the results.

---

## File Structure

- **sample.log**: Example log file for testing.
- **log_analysis.py**: Main Python script for log analysis.
- **log_analysis_results.csv**: Generated CSV file with the analysis results.

---

## Results Example

### Terminal Output
```bash
Requests per IP Address:
192.168.1.1          6
203.0.113.5          9
10.0.0.2             6
198.51.100.23        7
192.168.1.100        6

Most Frequently Accessed Endpoint:
/home (Accessed 5 times)

Suspicious Activity Detected:
203.0.113.5          9
192.168.1.100        6

Results saved to log_analysis_results.csv
```

### CSV File Structure

- **Requests per IP**:
  | IP Address      | Request Count |
  |-----------------|---------------|
  | 192.168.1.1     | 6             |

- **Most Accessed Endpoint**:
  | Endpoint        | Access Count  |
  |-----------------|---------------|
  | /home           | 5             |

- **Suspicious Activity**:
  | IP Address      | Failed Login Count |
  |-----------------|--------------------|
  | 203.0.113.5     | 9                  |

---

## Configuration

### Threshold for Suspicious Activity

- You can adjust the failed login attempt threshold by modifying the `FAILED_LOGIN_THRESHOLD` variable in `log_analysis.py`:
  ```python
  FAILED_LOGIN_THRESHOLD = 10
  ```

---

## Contributing

If you have suggestions for improvements or additional features, feel free to fork this repository and submit a pull request. Alternatively, you can open an issue to discuss your ideas.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For any questions or feedback, please contact **Tharun Kota Sreekanth** at [tharunkotasreekanth2003@gmail.com].
