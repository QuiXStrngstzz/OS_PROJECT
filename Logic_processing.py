class Process:
    def __init__(self, id, arrival_time, burst_time, completion_time=None):
        self.id = id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = completion_time
        self.remaining_burst_time = burst_time 

def compare_arrival_time(p1, p2):
    return p1.arrival_time < p2.arrival_time

def compare_burst_time(p1, p2):
    return p1.burst_time < p2.burst_time

def compare_remaining_burst_time(p1, p2):
    return p1.remaining_burst_time < p2.remaining_burst_time

def FCFS_sched(processes):
    processes.sort(key=lambda x: x.arrival_time)

    current_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0

    result_list = []  # List to store the results

    for p in processes:
        current_time = max(current_time, p.arrival_time)
        p.completion_time = current_time + p.burst_time
        turnaround_time = p.completion_time - p.arrival_time
        waiting_time = turnaround_time - p.burst_time
        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time

        result_list.append({
            "PID": p.id,
            "AT": p.arrival_time,
            "BT": p.burst_time,
            "CT": p.completion_time,
            "TT": turnaround_time,
            "WT": waiting_time
        })

        current_time = p.completion_time

    average_turnaround_time = total_turnaround_time / len(processes)
    average_waiting_time = total_waiting_time / len(processes)

    result_list.append({
        "Average Turnaround Time": average_turnaround_time,
        "Average Waiting Time": average_waiting_time
    })

    return result_list

def SJF_sched(processes):
    processes.sort(key=lambda x: x.burst_time)

    current_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0

    result_list = []  # List to store the results

    for p in processes:
        current_time = max(current_time, p.arrival_time)
        p.completion_time = current_time + p.burst_time
        turnaround_time = p.completion_time - p.arrival_time
        waiting_time = turnaround_time - p.burst_time
        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time

        result_list.append({
            "PID": p.id,
            "AT": p.arrival_time,
            "BT": p.burst_time,
            "CT": p.completion_time,
            "TT": turnaround_time,
            "WT": waiting_time
        })

        current_time = p.completion_time

    average_turnaround_time = total_turnaround_time / len(processes)
    average_waiting_time = total_waiting_time / len(processes)

    result_list.append({
        "Average Turnaround Time": average_turnaround_time,
        "Average Waiting Time": average_waiting_time
    })

    return result_list

def STRF_sched(processes):
    result_list = []

    if not processes:
        result_list.append({"No processes to schedule"})
    else:
        processes.sort(key=lambda x: x.arrival_time)

        current_time = processes[0].arrival_time
        total_turnaround_time = 0
        total_waiting_time = 0
        ready_queue = []

        while processes or ready_queue:
            while processes and processes[0].arrival_time <= current_time:
                ready_queue.append(processes.pop(0))

            if ready_queue:
                ready_queue.sort(key=lambda x: x.remaining_burst_time)
                p = ready_queue[0]

                if p.completion_time is None:
                    p.completion_time = current_time

                # Execute for 1 time unit
                p.remaining_burst_time -= 1
                current_time += 1

                if p.remaining_burst_time == 0:
                    turnaround_time = current_time - p.arrival_time
                    waiting_time = turnaround_time - p.burst_time
                    total_turnaround_time += turnaround_time
                    total_waiting_time += waiting_time

                    result_list.append({
                        "PID": p.id,
                        "AT": p.arrival_time,
                        "BT": p.burst_time,
                        "CT": p.completion_time,
                        "TT": turnaround_time,
                        "WT": waiting_time
                    })

                    ready_queue.pop(0)
            else:
                # No process in the ready queue, move to the next time unit
                current_time += 1

        if total_turnaround_time == 0 or total_waiting_time == 0:
            result_list.append({"No processes completed"})
            
        else:
            total_processes = len(result_list)
            average_turnaround_time = total_turnaround_time / max(1, total_processes)
            average_waiting_time = total_waiting_time / max(1, total_processes)

            result_list.append({
                "Average Turnaround Time": average_turnaround_time,
                "Average Waiting Time": average_waiting_time
            })

    return result_list







