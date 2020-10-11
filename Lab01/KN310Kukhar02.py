import matplotlib.pyplot as plt
import seaborn as sns


def draw_hist_plot(data_type, data):
    plt.hist(data[data_type])
    plt.xlabel(data_type)
    plt.show()


def draw_pie_plot(data_type, data):
    sum = data.groupby(data_type).size().reset_index(name=data_type+'_val')
    sum.set_index(data_type, inplace=True)
    sum.plot.pie(y=data_type+'_val', figsize=(15, 15), labels=None)
    plt.show()


def draw_dot_plot(data_type, data):
    min_value = data.groupby('Date').agg({data_type: 'min'})

    plt.plot(min_value, 'o')

    plt.ylabel(data_type)
    plt.xlabel('Date')
    plt.xticks(rotation=45)

    plt.show()


def draw_box_plot(data_type, data):
    plt.figure(figsize=(15, 15))
    ax = sns.boxplot(x="Date", y=data_type, data=data)
    plt.xticks(rotation=45)
    plt.show()


def draw_linear_plot(data_type, data):
    max_value = data.groupby('Date').agg({data_type: 'max'})
    min_value = data.groupby('Date').agg({data_type: 'min'})

    plt.plot(min_value, label="Min")
    plt.plot(max_value, label="Max")
    plt.legend(loc='upper left')

    plt.ylabel(data_type)
    plt.xlabel('Date')
    plt.xticks(rotation=45)

    plt.show()


def draw_plots(data):
    available_data_types = ['Temperature', 'Dew Point', 'Humidity',
                            'Wind Speed', 'Wind Gust', 'Pressure',
                            'Precip.', 'Precip Accum']

    def print_available_data_types():
        for i in range(len(available_data_types)):
            print(i + 1, available_data_types[i])

    while True:
        print("Available plots: \n1. Linear\n2. Histogram\n3. Box\n4. Dot\n5. Pie")

        plot_type = int(input(": "))
        if plot_type == 1:
            print("Available types for linear plot:")
            print_available_data_types()

            chosen_data_types = list(map(int, input(": ").split(" ")))

            for t in chosen_data_types:
                draw_linear_plot(available_data_types[t-1], data)
        elif plot_type == 2:
            print("Available types for hist plot:")
            print_available_data_types()

            chosen_data_types = list(map(int, input(": ").split(" ")))

            for t in chosen_data_types:
                draw_hist_plot(available_data_types[t - 1], data)
        elif plot_type == 3:
            print("Available types for box plot:")
            print_available_data_types()

            chosen_data_types = list(map(int, input(": ").split(" ")))

            for t in chosen_data_types:
                draw_box_plot(available_data_types[t - 1], data)

        elif plot_type == 4:
            print("Available types for dot plot:")
            print_available_data_types()

            chosen_data_types = list(map(int, input(": ").split(" ")))

            for t in chosen_data_types:
                draw_dot_plot(available_data_types[t - 1], data)
        elif plot_type == 5:
            print("Available types for pie plot:")
            print("1. Wind\n2. Condition")
            available_pie_data_types = ['Wind', 'Condition']
            chosen_data_types = list(map(int, input(": ").split(" ")))

            for t in chosen_data_types:
                draw_pie_plot(available_pie_data_types[t - 1], data)
