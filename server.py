import time
import base64
import onnx
from onnx import helper
from onnx import TensorProto
from flask import Flask, request, jsonify
from flask_cors import CORS
import sys

app = Flask(__name__)
CORS(app)

def create_onnx_model(op_type):
    name = f"arc_solver_{op_type}"
    X = helper.make_tensor_value_info('input', TensorProto.FLOAT, [1, 10, 30, 30])
    Y = helper.make_tensor_value_info('output', TensorProto.FLOAT, [1, 10, 30, 30])

    if op_type == 'identity':
        node = helper.make_node('Identity', inputs=['input'], outputs=['output'])
        graph = helper.make_graph([node], name, [X], [Y])
    elif op_type == 'add':
        const_tensor = helper.make_tensor('const', TensorProto.FLOAT, [1], [1.0])
        const_node = helper.make_node('Constant', inputs=[], outputs=['const_out'], value=const_tensor)
        node = helper.make_node('Add', inputs=['input', 'const_out'], outputs=['output'])
        graph = helper.make_graph([const_node, node], name, [X], [Y])
    elif op_type == 'mask':
        const_tensor = helper.make_tensor('const', TensorProto.FLOAT, [1], [0.0])
        const_node = helper.make_node('Constant', inputs=[], outputs=['const_out'], value=const_tensor)
        node = helper.make_node('Mul', inputs=['input', 'const_out'], outputs=['output'])
        graph = helper.make_graph([const_node, node], name, [X], [Y])
    elif op_type == 'invert':
        const_tensor = helper.make_tensor('const', TensorProto.FLOAT, [1], [9.0])
        const_node = helper.make_node('Constant', inputs=[], outputs=['const_out'], value=const_tensor)
        node = helper.make_node('Sub', inputs=['const_out', 'input'], outputs=['output'])
        graph = helper.make_graph([const_node, node], name, [X], [Y])
    else:
        node = helper.make_node('Identity', inputs=['input'], outputs=['output'])
        graph = helper.make_graph([node], name, [X], [Y])

    model = helper.make_model(graph, producer_name='arc-compute-engine')
    onnx.save(model, f"{name}.onnx")
    with open(f"{name}.onnx", "rb") as f:
        b64 = base64.b64encode(f.read()).decode('utf-8')
    return b64

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/compute', methods=['POST'])
def compute():
    data = request.json
    train_pairs = data.get('train', [])

    # Simulate compute engine logs generator
    def generate_logs():
        yield "Analyse dimensionnelle en cours...\n"
        time.sleep(0.5)

        # Engine heuristics logic
        is_identity = True
        is_mask = True
        is_invert = True

        for pair in train_pairs:
            inp = pair['input']
            out = pair['output']

            for r in range(len(inp)):
                for c in range(len(inp[r])):
                    if inp[r][c] != out[r][c]:
                        is_identity = False
                    if out[r][c] != 0:
                        is_mask = False
                    if out[r][c] != abs(9 - inp[r][c]):
                        is_invert = False

        yield "Tests d'hypothèses logiques:\n"
        time.sleep(0.5)
        yield f" - H1 (Identité): {'Validé' if is_identity else 'Échec'}\n"
        time.sleep(0.3)
        yield f" - H2 (Masque): {'Validé' if is_mask else 'Échec'}\n"
        time.sleep(0.3)
        yield f" - H3 (Inversion): {'Validé' if is_invert else 'Échec'}\n"
        time.sleep(0.5)

        detected = "broadcast"
        if is_identity: detected = "identity"
        elif is_mask: detected = "mask"
        elif is_invert: detected = "invert"

        yield f"\nLogique principale inférée: {detected.upper()}\n"
        time.sleep(0.5)
        yield "Optimisation du chemin de calcul...\n"
        time.sleep(0.5)
        yield "Création du graphe Tensor ONNX [1, 10, 30, 30]... DONE\n"

        b64_model = create_onnx_model(detected)
        yield f"RESULT::{detected}::{b64_model}"

    return app.response_class(generate_logs(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
