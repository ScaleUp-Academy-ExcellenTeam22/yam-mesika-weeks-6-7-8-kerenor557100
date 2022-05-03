#submitted by Keren Or Hadad 208025205

from PIL import Image


def remember_and_remember(path: str) -> str:
    '''
    At this function we receives a path to an image,
    and-> according to the number of lines of the black pixels finds the message.
    :param path: string of path of image file.
    :return: The decrypted file.
    '''
    image = Image.open(path)
    width, high = image.size
    letter = [chr(row) for column in range(width) for row in range(high) if image.load()[column, row] == 1]
    return ''.join(letter)


print(remember_and_remember("code.png"))


"""
output:  
Place gunpowder beneath the House of Lords. 11/05/1605
"""
