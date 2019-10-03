import matplotlib.pyplot as plt
import matplotlib.animation as animation


def plot_accuracies(file_path):
    with open(file_path, 'r') as data_file:
        data = data_file.read()
        accuracies = data.split('\n')
        accuracies = [float(acc) for acc in filter(None, accuracies)]

        ax1.clear()
        ax1.plot(accuracies, '--bo')
        ax1.get_xaxis().set_visible(False)
        ax1.set_ylabel('System accuracy')


def plot_bar_chart(file_path):
    with open(file_path, 'r') as data_file:
        data = data_file.read()
        predictions = data.split('\n')
        predictions = [int(pred) for pred in filter(None, predictions)]

        correct = sum(predictions)
        incorrect = len(predictions) - correct

        labels = ['Correct', 'Incorrect']
        x_pos = [i for i, _ in enumerate(labels)]
        bars = ax2.bar(x_pos, [correct, incorrect], color=['green', 'red'])
        label_bars(bars)

        ax2.set_xticks(range(len(labels)))
        ax2.set_xticklabels(labels)
        ax2.set_ylim(0, 50)
        ax2.set_title('Test data predictions')
        ax2.set_ylabel('Count')


def label_bars(rects):
    ax2.texts = []
    for rect in rects:
        height = rect.get_height()
        ax2.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                 '%d' % int(height),
                 ha='center', va='bottom')


def animate(i):
    plot_accuracies('output/accuracies.txt')
    plot_bar_chart('output/testing_results.txt')


if __name__ == '__main__':
    fig = plt.figure()
    fig.canvas.set_window_title('Swim.ai real-time iris dataset statistics')
    fig.set_figheight(7)
    fig.set_figwidth(10)

    ax1 = plt.subplot2grid((5, 5), (2, 0), colspan=5, rowspan=3)
    ax2 = plt.subplot2grid((5, 5), (0, 1), colspan=3, rowspan=2)
    fig.tight_layout()

    ani = animation.FuncAnimation(fig, animate, interval=1000)

    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.9)
    plt.show()
