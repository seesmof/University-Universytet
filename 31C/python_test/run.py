def get_cpu_name_raw():
    cpu_name = ""
    command = "wmic cpu get name"
    cpu_name = exec(command)
    return cpu_name


def get_cpu_name_platform():
    import platform

    cpu_name = platform.processor()
    return cpu_name


def main():
    cpu_name = get_cpu_name_platform()
    print(cpu_name)


if __name__ == "__main__":
    main()
