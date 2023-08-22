import logging
import subprocess
import traceback
from datetime import datetime

# Configure logging
logging.basicConfig(filename='execution_log.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class log_test:
    def log_execution():
        try:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            logging.info(f"Execution started at: {current_time}")
            
            # Run main.py using subprocess
            subprocess.run(["python", "main.py"], check=True)
            
            logging.info("Execution completed successfully")
        except subprocess.CalledProcessError as e:
            logging.error("Error during execution:")
            logging.error(traceback.format_exc())
            logging.error(f"Error details: {e}")

log = log_test()

# if __name__ == "__main__":
#     log_execution()
