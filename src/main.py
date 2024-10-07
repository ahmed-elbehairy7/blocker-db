from low import low as low_raw
from high import high as high_raw
from os.path import join


def main():
    low = generate_ips(low_raw)
    high = generate_ips(high_raw)

    for level in ["high", "low"]:
        with open(join("lists", level), "w", encoding="utf-8") as f:
            f.write("# This is the start of mafazaa's blocker hosts list\n\n")
            list(map(lambda x: write_line(x, f), low))
            if level == "high":
                list(map(lambda x: write_line(x, f), high))
            f.write("\n# This is the end of mafazaa's blocker hosts list\n")


write_line = lambda x, f: f.write("        ".join(x) + "\n")


def generate_ips(hosts: list[tuple]):

    for i in range(len(hosts)):
        if len(hosts[i]) == 1:
            hosts[i] = ("0.0.0.0", hosts[i][0])
        else:
            hosts[i] = (hosts[i][1], hosts[i][0])

    return hosts


if __name__ == "__main__":
    main()
