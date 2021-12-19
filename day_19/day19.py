
def rotate(img):
    h = len(img)
    w = len(img[0])
    hh = w
    ww = h

    for j in range(hh):
        for i range(ww):
            




with open('input.txt') as f:
    rdata = [x.strip() for x in f.read().split('\n\n')]

sd = {}
for rdatum in rdata:
    datum = [x.strip() for x in rdatum.split('\n')]
    sn = int(datum[0].replace('scanner','').replace('-','').replace(' ',''))
    bs = datum[1:]
    sd[sn] = []
    for b in bs:
        x,y,z = b.split(',')
        sd[sn].append((int(x),int(y),int(z)))
                      
for s in sd:
