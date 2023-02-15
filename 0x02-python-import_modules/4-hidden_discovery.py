#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    ls = dir()
    for name in ls:
        if name[:2] != "__":
            print(name)
