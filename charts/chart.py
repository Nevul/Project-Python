import matplotlib.pyplot as plt

#Aquí generamos un gráfico de tipo pastel(pie) y lo guardamos como un archivo .png
def generate_pie_chart():
    labels = ['Alex', 'Karen', 'Dayana']
    values = [25, 23, 26]

    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    plt.savefig('charts/pie.png')
    plt.close()