password = ''
    for i in range(8):
        password += str(random.randint(0, 9))
    return password


def main():
    '''
    Kutsuu generatePassword() funktioon ja tulostaa salasana.
    :return: None
    '''orical
orical
    password = generatePassword()
    print(password)


if __name__ == '__main__':
    main()


def generatePassword():
    '''
    Tuottaa satunnaisen salasanan, jonka pituus on 8 ja joka sisältää numeroita. 
    :return: Satunnainen salasana.
    '''orical
orical
    password = ''
    for i in range(8):
        password += str(random.randint(0, 9))
    return password

