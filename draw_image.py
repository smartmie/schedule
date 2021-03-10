from PIL import Image
import draw_text

def get_point_bin(f):
    f = f.convert("L")
    f = img_resize(f)
    test = []
    BinTOHex = ""

    for y in range(0,f.height):
        x = -1
        while x +8 <= f.width-1:
            for g in range(x+1,x+9):
                test.append('1' if f.getpixel((g,y)) > 90 else '0')
                pass
            BinTOHex = BinTOHex +out_image_hex(test)+','
            test.clear()
            x = g
            pass

    return BinTOHex.strip(',')

def out_image_hex(t):
    new_list = t[::-1]
    text = str(int(''.join([c.replace('0b', '') for c in new_list]),2))
    return text

def img_resize(im):
    mod_width = im.width % 8
    mod_height = im.height % 8

    im2 = Image.new("RGB",(im.width+mod_width,im.height + mod_height),(0,0,0))
    im2 = im2.convert("L")
    im2.paste(im,(0,0))
    
    return im2


if __name__ == "__main__":
    with open('a.txt',"w") as f:
        f.write("const unsigned char col[] U8X8_PROGMEM = {"+get_point_bin(draw_text.main("圣诞节快乐\n芝士"))+"};")
    pass


