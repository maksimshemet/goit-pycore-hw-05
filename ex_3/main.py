from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import List, Optional
from collections import namedtuple
from tabulate import tabulate

def _check_if_file_exist(path_str: str) -> Path:
    p = Path(path_str)
    if not p.is_file():
        raise argparse.ArgumentTypeError(f"'{path_str}' not exist...")
    return p.resolve()


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    """
    Parse CLI arguments.

    """
    description = "List directory tool"
    epilog = (
        "Examples:\n"
        "  python main.py /path/to/log/file.txt\n"
        "  python main.py /path/to/log/file.txt error\n"
    )

    parser = argparse.ArgumentParser(
        prog="ex_3",
        description=description,
        epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # Positional arguments
    parser.add_argument(
        "logfile",
        type=_check_if_file_exist,
        help="Path to logfile.",
    )

    parser.add_argument(
        "logLevel",
        nargs="?",
        type=str,
        default="",
        help="String to filter log lines.",
    )

    return parser.parse_args(argv)

    
def run(args: argparse.Namespace) -> int:
    """
    Main program logic separated from parsing for testability.
    Returns exit code (0 = success).
    """

    try:
        logList = [namedtuple("ParsedLog", ["date","time","level", "message"])]
        if args.logfile:
            print(f"{args.logfile}")

            for line in load_logs(args.logfile):
                logList.append(parse_log_line(line))
            
            filter_logs_by_level(logList, args.logLevel)
        
            display_log_counts(count_logs_by_level(logList))
            if args.logLevel:
                print(f"Деталі логів для рівня: {args.logLevel.upper()}")
                for log in filter_logs_by_level(logList, args.logLevel.upper()):
                    print(f"{log.date} {log.time} {log.level} - {log.message}")

        return 0
    except Exception as exc:
        print(f"ERROR: error heppens...\n{exc}")
        return 1


def load_logs(logfile: Path) -> List[str]:
    with logfile.open("r") as f:
        return f.readlines()
    
def parse_log_line(line: str) -> namedtuple:
    ParsedLog = namedtuple("ParsedLog", ["date","time","level", "message"])
    parts = line.split(" ", 3)
    parsedLog = ParsedLog(parts[0], parts[1], parts[2], parts[3].strip())

    return parsedLog

def filter_logs_by_level(logs: list, level: str) -> list:

    logsByLevel = lambda level: [log for log in logs if log.level == level]

    return logsByLevel(level)

def count_logs_by_level(logs: list) -> dict:
    logLevelsCounter = {}

    for log in logs:
        if log.level in logLevelsCounter:
            logLevelsCounter[log.level] += 1
        else:
            logLevelsCounter[log.level] = 1

    #Filter the dictionary to remove the internal field
    logLevelsCounter = {key: value for key, value in logLevelsCounter.items() if '_tuplegetter' not in str(key)}

    return logLevelsCounter

def display_log_counts(counts: dict):
    headers = ["Log Level", "Count"]

    print(tabulate(counts.items(), headers=headers, tablefmt="grid"))

def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)

    return run(args)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
