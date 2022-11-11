import os
import filecmp


# Compare the files in crq_configs and snapshots/configs
def fetch_change_devices():
    files = []
    for file in os.listdir("./crq_configs"):
        files.append(file)
    hostnames = [os.path.splitext(x)[0] for x in files]
    return hostnames


def main():
    fetch_change_devices()


if __name__ == "__main__":
    main()
