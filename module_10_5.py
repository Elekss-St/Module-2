import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    # Для демонстрации можно вывести количество строк, но в реальном сценарии это не рекомендуется из-за большого объема данных
    print(f"{name} содержит {len(all_data)} строк.")

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.time() - start_time
    print(f"Линейное выполнение заняло: {linear_duration} секунд.")

    # Многопроцессный вызов
    start_time = time.time()
    with Pool(processes=4) as pool:  # Количество процессов можно настроить в зависимости от количества ядер процессора
        pool.map(read_info, filenames)
    multiprocess_duration = time.time() - start_time
    print(f"Многопроцессное выполнение заняло: {multiprocess_duration} секунд.")