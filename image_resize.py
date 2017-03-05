from PIL import Image
import argparse
import os.path


def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('--scale', help='Пропорциональное изменение размера в N раз')
	parser.add_argument('--width', help='Ширина')
	parser.add_argument('--height', help='Высота')
	parser.add_argument('--path', help='Путь')
	arguments = parser.parse_args()
	print(arguments.scale)
	return arguments



def get_path_to_original(arguments):
	if arguments:
		file_path = arguments
	else:
		file_path = input('Введи путь к изображению: ')

	if os.path.isfile(file_path):
			return file_path

	print('Такого файла нет!')
	get_path_to_original(arguments)	


def resize_image(path_to_original, path_to_result, scale, ):
    original_image = Image.open(path_to_original)


if __name__ == '__main__':
    arguments = get_arguments()
    file_path = get_path_to_original(arguments)

