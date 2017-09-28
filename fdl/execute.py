def execute(trtl, length, cmd, args):
    if cmd == "scale":
        return length * float(args[0])
    elif cmd == "nop":
        return length
    else:
        method = getattr(trtl, cmd)
        if cmd in ["fd", "bk"]:
            args = [float(length)]
        method(*args)
