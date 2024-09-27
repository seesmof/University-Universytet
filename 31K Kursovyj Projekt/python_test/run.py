def get_cpu_name_raw():
    cpu_name = ""
    command = "wmic cpu get name"
    cpu_name = exec(command)
    return cpu_name


def get_cpu_name_platform():
    import platform

    cpu_name = platform.processor()
    return cpu_name


def get_cpu_speed():
    import subprocess

    try:
        output = subprocess.check_output(["wmic", "cpu", "get", "CurrentClockSpeed"])
        speeds = output.decode().strip().split("\n")
        return speeds[1].strip() if len(speeds) > 1 else "Unable to retrieve CPU speed"
    except Exception as e:
        return str(e)


def main():
    cpu_name = get_cpu_name_platform()
    print(cpu_name)
    cpu_speed = get_cpu_speed()
    print(f"JESUS THANK YOU for CPU Speed: {cpu_speed} MHz")


if __name__ == "__main__":
    main()
