numbers = request.json.get('numbers')
    if not numbers:
        return jsonify({'message': 'No numbers provided'}), 400

    # Hae käyttäjän token
    token = request.json.get('token')
    if not token:
        return jsonify({'message': 'No token provided'}), 400

    # Hae käyttäjän tiedot
    user = User.query.filter_by(token=token).first()
    if not user:
        return jsonify({'message': 'Invalid token'}), 401

    # Hae lukujen keskiarvon
    total = sum(numbers)
    count = len(numbers)
    average = total / count

    # Palauta JSON-objekti
    return jsonify({'message': f'Average: {average:.2f}'}), 200


@app.route('/median', methods=['GET'])
def get_median():
    '''
    Hae "numbers" kyselyparametri ja palauta lukujen mediaani.  
    @return: JSON-objekti, jossa on "message" avain, joka sisältää lukujen keskiarvon.
    '''orical
orical
    numbers = request.args.get('numbers')
    if not numbers:
        return jsonify({'message': 'No numbers provided'}), 400

    # Hae käyttäjän token
    token = request.args.get('token')
    if not token:
        return jsonify({'message': 'No token provided'}), 400

    # Hae käyttäjän tiedot
    user = User.query.filter_by(token=token).first()
    if not user:
        return jsonify({'message': 'Invalid token'}), 401

    # Hae lukujen keskiarvon
    total = sum(numbers)
    count = len(numbers)
    average = total / count

    # Palauta JSON-objekti
    return jsonify({'message': f'Average: {average:.2f}'}), 200


@app.route('/median', methods=['POST'])
def avg():
    '''
    Hae "numbers" kyselyparametri ja palauta lukujen mediaani.  
    @return: JSON-objekti, jossa on "message" avain, joka sisältää lukujen keskiarvon.