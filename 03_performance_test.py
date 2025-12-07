import timeit
from visualize_results import create_chart
from searching_algorithms import boyer_moore_search, kmp_search, rabin_karp_search, regex_search


def measure_time(algorithm, text, pattern, number=10) -> [float]:
    """
    Вимірює час виконання алгоритму
    """
    return timeit.timeit(lambda: algorithm(text, pattern), number=number)


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
                "non_existent_big": "Це дуже довгий рядок якого точно "
                                    "немає в цьому тексті про алгоритми."
            }
        },
        "стаття_2.txt": {
            "patterns": {
                "small": "рекомендацій",
                "big": "відповідно до результатів проведених експериментів",
                "non_existent_small": "синхрофазотрон",
                "non_existent_big": "Це ще один дуже довгий рядок якого "
                                    "точно немає в цій статті про бази даних."
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


    number = 100
    print("")
    print("=" * 81)
    print("ПОРІВНЯЛЬНИЙ АНАЛІЗ АЛГОРИТМІВ ПОШУКУ ПІДРЯДКІВ")
    print(f"Загальний час (ms) на {number} повторів")
    print("=" * 81)
    print()

    for filename, conf in settings.items():
        tests = []
        if not conf['text']:
            continue
        for pattern_name, pattern in conf['patterns'].items():
            result = {}
            for alg_name, alg_func in algorithms.items():
                if pattern_name not in result:
                    result[pattern_name] = {}
                result[pattern_name][alg_name] = measure_time(
                            alg_func, conf['text'], pattern, number=number
                        )
            tests.append(result)

        print("\n" + "=" * 81)
        print(f"НАЗВА ФАЙЛУ: {filename}")
        print("=" * 81 + "\n")
        column_names = ""
        for alg_name in algorithms:
            column_names += f"{alg_name: >15}"
        print( f"{'Тип підрядка':<20} {column_names}")
        for test in tests:
            row = ""
            for pattern_name in test:
                for alg_name in algorithms:
                    row += f"{test[pattern_name][alg_name] * 1000: >15.3f}"
            print(f"{pattern_name:<20} {row}")

        chart_data = {}
        for test in tests:
            for pattern_name in test:
                for alg_name in algorithms:
                    if pattern_name not in chart_data:
                        chart_data[pattern_name] = []
                    chart_data[pattern_name].append(test[pattern_name][alg_name] * 1000)
        create_chart(
            "Загальний час виконання алгоритмів пошуку підрядків",
            chart_data,
            filename.split(".", maxsplit=1)[0]+"_chart.png"
        )

        print()

if __name__ == "__main__":
    run_performance_tests()
