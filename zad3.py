def finish(name, task_id, time_ms):
    time_s = time_ms // 1000
    time_ms = time_ms % 1000
    time = (time_s, time_ms)
    message = \
        f'{name} wykonał(a) zadanie nr {task_id} w {time[0]}.{time[1]:03}s.'
    return message


def finish2(name, task_id, time_ms):
    time_s = time_ms / 1000
    message = f'{name} wykonał(a) zadanie nr {task_id} w {time_s:.3f}s.'
    return message


print(finish("Kacper", 3, 333056))
print(finish2("Kacper", 3, 333056))
