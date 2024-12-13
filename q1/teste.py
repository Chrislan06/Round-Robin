def round_robin(processes, burst_time, quantum, interval, context_switch_time=1):
    n = len(processes)
    remaining_burst_time = burst_time[:]
    completed_processes = 0
    current_time = 0
    waiting_time = [0] * n
    turnaround_time = [0] * n
    throughput_intervals = []
    
    # Execução do algoritmo Round Robin
    while completed_processes < n:
        for process in range(n):
            if remaining_burst_time[process] > 0:
                # Determina o tempo que o processo será executado neste ciclo
                time_slice = min(quantum, remaining_burst_time[process])
                current_time += time_slice
                remaining_burst_time[process] -= time_slice

                # Se o processo for concluído, registre os tempos
                if remaining_burst_time[process] == 0:
                    completed_processes += 1
                    turnaround_time[process] = current_time
                    waiting_time[process] = current_time - burst_time[process]

                # Adicione o tempo de troca de contexto
                if completed_processes < n:
                    current_time += context_switch_time

    # Calcular a vazão em intervalos
    final_interval = (current_time // interval + 1) * interval
    processes_completed = 0

    for time in range(interval, final_interval + 1, interval):
        while processes_completed < n and turnaround_time[processes_completed] <= time:
            processes_completed += 1
        throughput_intervals.append(processes_completed)

    print(turnaround_time, waiting_time)
    # Calcula as médias
    average_waiting_time = sum(waiting_time) / n
    average_turnaround_time = sum(turnaround_time) / n

    return average_turnaround_time, average_waiting_time, throughput_intervals


# Exemplo de entrada
processes = [1, 2, 3, 4]
burst_time = [15, 5, 8, 10]
quantum = 4
interval = 5

# Chamada da função
avg_turnaround_time, avg_waiting_time, throughput_intervals = round_robin(processes, burst_time, quantum, interval)

print("Tempo médio de retorno:", avg_turnaround_time)
print("Tempo médio de espera:", avg_waiting_time)
print("Vazão por intervalo:", throughput_intervals)
