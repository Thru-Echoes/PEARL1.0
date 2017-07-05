import os, re
import rpy2.robjects as ro
from multiprocessing import Pool, cpu_count

print('+++++++++++')
print('Starting...')

def split_seq(seq, size):
    newseq = []
    splitsize = 1.0/size*len(seq)
    for i in range(size):
        newseq.append(seq[int(round(i*splitsize)):int(round((i+1)*splitsize))])
    return newseq

def tif_translate(in_dir, out_dir, file):
    ro.r('''library(raster)
            in_dir <- "%s"
            out_dir <- "%s"
            in_file <- "%s"
            out_file <- gsub(".grd", ".tif", in_file)
            out_file <- gsub(" ", "_", out_file)
            r <- raster(paste(in_dir, in_file, sep=''))
            r[r!=1] <- NA
            writeRaster(r, paste(out_dir, out_file, sep=''), format="GTiff")''' % (in_dir, out_dir, file))

def raster_out (filename):
    print 'making wd\'s'
    _tif_dir = wd + '/pearl_data_18futures/tiff/'
    _tif_dir_c = wd + '/pearl_data_18futures/color_tiff/'
    _color_dir = wd + '/pearl_data_18futures/colors/'
    _tile_dir = wd + '/pearl_data_18futures/tilemaps/'

    if isinstance(filename, list):

        for i in range(0, len(filename)):
            raster_out(filename[i])
    else:
        print filename[1]
        _in_file = _tif_dir + filename[0] + filename[1]
        print 'pattern'
        pattern = '_[a-z]\w+\.'
        print 'modelName'
        modelName = re.findall(pattern,filename[1])[0][1:-1]
        print 'modelIndex'
        modelIndex = models.index(modelName)
        print 'make color file'
        _color_file = _color_dir + 'color_%s.txt'%(modelIndex+1)
        print 'make tile dir'
        _tile_dir = _tile_dir + filename[0] + '/' + modelName
        print 'make out file'
        _out_file = _tif_dir_c + filename[0] + filename[1]
        print _out_file
        print 'doing color_tiff_cmd'
        color_tiff_cmd = 'gdaldem color-relief -of GTiff %s %s %s -alpha' % (_in_file, _color_file, _out_file)
        os.system(color_tiff_cmd)
        print 'doing tile_cmd'
        tile_cmd = 'gdal2tiles.py -z 1-6 %s %s' % (_out_file, _tile_dir)
        os.system(tile_cmd)

def color_file_create(color_dir, color, number):

    _out_dir = color_dir + "/color_%d.txt" % (number)

    with open(_out_dir, "w") as color_file:
        color_file.write('0, red 0\n0, %s' % (color))

print('Creating diretories')

wd = os.getcwd()
origin = wd + '/pearl_data_18futures/origin/'
tif_dir = wd + '/pearl_data_18futures/tiff/'
tif_dir_c = wd + '/pearl_data_18futures/color_tiff/'
color_dir = wd + '/pearl_data_18futures/colors/'
tile_dir = wd + '/pearl_data_18futures/tilemaps/'

if not os.path.exists(tif_dir):
    os.makedirs(tif_dir)
if not os.path.exists(tif_dir_c):
    os.makedirs(tif_dir_c)
if not os.path.exists(color_dir):
    os.makedirs(color_dir)
if not os.path.exists(tile_dir):
    os.makedirs(tile_dir)

#color reference: http://www.rapidtables.com/web/color/RGB_Color.htm
color = ['0 0 255','255 0 0','255 128 0','255 255 0','128 255 0','0 255 0',
 '0 255 128','0 255 255','0 128 255','0 0 255','127 0 255','255 0 255',
 '255 0 127','128 128 128','255 153 153','153 204 255','204 153 255',
'255 255 153','255 204 204']

models = ['current','futureac45','futureac85','futurebc26','futurebc45',
'futurebc60','futurebc85','futurecc26','futurecc45','futurecc60','futurecc85',
'futurehd26','futurehd45','futurehd60','futurehd85','futurehe26','futurehe45',
'futurehe60','futurehe85']

for i in range(0, len(color)):
    color_file_create(color_dir, color[i], i+1)

print('Creating GeoTIFF from R raster...')

for folder in os.listdir(wd + '/pearl_data_18futures/origin/'):
    if not folder.startswith('.') and not folder.endswith('.csv'):

        in_dir = origin + folder + '/'
        out_dir = tif_dir + folder + '/'

        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        for file in os.listdir(in_dir):
            if not file.startswith('.') and not file.endswith('.csv') and not file.endswith('.gri'):
                tif_translate(in_dir, out_dir, file)

file_list = []

for folder in os.listdir(tif_dir):
    if not folder.startswith('.'):

        in_dir = tif_dir + folder + '/'
        out_dir_c = tif_dir_c + folder + '/'
        out_dir_t = tile_dir + folder + '/'

        if not os.path.exists(out_dir_c):
            os.makedirs(out_dir_c)

        if not os.path.exists(out_dir_t):
            os.makedirs(out_dir_t)

        for tif in os.listdir(in_dir):
            if not tif.startswith('.'):
                tile_dir_model = out_dir_t + tif.strip('tif').strip('.').split('_')[2]
                if not os.path.exists(tile_dir_model):
                    os.makedirs(tile_dir_model)
                file_list.append((folder, '/' + tif))

print('Creating tile maps....')

numprocessors = cpu_count()
split_filenames = split_seq(file_list, numprocessors)

p = Pool(numprocessors)
result = p.map(raster_out, split_filenames)

print('Finished!!')
print('+++++++++++')
