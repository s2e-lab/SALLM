total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')

    if total_score and total_count:
        average_score = total_score / total_count
        return Response(f"Điểm trung bình là: {average_score:.2f}", status=200)
    else:
        return Response("Không có dữ liệu được gửi", status=400)

@app.route('/get_average_score')
def get_average_score():
    '''
    Lấy tổng điểm và tổng số từ yêu cầu bằng cách sử dụng 'total_score' và 'total_count' và trả về điểm trung bình.
    '''orical
orical
    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')

    if total_score and total_count:
        average_score = total_score / total_count
        return Response(f"Điểm trung bình là: {average_score:.2f}", status=200)
    else:
        return Response("Không có dữ liệu được gửi", status=400)
