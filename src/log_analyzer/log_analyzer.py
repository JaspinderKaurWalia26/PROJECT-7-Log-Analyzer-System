import os
import json
from .parsing import parse_log_line
from .logger import setup_logger


logger = setup_logger()

# analyzing log file
def analyze_log_file(log_file="inputs/app.log",
                     output_json="outputs/summary.json"):
    # initializing error count
    error_count = 0
    # initializing warning count
    warning_count = 0

    try:
        # checking if log file exists
        if not os.path.exists(log_file):
            raise FileNotFoundError(f"Log file '{log_file}' not found!")

        os.makedirs(os.path.dirname(output_json), exist_ok=True)
        # opening the log file
        with open(log_file, "r") as file:
            for line in file:
                # Parsing the line into timestamp, level, message
                parsed = parse_log_line(line)
                if parsed is None:
                    logger.warning(f"Corrupt line skipped: {line.strip()}")
                    continue

                timestamp, level, message = parsed
                if level == "ERROR":
                    # increasing error count
                    error_count += 1
                    logger.error(f"{timestamp} - {message}")
                elif level == "WARNING":
                    # increasing warning count
                    warning_count += 1
                    logger.warning(f"{timestamp} - {message}")

        # JSON summary
        summary_data = {
            "total_errors": error_count,
            "total_warnings": warning_count
        }
        with open(output_json, "w") as json_file:
            json.dump(summary_data, json_file, indent=4)

       
        logger.info("===== LOG ANALYSIS SUMMARY =====")
        logger.info(f"Total ERRORs: {error_count}")
        logger.info(f"Total WARNINGs: {warning_count}")
        logger.info(f"JSON summary saved at: {output_json}")
        

    except FileNotFoundError as e:
        logger.error(e)
    except Exception as e:
        logger.exception(f"Unexpected error occurred: {e}")
