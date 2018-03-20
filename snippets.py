### matplotlib

# 9 Bilder ohne Text in 3x3 Gitter anzeigen
fig = plt.figure(figsize=(20,20))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
for i in range(9):
    ax = fig.add_subplot(3, 3, i + 1, xticks=[], yticks=[])
    plot_data(X_train[i], y_train[i], ax)


# geht doch nicht so, weil das neue Bild doch nicht die gewünschte Länge hat, sondern verzogen aussieht?
import Image
image1 = Image.open('data/test/test3.jpg')
image2 = image1.copy()
image2.thumbnail((200, 200), Image.ANTIALIAS)