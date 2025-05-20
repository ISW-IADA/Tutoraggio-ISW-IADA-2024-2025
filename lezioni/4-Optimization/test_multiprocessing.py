import argparse
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor


def is_prime(n):
    """Verifica se un numero è primo. Generato da Claude 3.7 Sonnet"""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def count_primes(start, end):
    """Conta i numeri primi in un intervallo"""
    count = 0
    for n in range(start, end):
        if is_prime(n):
            count += 1
    return count


def sequential_primes(ranges):
    """Esecuzione sequenziale"""
    results = []
    for start, end in ranges:
        results.append(count_primes(start, end))
    return results


def multiprocessing_primes(ranges):
    with mp.Pool() as pool:
        results = pool.starmap(count_primes, ranges)
    return results


def concurrent_processing_primes(ranges):
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(count_primes, *list(zip(*ranges))))
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Contare i numeri primi in un intervallo.")
    parser.add_argument("--method", choices=["sequential", "multiprocessing", "concurrent"], default="sequential",
                        help="Metodo da utilizzare per il calcolo")
    args = parser.parse_args()

    # Creazione degli intervalli
    ranges = [(i*1000000, (i+1)*1000000) for i in range(3)]

    if args.method == "multiprocessing":
        results = multiprocessing_primes(ranges)
    elif args.method == "concurrent":
        results = concurrent_processing_primes(ranges)
    else:
        raise argparse.ArgumentError("Metodo non valido. Scegli tra 'multiprocessing' o 'concurrent'.")

    print(f"Risultati ({args.method}): {results}")
