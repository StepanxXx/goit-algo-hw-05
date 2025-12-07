import matplotlib.pyplot as plt
import numpy as np

def create_chart(title, data, filename, ndigits = 3):
    # data structure: {'sub_type': [BM, KMP, RK, Regex]}

    # Transpose data for plotting
    # We want groups by Substring Type

    substring_types = list(data.keys()) # ['small', 'big', ...]

    x = np.arange(len(substring_types))  # the label locations
    width = 0.2  # the width of the bars

    fig, ax = plt.subplots(figsize=(10, 6))

    rects = []
    values = {}
    for _, record in data.items():
        for column_name, value in record.items():
            if column_name not in values:
                values[column_name] = []
            values[column_name].append(value)

    columns = values.keys()
    for index, column_name in enumerate(columns):
        rects.append(
            ax.bar(x + (index - 1.5) * width,
            values[column_name],
            width,
            label=column_name)
        )
        ax.bar_label(rects[-1], fmt=f'%.{ndigits}f', padding=3, rotation=90, fontsize=8)

    # Set y-limit slightly higher to accommodate labels
    all_vals = []
    for _, record in data.items():
        for column_name, value in record.items():
            all_vals.append(value)
    if all_vals:
        ax.set_ylim(0, max(all_vals) * 1.2)

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
    data_1 = {
        'small': {'Boyer-Moore': 0.512, 'KMP': 1.277, 'Rabin-Karp': 2.864, 'Regex': 0.065},
        'big': {'Boyer-Moore': 5.121, 'KMP': 43.367, 'Rabin-Karp': 96.777, 'Regex': 0.341},
        'non_existent_small': {'Boyer-Moore': 27.517, 'KMP': 52.086,
            'Rabin-Karp': 115.522, 'Regex': 0.443},
        'non_existent_big': {'Boyer-Moore': 4.524, 'KMP': 51.015,
            'Rabin-Karp': 117.862, 'Regex': 0.369}
    }

    data_2 = {
        'small': {'Boyer-Moore': 0.223, 'KMP': 0.364, 'Rabin-Karp': 0.754, 'Regex': 0.041},
        'big': {'Boyer-Moore': 11.557, 'KMP': 73.802, 'Rabin-Karp': 165.409, 'Regex': 0.670},
        'non_existent_small': {'Boyer-Moore': 20.145, 'KMP': 75.604,
            'Rabin-Karp': 166.065, 'Regex': 0.630},
        'non_existent_big': {'Boyer-Moore': 7.189, 'KMP': 72.506,
            'Rabin-Karp': 168.564, 'Regex': 0.504}
    }

    create_chart('Час виконання алгоритмів для Тексту 1', data_1, 'стаття_1_chart.png')
    create_chart('Час виконання алгоритмів для Тексту 2', data_2, 'стаття_2_chart.png')
