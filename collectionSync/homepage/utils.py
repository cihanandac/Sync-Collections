def tail(file_path, lines=100):
    with open(file_path, 'r') as file:
        buffer = []
        for line in file:
            buffer.append(line)
            if len(buffer) > lines:
                buffer.pop(0)
    return buffer
