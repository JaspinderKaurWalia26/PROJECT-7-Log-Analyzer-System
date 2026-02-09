# parsing log function
def parse_log_line(line):
    if not line or line.strip() == "":
        return None

    try:
        # splitting in 4 parts
        parts = line.split(" ", 3)
        # combining first two to get timestamp
        timestamp = parts[0] + " " + parts[1]
        # log level converted to upper case
        level = parts[2].upper()
        # removing extra spaces from message
        message = parts[3].strip()
        # if level is not in specified levels return none
        if level not in ("INFO", "WARNING", "ERROR","CRITICAL", "DEBUG"):
            return None  
        # if level is specified then return 
        return timestamp, level, message
    except IndexError:
        return None
