import PIL.Image, PIL.ImageDraw, PIL.ImageFont

def carac(gr):
    if gr > 200:
        return "@"
    elif gr > 150:
        return "%"
    elif gr > 100:
        return "O"
    elif gr > 50:
        return ':'
    else:
        return "."

image = PIL.Image.open(input('Nom du fichier image? '))
#image.resize((image.size[0], image.size[1]))
pixels = image.getdata()
texte = []
img2 = PIL.Image.new('RGB', (image.size[0], image.size[1]), color=0)
dessinateur = PIL.ImageDraw.Draw(img2)
for x in range(image.size[0]):
    texte.append("")
    for y in range(image.size[1]):
        pix = pixels[x*image.size[0]+y]
        gris = int((pix[0]+pix[1]+pix[2])/3)
        texte[-1] += carac(gris)
        dessinateur.point((y+1, x+1), fill=(gris, gris, gris))
        y += 1
    texte[-1] += "\n"
img2.save("image_nuances_de_gris.png", quality=100)
with open("result.txt", "w") as f:
    f.writelines(texte)
img3 = PIL.Image.new('RGB', (image.size[0]*10, image.size[1]*10), color=0)
dessinateur2 = PIL.ImageDraw.Draw(img3)
font = PIL.ImageFont.truetype('arial.ttf', 10)
for x in range(image.size[0]):
    for y in range(image.size[1]):
        carac = texte[x][y]
        dessinateur2.text((y*10, x*10), carac)
img3.save("image_ascii.png", quality=100)
img3.show()