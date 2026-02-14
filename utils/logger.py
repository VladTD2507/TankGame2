import datetime

class Logger:
    @staticmethod
    def log(message, level="INFO"):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}"
        print(log_entry)
        
        with open("game_log.txt", "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")

    @staticmethod
    def clear_log():
        with open("game_log.txt", "w", encoding="utf-8") as f:
            f.write("")