from PIL import Image,ImageDraw,ImageFont

def main(t="AB cd",xy=(2,0),height = 128,width = 64):
    im = Image.new("RGB",(height,width),(0,0,0))
    font = ImageFont.truetype("simsun.ttc", 16, encoding="unic")
    new_im = ImageDraw.Draw(im)
    new_im.text(xy,t,font=font,fill=(255,255,255))
    im.save('a.jpg')
    save_im = im.convert("L")
    return save_im

if __name__ == "__main__":
    main()
    pass
