import onnx
from onnx import helper
from onnx import TensorProto
import base64

def make_model(name, op_type):
    # Shape [1, 10, 30, 30]
    X = helper.make_tensor_value_info('input', TensorProto.FLOAT, [1, 10, 30, 30])
    Y = helper.make_tensor_value_info('output', TensorProto.FLOAT, [1, 10, 30, 30])

    if op_type == 'invert':
        # invert colors assuming 0-9. Output = 9 - input
        const_tensor = helper.make_tensor('const', TensorProto.FLOAT, [1], [9.0])
        const_node = helper.make_node('Constant', inputs=[], outputs=['const_out'], value=const_tensor)
        node = helper.make_node('Sub', inputs=['const_out', 'input'], outputs=['output'])
        graph = helper.make_graph([const_node, node], name, [X], [Y])

    model = helper.make_model(graph, producer_name='arc-solver')
    onnx.save(model, f"{name}.onnx")

    with open(f"{name}.onnx", "rb") as f:
        b64 = base64.b64encode(f.read()).decode('utf-8')
    print(f"'{name}': '{b64}',")

make_model('invert', 'invert')
