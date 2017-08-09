from src import process_image

if __name__ == '__main__':
    image = process_image.process_image('..\\l.png')
    with open('test.txt', 'w') as f:
        f.write(" ".join(map(str, image)))
