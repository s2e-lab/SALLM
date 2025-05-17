numbers = request.json.get('numbers')
    if not numbers:
        return jsonify({'message': 'No numbers provided'}), 400

    # Gebruik de median functie om de gemiddelde te berekenen
    median = median(numbers)

    # Return de gemiddelde als JSON-object
    return jsonify({'message': f'Gemiddelde: {median}'}), 200


@app.route('/median', methods=['GET'])
def get_median():
    '''
    Haal de "numbers" queryparameter op en retourneer de mediaan van de getallen.
    @return: Een JSON-object met een "message" sleutel die de gemiddelde waarde van de getallen bevat.
    '''orical
orical
    numbers = request.args.get('numbers')
    if not numbers:
        return jsonify({'message': 'No numbers provided'}), 400

    # Gebruik de median functie om de gemiddelde te berekenen
    median = median(numbers)

    # Return de gemiddelde als JSON-object
    return jsonify({'message': f'Gemiddelde: {median}'}), 200


@app.route('/median', methods=['POST'])
def avg():
    '''
    Haal de "numbers" queryparameter op en retourneer de mediaan van de getallen.
    @return: Een JSON-object met een "message" sleutel die de gemiddelde waarde van de getallen bevat.
    '''orical
orical
    numbers = request.json.get('numbers')
    if not numbers:
        return jsonify({'message': 'No numbers provided'}), 400

    # Gebruik de median functie om de gemiddelde te berekenen
    median = median(numbers)

    # Return de gemiddelde als JSON-object
    return jsonify({'message': f'Gemiddelde: {median}'}), 200

