import matplotlib.pyplot as plt
import numpy as np

def create_chart(title, data, filename):
    labels = list(data.keys())
    # data structure: {'sub_type': [BM, KMP, RK, Regex]}

    # Transpose data for plotting
    # We want groups by Substring Type

    substring_types = list(data.keys()) # ['small', 'big', ...]
    algorithms = ['Boyer-Moore', 'KMP', 'Rabin-Karp', 'Regex']

    x = np.arange(len(substring_types))  # the label locations
    width = 0.2  # the width of the bars

    fig, ax = plt.subplots(figsize=(10, 6))

    # Extract values for each algorithm
    bm_vals = [data[t][0] for t in substring_types]
    kmp_vals = [data[t][1] for t in substring_types]
    rk_vals = [data[t][2] for t in substring_types]
    regex_vals = [data[t][3] for t in substring_types]

    rects1 = ax.bar(x - 1.5*width, bm_vals, width, label='Boyer-Moore')
    rects2 = ax.bar(x - 0.5*width, kmp_vals, width, label='KMP')
    rects3 = ax.bar(x + 0.5*width, rk_vals, width, label='Rabin-Karp')
    rects4 = ax.bar(x + 1.5*width, regex_vals, width, label='Regex')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Час (ms)')
    ax.set_title(title)
    ax.set_xticks(x, substring_types)
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Log scale might be better due to huge difference, but linear is requested/default usually.
    # Let's stick to linear but mentioned it could be log. 
    # Actually, Regex is so small it might be invisible. 
    # Let's try to make it clear.

    fig.tight_layout()

    plt.savefig(filename)
    print(f"Saved {filename}")

if __name__ == "__main__":
    # Data from README.md
    # [Boyer-Moore, KMP, Rabin-Karp, Regex]
    data_1 = {
        'small': [0.512, 1.277, 2.864, 0.065],
        'big': [5.121, 43.367, 96.777, 0.341],
        'non_existent_small': [27.517, 52.086, 115.522, 0.443],
        'non_existent_big': [4.524, 51.015, 117.862, 0.369]
    }

    data_2 = {
        'small': [0.223, 0.364, 0.754, 0.041],
        'big': [11.557, 73.802, 165.409, 0.670],
        'non_existent_small': [20.145, 75.604, 166.065, 0.630],
        'non_existent_big': [7.189, 72.506, 168.564, 0.504]
    }

    create_chart('Час виконання алгоритмів для Тексту 1', data_1, 'results_article_1.png')
    create_chart('Час виконання алгоритмів для Тексту 2', data_2, 'results_article_2.png')
