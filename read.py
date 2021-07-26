import psutil
import platform
from datetime import datetime


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def read_from_txt():
    extracted_txt = {}

    with open("readTest.txt", "r") as systemInfo:
        for line in systemInfo:
            content = line.split(" ")

            item = content[0]
            value = content[1]

            extracted_txt[item] = value

        print(extracted_txt)

    systemInfo.close()


with open("sys_info_output.txt", "a") as f:
    """
    print("Hello stackoverflow!", file=f)
    print("I have a question.", file=f)
    """

    print("=" * 40, "System Information", "=" * 40, file=f)
    uname = platform.uname()
    print(f"System: {uname.system}", file=f)
    print(f"Version: {uname.version}", file=f)
    print(f"Machine: {uname.machine}", file=f)
    print(f"Processor: {uname.processor}", file=f)

    # let's print CPU information
    print("=" * 40, "CPU Info", "=" * 40, file=f)
    # number of cores
    print("Physical cores:", psutil.cpu_count(logical=False), file=f)
    print("Total cores:", psutil.cpu_count(logical=True), file=f)
    # CPU frequencies

    cpufreq = psutil.cpu_freq()
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz", file=f)

    # Memory Information
    print("=" * 40, "Memory Information", "=" * 40, file=f)
    # get the memory details
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}", file=f)

    # Disk Information
    print("=" * 40, "Disk Information", "=" * 40, file=f)
    print("Partitions and Usage:", file=f)
    # get all disk partitions
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Device: {partition.device} ===", file=f)
        print(f"  Mountpoint: {partition.mountpoint}", file=f)

        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            continue
        print(f"  Total Size: {get_size(partition_usage.total)}", file=f)





