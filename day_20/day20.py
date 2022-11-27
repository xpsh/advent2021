def extend_dark(img):
    blank_row = ''.join(['.' for x in range(len(img[0])+4)])
    ext_img = [blank_row,blank_row]
    for row in img:
        ext_row = f'..{row}..'
        ext_img.append(ext_row)
    ext_img.append(blank_row)
    ext_img.append(blank_row)
    return ext_img

def extend_light(img):
    blank_row = ''.join(['#' for x in range(len(img[0])+4)])
    ext_img = [blank_row,blank_row]
    for row in img:
        ext_row = f'##{row}##'
        ext_img.append(ext_row)
    ext_img.append(blank_row)
    ext_img.append(blank_row)
    return ext_img

def enhance_img(img,alg):
    out_img = []
    for y in range(1,len(img)-1):
        out_list = []
        for x in range(1,len(img[0])-1):
            pixels = []
            for j in [-1,0,1]:
                for i in [-1,0,1]:
                    pixels.append(img[y+j][x+i])
            number = int(''.join(pixels).replace(".","0").replace("#","1"),2)
            out_list.append(alg[number])
        out_img.append(''.join(out_list))
    return out_img

def count_brights(img):
    count = 0
    for row in img:
        for x in row:
            if x == "#":
                count+=1
    return count
                    
if __name__ == '__main__':
    with open('input.txt','r') as f:
        r_alg, r_img = f.read().split('\n\n')

    alg = ''.join(r_alg.split())
    img =  r_img.split()

    n = 50
    for i in range(n):
        if i%2 and alg[0] == '#':
            print('ha')
            ext_img = extend_light(img)
        else:
            ext_img = extend_dark(img)
        img = enhance_img(ext_img,alg)
        
    
    print(count_brights(img))
