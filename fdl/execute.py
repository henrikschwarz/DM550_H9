def execute(trtl, length, cmd, args):
    if cmd == "fd":
        trtl.forward(length)
    elif cmd == "lt":
        trtl.left(int(args[0]))
    elif cmd == "rt":
        trtl.right(int(args[0]))
    elif cmd == "scale":
        return length * float(args[0])
    elif cmd == "nop":
        return length
    else:
        raise Exception("Unknown command '"+cmd+"'")
