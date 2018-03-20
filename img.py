# Bild mit Titel anzeigen, ohne Schnickschnack
fig = plt.figure(figsize = (8,8))
ax1 = fig.add_subplot(111)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_title('Image with sunglasses')
ax1.imshow(img)

# Alpha-Kanal mit einlesen
img = cv2.imread("sunglasses.png", cv2.IMREAD_UNCHANGED)