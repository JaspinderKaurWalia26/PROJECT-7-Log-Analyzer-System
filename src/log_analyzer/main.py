from .log_analyzer import analyze_log_file
from .logger import setup_logger


logger=setup_logger()
# main function
def main():
    logger.info(f"Starting Log Analyzer System...\n")
    analyze_log_file()
    logger.info(f"Log analysis completed!")

if __name__ == "__main__":
    main()
