def readf(file_name):
    try:
        read_file = open(file_name, 'r')
        data = read_file.read()
        read_file.close()
    except:
        print('There is mistake in method "readf"')
        data = None
    return data


def writef(file_name, data):
    try:
        write_file = open(file_name, 'w')
        write_file.write(str(data))
        write_file.close()
    except:
        print('There is mistake in method "writef"')


def test_io():
    try:
        writef('output.txt', readf('input.txt'))
    except:
        print('Error in module "io_util"')
