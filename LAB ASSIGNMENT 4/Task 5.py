#TASK 5
def fcfs(processes):
    processes.sort(key=lambda x: x[1])

    total_wt = 0
    total_tat = 0
    current_time = 0

    print("\n--- FCFS Scheduling ---")
    print("PID\tAT\tBT\tWT\tTAT")

    for pid, at, bt, pr in processes:
        if current_time < at:
            current_time = at

        wt = current_time - at
        tat = wt + bt
        current_time += bt

        total_wt += wt
        total_tat += tat

        print(f"{pid}\t{at}\t{bt}\t{wt}\t{tat}")

    print("\nAverage WT =", total_wt / len(processes))
    print("Average TAT =", total_tat / len(processes))
