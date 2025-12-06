import timeit
from searching_algorithms import boyer_moore_search, kmp_search, rabin_karp_search, regex_search


def measure_time(algorithm, text, pattern, number=10):
    """
    Вимірює час виконання алгоритму
    """
    result = timeit.timeit(lambda: algorithm(text, pattern), number=number)
    return result / number


def run_performance_tests():
    """Виконує повний набір тестів продуктивності"""

    # Алгоритми для тестування
    algorithms = {
        'Boyer-Moore': boyer_moore_search,
        'KMP': kmp_search,
        'Rabin-Karp': rabin_karp_search,
        'Regex': regex_search
    }



    settings = {
        "стаття_1.txt": {
            "patterns": {
                "small": "алгоритми",
                "big": "Висновки. Кожна система містить набір обмежень і вимог.",
                "non_existent_small": "космос",
                "non_existent_big": "Це дуже довгий рядок якого точно \
                    немає в цьому тексті про алгоритми."
            }
        },
        "стаття_2.txt": {
            "patterns": {
                "small": "рекомендацій",
                "big": "відповідно до результатів проведених експериментів",
                "non_existent_small": "синхрофазотрон",
                "non_existent_big": "Це ще один дуже довгий рядок якого \
                    точно немає в цій статті про бази даних."
            }
        }
    }

    for filename, conf in settings.items():
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                conf['text'] = f.read()
        except FileNotFoundError:
            print(f"Помилка: Файл '{filename}' не знайдено.")
            conf['text'] = ""

    print("")
    print("=" * 100)
    print("ПОРІВНЯЛЬНИЙ АНАЛІЗ АЛГОРИТМІВ ПОШУКУ ПІДРЯДКІВ")
    print("=" * 100)
    print()

    for filename, conf in settings.items():
        if not conf['text']:
            continue
        number = 100
        print("\n" + "=" * 100)
        print(f"НАЗВА ФАЙЛУ: {filename}")
        print("=" * 100 + "\n")
        print(
            f"{'Тип підрядка':<20} {'Алгоритм':<20} {f'Середній час (ms)':<20}"
            + f"{f'Час для {number} спроб (ms)':<20}"
        )
        for pattern_name, pattern in conf['patterns'].items():
            print("-" * 100)
            times = {}
            for alg_name, alg_func in algorithms.items():
                times[alg_name] = measure_time(
                    alg_func, conf['text'], pattern, number=number
                )
                print(f"{pattern_name:<20} {alg_name:<20} {times[alg_name] * 1000:<20.5f}"
                + f" {times[alg_name] * number * 1000:<20.5f}")
        print()

if __name__ == "__main__":
    run_performance_tests()
