from typing import List

def list_to_int(pref: List[int]) -> int:
    res = 0
    for v in pref:
        res = (res << 8) | v
    return res

def int_to_list(x: int) -> List[int]:
    return [
        (x >> 24) & 0xFF,
        (x >> 16) & 0xFF,
        (x >> 8) & 0xFF,
        x & 0xFF,
    ]

def int_to_ip(x: int) -> str:
    return ".".join(map(str, int_to_list(x)))

if __name__ == "__main__":
    addr = input().strip()
    ip_str, mask_str = addr.split("/")

    prefix_len = int(mask_str)

    ip_list = [int(i) for i in ip_str.split(".")]
    ip_int = list_to_int(ip_list)

    netmask = (0xFFFFFFFF << (32 - prefix_len)) & 0xFFFFFFFF

    begin_int = ip_int & netmask
    end_int = begin_int | (~netmask & 0xFFFFFFFF)

    print(f"begin address: {int_to_ip(begin_int)}")
    print(f"end   address: {int_to_ip(end_int)}")