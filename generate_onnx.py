import onnx
from onnx import helper
from onnx import TensorProto
import base64

def make_model(name, op_type):
    # Shape [1, 10, 30, 30]
    X = helper.make_tensor_value_info('input', TensorProto.FLOAT, [1, 10, 30, 30])
    Y = helper.make_tensor_value_info('output', TensorProto.FLOAT, [1, 10, 30, 30])

    if op_type == 'identity':
        node = helper.make_node('Identity', inputs=['input'], outputs=['output'])
        graph = helper.make_graph([node], name, [X], [Y])
    elif op_type == 'add':
        # Add 1.0 to input
        const_tensor = helper.make_tensor('const', TensorProto.FLOAT, [1], [1.0])
        const_node = helper.make_node('Constant', inputs=[], outputs=['const_out'], value=const_tensor)
        node = helper.make_node('Add', inputs=['input', 'const_out'], outputs=['output'])
        graph = helper.make_graph([const_node, node], name, [X], [Y])
    elif op_type == 'mul':
        # Multiply by 0.0 (mask)
        const_tensor = helper.make_tensor('const', TensorProto.FLOAT, [1], [0.0])
        const_node = helper.make_node('Constant', inputs=[], outputs=['const_out'], value=const_tensor)
        node = helper.make_node('Mul', inputs=['input', 'const_out'], outputs=['output'])
        graph = helper.make_graph([const_node, node], name, [X], [Y])

    model = helper.make_model(graph, producer_name='arc-solver')
    onnx.save(model, f"{name}.onnx")

    with open(f"{name}.onnx", "rb") as f:
        b64 = base64.b64encode(f.read()).decode('utf-8')
    print(f"{name}_b64 = '{b64}'")

make_model('identity', 'identity')
make_model('broadcast', 'add')
make_model('mask', 'mul')
