from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    # 记录服务器接收时间
    server_receive_time = time.time()
    try:
        # 获取客户端发送的 JSON 数据
        data = request.json
        if not data or 'message' not in data or 'client_send_time' not in data:
            return jsonify({'error': 'Missing message or client_send_time'}), 400

        # 模拟处理（替换为你的推理逻辑）
        # time.sleep(1)

        # 记录服务器发送时间
        server_send_time = time.time()

        # 构造响应，包含时间戳
        response = {
            'reply': 'World',
            'server_receive_time': server_receive_time,
            'server_send_time': server_send_time
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask server")
    app.run(host='0.0.0.0', port=5000)
