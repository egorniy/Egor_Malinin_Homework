import matplotlib.pyplot as plt


def draw():
    while True:
        if input('Continue? ') == 'n':
            break
        else:
            xs = input('x: ')
            ys = input('y: ')
            color = input("color: ")
        try:
            xs_int = [int(x) for x in xs.split()]
            ys_int = [int(y) for y in ys.split()]
            if color:
                plt.plot(xs_int, ys_int, color = color)
            else:
                plt.plot(xs_int, ys_int)
        except Exception as e:
            print(e)
    plt.show()


def draw_plots(*args, **kwargs):
    i = 1
    keys = kwargs.keys()
    for x, y in args:
        color = 'color_'+str(i)
        try:
            if color in keys:
                plt.plot(x, y, color = kwargs[color])
            else:
                plt.plot(x, y)
        except Exception as e:
            print(e)
        i += 1
    plt.show()

# draw_plots(([3,4, 6], [6, 9, 7]), color= 'red')


def draw_pie(*args):
    sizes, colors, labels = [], [], []
    for size, color, label in args:
        sizes.append(size)
        colors.append(color)
        labels.append(label)
    plt.pie(sizes, colors=colors, autopct='%1.2f%%', startangle= 90)
    plt.legend(labels, loc ='best')
    plt.show()

# draw_pie((12, 'red', 'vasrdsuyd'), (13, 'blue', '2'))

def draw_bar(*args, colors):
    x, y = [], []
    for xs, ys, color in args:
        x.append(xs)
        y.append(ys)
        colors.append(color)
    bars = plt.bar(x, y)
    if colors:
        for i in range(len(bars)):
            bars[i].set_color(colors[i])
    plt.show()



# draw()
draw_plots(([3,4, 6], [6, 9, 7]), color_1= 'red')
draw_pie((12, 'red', 'vasrdsuyd'), (13, 'blue', '2'))
draw_bar(([10, 23, 23]),([12, 34, 56]), colors =['red', 'black'])
